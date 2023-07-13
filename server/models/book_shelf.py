from models import db

class BookShelf(db.Model):
    __tablename__ = "book_shelves"

    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    shelf_id = db.Column(db.Integer, db.ForeignKey("shelves.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    book = db.relationship("Book", back_populates="book_shelves")
    shelf = db.relationship("Shelf", back_populates="book_shelves")
    user = db.relationship("User", back_populates="book_shelves")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return (
            f"BookShelf #{self.id}:"
            + f"Book: {self.book.title}"
            + f"Shelf: {self.shelf.name}"
        )