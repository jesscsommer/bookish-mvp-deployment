from blueprints import (
    Resource,
    request, 
    session, 
    Blueprint, 
    make_response, 
    abort, 
    g
)

from config import (
    app,
    login_user,
    client,
    redirect,
    url_for,
    login_required,
    logout_user
) 

from models import db
from models.user import User
from blueprints.user_by_id import user_schema

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    try: 
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if user := User.query.filter(User.username == username).first():

            if user.authenticate(password):

                session["user_id"] = user.id

                return make_response({"user": user_schema.dump(user)}, 200)
            
            return make_response({"error": "Invalid credentials"}, 401)
        return make_response({"error": "Invalid credentials"}, 401)
    except: 
        return make_response({"error": "Invalid credentials"}, 401)
