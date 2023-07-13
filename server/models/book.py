from models import db, association_proxy

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    cover_photo = db.Column(db.String)
    genre = db.Column(db.String, nullable=False)
    page_count = db.Column(db.Integer)
    description = db.Column(db.String)

    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    author = db.relationship("Author", back_populates="books")
    quotes = db.relationship("Quote", back_populates="book")

    reviews = db.relationship("Review", back_populates="book", cascade="all, delete-orphan")
    book_tags = db.relationship("BookTag", back_populates="book", cascade="all, delete-orphan")
    
    book_shelves = db.relationship("BookShelf", back_populates="book")
    shelves = association_proxy("book_shelves", "shelf")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return (
            f"Book #{self.id}:"
            + f"Title: {self.title}"
            + f"Author: {self.author}"
        )