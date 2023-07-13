from blueprints import (
    Resource,
    request, 
    session, 
    Blueprint, 
    make_response, 
    abort, 
    g
)

from config import app 
from models import db
from models.user import User
from schemas.user_schema import UserSchema

users_schema = UserSchema(many=True)
users_bp = Blueprint("users", __name__, url_prefix="/users")

class Users(Resource):
    def get(self): 
        users = User.query.order_by(User.created_at.desc()).all()
        return make_response(users_schema.dump(users), 200)