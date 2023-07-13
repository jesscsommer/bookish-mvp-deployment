from schemas import (
    fields,
    validate,
    ma,
    Quote
)

class QuoteSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Quote
        load_instance = True
        ordered = True
        fields = ("id", "content", "book", "url")

    content = fields.String(required=True, \
                            validate=validate.Length(min=1, max=1000), \
                            error="Quote must be less than 1000 characters")
    book = fields.Nested("BookSchema", only=("id", "title", "url"))
    # book = fields.Nested("BookSchema", only=("id", "title", "author.full_name", "url"))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "quotebyid",
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor("quotes")
        }
    )