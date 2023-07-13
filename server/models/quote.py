from models import db

class Quote(db.Model):
    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    book = db.relationship("Book", back_populates="quotes")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return (
            f"Quote #{self.id}:"
            + f"Content: {self.content}"
        )