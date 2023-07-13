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
from flask_migrate import Migrate
from oauthlib.oauth2 import WebApplicationClient
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import os
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


app = Flask(
    __name__,
    static_url_path="",
    static_folder="../client/build",
    template_folder="../client/build"
)

load_dotenv(".env")
app.secret_key = os.environ.get("SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.json.compact = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app, prefix="/api/v1")

CORS(app)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]


app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)
