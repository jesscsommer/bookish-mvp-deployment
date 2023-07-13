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
from models.book_shelf import BookShelf
from schemas.book_shelf_schema import BookShelfSchema

book_shelf_schema = BookShelfSchema()
book_shelf_by_id_bp = Blueprint("book_shelf_by_id", __name__, url_prefix="/book_shelves/<int:id>")

class BookShelfById(Resource):
    def get(self, id): 
        if book_shelf := book_shelf_schema.dump(db.session.get(BookShelf, id)):
            return make_response(book_shelf, 200)
        return make_response({"error": "Book shelf not found"}, 404)
    def delete(self, id):
        try:
            book_shelf = db.session.get(BookShelf, id)
            db.session.delete(book_shelf)
            db.session.commit()
            return make_response({}, 204)
        except Exception as e:
            return make_response({"error": "Book shelf not found"}, 404)