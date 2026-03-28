from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1984@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Импортируем модели, чтобы они были известны SQLAlchemy
import User
import Match
import Games
import Game_match
import User_match

with app.app_context():
    db.create_all()

migrate = Migrate(app, db, render_as_batch=True, compare_type=True)

app.secret_key = "hfjksldjryt6783kmdhfdfgvbnfghddjulpfkikotg654132645kjhfdgghjkfdsdfhkgj645489691065df564sdd65f4sd23ds2wqertyuiosdxcvbnmwedrfghjkpl,oikijnyuhtygvrdf"

@app.route('/test')
def test():
    return render_template('test.html')

from routes import index, login, register, logout, profile, create_match

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
