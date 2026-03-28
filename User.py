from app import *
from werkzeug.security import generate_password_hash
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    editing = db.Column(db.Boolean, default=False)
