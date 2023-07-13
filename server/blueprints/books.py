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
from models.book import Book
from schemas.book_schema import BookSchema

books_schema = BookSchema(many=True)
books_bp = Blueprint("books", __name__, url_prefix="/books")

class Books(Resource):
    def get(self): 
        books = Book.query.order_by(Book.created_at.desc()).all()
        return make_response(books_schema.dump(books), 200)