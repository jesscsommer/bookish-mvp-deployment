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
from blueprints.user_by_id import user_schema

user_by_username_bp = Blueprint("user_by_username", __name__)

@user_by_username_bp.route("/users/<string:username>", methods=["GET"])
def user_by_username(username):
    if user := User.query.filter(User.username == username).first():
        return make_response(user_schema.dump(user), 200)
    return make_response({"error": "User not found"}, 404) 
