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

author_schema = AuthorSchema()
author_by_id_bp = Blueprint("author_by_id", __name__, url_prefix="/authors/<int:id>")

class AuthorById(Resource):
    def get(self, id): 
        if author := author_schema.dump(db.session.get(Author, id)):
            return make_response(author, 200)
        return make_response({"error": "Author not found"}, 404)