from schemas import (
    fields,
    validate,
    validates,
    ValidationError,
    ma,
    Book
)
from schemas.author_schema import AuthorSchema

class BookSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Book
        load_instance = True
        ordered = True
        fields = ("id", "title", "cover_photo", "genre", "page_count", \
                "description", "author", "shelves", "book_shelves", "url")
        
    title = fields.String(validate=validate.Length(min=1, max=150), \
                    error="Title must be less than 150 characters")
    description = fields.String(validate=validate.Length(min=1, max=2000), \
                    error="Description must be less than 2000 characters")
    page_count = fields.Integer(strict=True, \
                    validate=validate.Range(min=1, max=25000), \
                    error="Page count must be between 1 and 25000")
    author = fields.Nested(AuthorSchema, only=("id", "full_name", "url"))
    book_shelves = fields.Nested("BookShelfSchema", only=("id", "url"), many=True)
    shelves = fields.Nested("ShelfSchema", only=("id", "name", "user_id"), many=True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "bookbyid",
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor("books")
        }
    )

    @validates("genre")
    def validates_genre(self, genre): 
        ACCEPTED_GENRES = ["Poetry", "Fantasy", "Historical Fiction", "Memoir", 
                "Literary Fiction", "Horror", "Drama", "Children's"]
        if genre not in ACCEPTED_GENRES: 
            raise ValidationError("Genre not valid")