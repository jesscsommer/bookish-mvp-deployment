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

quotes_schema = QuoteSchema(many=True)
quotes_bp = Blueprint("quotes", __name__, url_prefix="/quotes")

class Quotes(Resource):
    def get(self): 
        quotes = Quote.query.order_by(Quote.created_at.desc()).all()
        return make_response(quotes_schema.dump(quotes), 200)