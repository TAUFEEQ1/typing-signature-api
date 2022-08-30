from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(300), unique=True, nullable=False)
    petname = db.Column(db.String(300), unique=True, nullable=False)
    signature = db.Column(db.String(20),nullable=False)