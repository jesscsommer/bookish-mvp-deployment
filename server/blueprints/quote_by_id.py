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
from models.quote import Quote
from schemas.quote_schema import QuoteSchema

quote_schema = QuoteSchema()
quote_by_id_bp = Blueprint("quote_by_id", __name__, url_prefix="/quotes/<int:id>")

class QuoteById(Resource):
    def get(self, id): 
        if quote := quote_schema.dump(db.session.get(Quote, id)):
            return make_response(quote, 200)
        return make_response({"error": "Quote not found"}, 404)