from schemas import (
    fields,
    validate,
    ma,
    Author
)

class AuthorSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Author
        load_instance = True
        ordered = True
        fields = ("id", "full_name", "bio", "books", "url")

    bio = fields.String(validate=validate.Length(max=250, \
                        error="Bio must be less than 250 chars"))
    books = fields.Nested("BookSchema", only=("id", "title", "url"), many=True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "authorbyid",
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor("authors")
        }
    )