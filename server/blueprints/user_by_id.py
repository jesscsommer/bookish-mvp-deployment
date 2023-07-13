from blueprints import (
    Resource,
    request, 
    session, 
    Blueprint, 
    make_response, 
    abort, 
    g
)

from config import app, jwt_required, get_jwt_identity
from models import db
from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema()
user_by_id_bp = Blueprint("user_by_id", __name__, url_prefix="/users/<int:id>")

class UserById(Resource):
    def get(self, id): 
        if user := user_schema.dump(db.session.get(User, id)):
            return make_response(user, 200)
        return make_response({"error": "User not found"}, 404)
    
    def patch(self, id):
        if user := db.session.get(User, id):
            try:
                if user.id == session["user_id"]:
                    data = request.get_json()
                    user_schema.validate(data)

                    updated_user = user_schema.load(data, instance=user, \
                                                    partial=True)
                    db.session.commit()
                    return make_response(user_schema.dump(updated_user), 200)
            except Exception as e: 
                db.session.rollback()
                return make_response({"error": [str(e)]}, 422)
        return make_response({"error": "User not found"}, 404)

    def delete(self, id):
        if user := db.session.get(User, id): 
            try:
                current_user = db.session.get(User, session["user_id"])
                if user == current_user:
                    db.session.delete(user)
                    db.session.commit()

                    return make_response("", 204)
                return make_response({"error": "Unauthorized"}, 401)
            except Exception as e: 
                db.session.rollback()
                return make_response({"error": [str(e)]}, 400)
        return make_response({"error": "User not found"}, 404)