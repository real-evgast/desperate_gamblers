from app import *
class Game_match(db.Model):
    games_id = db.Column(db.Integer, db.ForeignKey('games.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)
