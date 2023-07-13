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
from schemas.shelf_schema import ShelfSchema

shelf_schema = ShelfSchema()
shelf_by_id_bp = Blueprint("shelf_by_id", __name__, url_prefix="/shelfs/<int:id>")

class ShelfById(Resource):
    def get(self, id): 
        if shelf := shelf_schema.dump(db.session.get(Shelf, id)):
            return make_response(shelf, 200)
        return make_response({"error": "Shelf not found"}, 404)
    def delete(self, id):
        try:
            shelf = db.session.get(Shelf, id)
            db.session.delete(shelf)
            db.session.commit()
            return make_response({}, 204)
        except Exception as e:
            return make_response({"error": "Shelf not found"}, 404)