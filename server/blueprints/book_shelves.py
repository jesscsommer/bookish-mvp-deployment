from blueprints import (
    Resource,
    request, 
    session, 
    Blueprint, 
    make_response, 
    abort, 
    g
)

from config import app, jwt_required 
from models import db
from models.book_shelf import BookShelf
from schemas.book_shelf_schema import BookShelfSchema

book_shelves_schema = BookShelfSchema(many=True)
book_shelf_schema = BookShelfSchema()
book_shelves_bp = Blueprint("book_shelves", __name__, url_prefix="/book_shelves")

class BookShelves(Resource):
    def get(self): 
        book_shelves = BookShelf.query.order_by(BookShelf.created_at.desc()).all()
        return make_response(book_shelves_schema.dump(book_shelves), 200)
    
    def post(self):
        try: 
            data = request.get_json()
            # import ipdb; ipdb.set_trace()
            book_shelf_schema.validate(data)

            new_book_shelf = book_shelf_schema.load(data)
            db.session.add(new_book_shelf)
            db.session.commit()
            return make_response(book_shelf_schema.dump(new_book_shelf), 201)
        except Exception as e: 
            db.session.rollback()
