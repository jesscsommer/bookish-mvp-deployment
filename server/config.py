from flask import (
    Flask, 
    make_response, 
    redirect, 
    request, 
    url_for
)
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_cors import CORS
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)
from flask_migrate import Migrate
from oauthlib.oauth2 import WebApplicationClient
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from os import environ
from dotenv import load_dotenv
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    get_jwt_identity,
    jwt_required,
    JWTManager,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    get_jwt,
    verify_jwt_in_request
)
from datetime import timedelta, datetime, timezone
import requests


app = Flask(__name__)

load_dotenv(".env")
app.secret_key = environ.get("SECRET_KEY")
app.config["JWT_SECRET_KEY"] = environ.get("JWT_SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.json.compact = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

CORS(app)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]


app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)

GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

login_manager = LoginManager()
login_manager.init_app(app)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

# @refresh_bp.route("/refresh", methods=["POST"])
# @jwt_required(refresh=True)
# def refresh():
#     user_id = get_jwt_identity()
#     user = db.session.get(User, user_id)

#     new_access_token = create_access_token(identity=user_id)
#     res = make_response({"user": user_schema.dump(user)}, 200)

#     set_access_cookies(res, new_access_token)

#     return res
