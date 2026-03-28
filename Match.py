from sqlalchemy.dialects.postgresql import ARRAY
from app import *

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(100), nullable=True)
    result = db.Column(db.String(50), nullable=True)
    date = db.Column(db.Date, default=db.func.now())
    player_list = db.Column(db.String(100), nullable=True)
    scores = db.Column(ARRAY(db.Integer), nullable=True)
