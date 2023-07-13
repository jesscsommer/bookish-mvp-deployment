import json

from blueprints import (
    Resource,
    request, 
    session, 
    Blueprint, 
    make_response, 
    abort, 
    g
)

from config import (
    app,
    login_user,
    client,
    redirect,
    url_for,
    login_required,
    logout_user,
    requests,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    GOOGLE_DISCOVERY_URL
) 

from models import db
from models.user import User
from blueprints.user_by_id import user_schema

login_with_google_bp = Blueprint("login_with_google", __name__)

def get_google_provider_cfg():
    ## add error handling
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@login_with_google_bp.route("/login_with_google")
def login_with_google():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@login_with_google_bp.route("/login_with_google/callback")
def callback():
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body) 

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return make_response({"error": "Email not available \
                            or not verified by Google"}, 400)
    
    data = {
        "google_unique_id": unique_id,
        "email": users_email,
        "profile_pic": picture,
        "display_name": users_name,
        "username": users_name
    }

    existing_user = User.query.filter(User.google_unique_id == unique_id).first()

    if not existing_user: 
        user = user_schema.load(data)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id 
        return redirect("http://127.0.0.1:4000"), 301
    
    
    session["user_id"] = existing_user.id 
    return redirect("http://127.0.0.1:4000"), 301