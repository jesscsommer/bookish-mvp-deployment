from models import db, association_proxy
from config import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)
    display_name = db.Column(db.String)
    profile_pic = db.Column(db.String)
    bio = db.Column(db.String)
    google_unique_id = db.Column(db.String)

    reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")
    reviewed_books = association_proxy("reviews", "book")

    shelves = db.relationship("Shelf", back_populates="user")
    book_shelves = db.relationship("BookShelf", back_populates="user")
    # book_shelves = association_proxy("shelves", "book_shelves")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    def __repr__(self):
        return (
            f"User #{self.id}: {self.username}"
        )
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed")
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, 
                                            password.encode('utf-8'))
    