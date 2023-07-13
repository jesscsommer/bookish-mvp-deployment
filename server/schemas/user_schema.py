from schemas import (
    fields, 
    validate, 
    validates, 
    ValidationError, 
    ma, 
    User
)

from models.user import User
import re

class UserSchema(ma.SQLAlchemySchema):
    class Meta(): 
        model = User
        load_instance = True
        ordered = True
        fields = ("id", "username", "display_name", "bio", "profile_pic", 
                "email", "shelves", "book_shelves", "google_unique_id", "url")
        
    
    username = fields.String(required=True, \
                            validate=validate.Length(min=5, max=20, \
                            error="Username must be between 5 and 20 chars"))
    display_name = fields.String(validate=validate.Length(min=5, max=50, \
                        error="Display name must be between 5 and 50 chars"))
    bio = fields.String(validate=validate.Length(max=250, \
                        error="Bio must be less than 250 chars"))
    shelves = fields.Nested("ShelfSchema", exclude=("user",), many=True)
    book_shelves = fields.Nested("BookShelfSchema", many=True)
    
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "userbyid",
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor("users")
        }
    )

    @validates("username")
    def validates_username(self, username):
        if not re.match(r"^[A-z0-9]+$", username):
            raise ValidationError("Username may only contain letters and digits")
        if user := User.query.filter(User.username == username).first():
            if not user.id:
                raise ValidationError("That username is taken")
        
    @validates("email")
    def validates_email(self, email): 
        EMAIL_PATTERN = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|'(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*')@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if not re.match(EMAIL_PATTERN, email):
            raise ValidationError("Invalid email address")
        if user := User.query.filter(User.email == email).first():
            if not user.id:
                raise ValidationError("That email is taken")
        

