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
from models.author import Author
from schemas.author_schema import AuthorSchema

authors_schema = AuthorSchema(many=True)
authors_bp = Blueprint("authors", __name__, url_prefix="/authors")

class Authors(Resource):
    def get(self): 
        authors = Author.query.order_by(Author.created_at.desc()).all()
        return make_response(authors_schema.dump(authors), 200)