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
from models.shelf import Shelf
from models.user import User
from schemas.shelf_schema import ShelfSchema

shelf_schema = ShelfSchema()
shelves_schema = ShelfSchema(many=True)
shelves_bp = Blueprint("shelves", __name__, url_prefix="/shelves")

class Shelves(Resource):
    def get(self): 
        shelves = Shelf.query.order_by(Shelf.created_at.desc()).all()
        return make_response(shelves_schema.dump(shelves), 200)
    
    def post(self):
        try: 
            # import ipdb; ipdb.set_trace()
            data = request.get_json()
            shelf_schema.validate(data)
            data["user_id"] = session["user_id"]

            new_shelf = shelf_schema.load(data)
            db.session.add(new_shelf)
            db.session.commit()
            return make_response(shelf_schema.dump(new_shelf), 201)
        except Exception as e: 
            db.session.rollback()
            return make_response({"error": str(e)}, 422)

