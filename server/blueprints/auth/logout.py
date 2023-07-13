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
from blueprints.auth.me import me

logout_bp = Blueprint("logout", __name__)

@logout_bp.route("/logout", methods=["POST"])
# @login_required
def logout():
    session["user_id"] = None
    return make_response({}, 204)
