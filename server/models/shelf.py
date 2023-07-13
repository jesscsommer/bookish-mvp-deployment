from models import db, association_proxy

class Shelf(db.Model):
    __tablename__ = "shelves"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="shelves")

    book_shelves = db.relationship("BookShelf", back_populates="shelf")
    books = association_proxy("book_shelves", "book")

    def __repr__(self):
        return (
            f"Shelf #{self.id}: {self.name}"
        )