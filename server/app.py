#!/usr/bin/env python3

from flask import request
from flask_restful import Resource

from config import (
    app, 
    db, 
    api, 
    get_jwt, 
    get_jwt_identity,
    make_response, 
    create_access_token, 
    set_access_cookies, 
    jwt_required,
    login_manager,
    current_user,
    requests,
    GOOGLE_DISCOVERY_URL,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    login_user,
    client,
    redirect,
    url_for,
    login_required,
    logout_user
)
from datetime import timedelta, datetime, timezone
import json

# Import models 
from models.author import Author
from models.book_shelf import BookShelf
from models.book_tag import BookTag
from models.book import Book
from models.quote import Quote
from models.review import Review
from models.shelf import Shelf
from models.tag import Tag
from models.user import User

# Import blueprints
from blueprints.auth.signup import signup_bp
from blueprints.auth.login import login_bp
from blueprints.auth.login_with_google import login_with_google_bp
from blueprints.auth.logout import logout_bp
from blueprints.auth.me import me_bp

from blueprints.authors import Authors
from blueprints.author_by_id import AuthorById
from blueprints.books import Books
from blueprints.book_by_id import BookById
from blueprints.book_shelves import BookShelves
from blueprints.book_shelf_by_id import BookShelfById
from blueprints.quotes import Quotes
from blueprints.quote_by_id import QuoteById
from blueprints.shelves import Shelves
from blueprints.shelf_by_id import ShelfById
from blueprints.users import Users
from blueprints.user_by_id import UserById, user_schema
from blueprints.user_by_username import user_by_username_bp

# Add resources

api.add_resource(Authors, "/authors")
api.add_resource(AuthorById, "/authors/<int:id>")
api.add_resource(Books, "/books")
api.add_resource(BookById, "/books/<int:id>")
api.add_resource(BookShelves, "/book_shelves")
api.add_resource(BookShelfById, "/book_shelves/<int:id>")
api.add_resource(Quotes, "/quotes")
api.add_resource(QuoteById, "/quotes/<int:id>")
api.add_resource(Shelves, "/shelves")
api.add_resource(ShelfById, "/shelves/<int:id>")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:id>")

app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)
app.register_blueprint(login_with_google_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(me_bp)

app.register_blueprint(user_by_username_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True, ssl_context="adhoc")
