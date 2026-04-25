from app import db
from sqlalchemy.dialects.postgresql import ARRAY
# TODO сделать так что бы у пользователя могло не быть пароля и при первой авторизации запрашивало пароль
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=True)
    editing = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(250), nullable=False)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(100), nullable=True)
    result = db.Column(db.String(50), nullable=True)
    date = db.Column(db.Date, default=db.func.now())
    player_list = db.Column(db.String(100), nullable=True)
    scores = db.Column(ARRAY(db.Integer), nullable=True)

class User_match(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)
    winner_t_f = db.Column(db.Boolean, default=False)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer, nullable=False)

class Game_match(db.Model):
    games_id = db.Column(db.Integer, db.ForeignKey('games.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)