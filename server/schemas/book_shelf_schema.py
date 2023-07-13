from schemas import (
    fields,
    validates,
    validates_schema,
    ValidationError,
    ma,
    BookShelf
)
    
from schemas.book_schema import BookSchema
from schemas.shelf_schema import ShelfSchema

from models.book import Book
from models.shelf import Shelf
from models.user import User

class BookShelfSchema(ma.SQLAlchemySchema):
    class Meta():
        model = BookShelf
        load_instance = True
        ordered = True
        # fields = ("id", "url")
        fields = ("id", "book", "shelf", "book_id", "shelf_id", "user_id", "url")
        
    book = fields.Nested(BookSchema, exclude=("book_shelves",))
    shelf = fields.Nested(ShelfSchema, only=("id", "name", "user", "books", "url"))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "bookshelfbyid",
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor("bookshelves")
        }
    )

    @validates_schema
    def validate_object(self, data, **kwargs):
        if BookShelf.query.filter(BookShelf.book_id == data["book_id"]) \
                            .filter(BookShelf.shelf_id == data["shelf_id"]) \
                            .first(): 
            raise ValidationError("Book already on that shelf")