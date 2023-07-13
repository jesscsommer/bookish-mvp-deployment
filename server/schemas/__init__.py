from marshmallow import (
    fields, 
    validate,
    validates, 
    validates_schema,
    ValidationError
)
from flask_marshmallow import Marshmallow

from models.author import Author
from models.book_shelf import BookShelf
from models.book_tag import BookTag
from models.book import Book
from models.quote import Quote
from models.review import Review
from models.shelf import Shelf
from models.tag import Tag
from models.user import User

from config import app

ma = Marshmallow(app)