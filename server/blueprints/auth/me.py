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
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    jwt_required,
    get_jwt_identity,
    cache
) 

from models import db
from models.user import User
from blueprints.user_by_id import user_schema

me_bp = Blueprint("me", __name__)

@me_bp.route("/me")
# @cache.memoize(50)
def me():
    if id_ := session.get("user_id"):
        if user := db.session.get(User, id_):
            return make_response({"user": user_schema.dump(user)}, 200)
    return {}

