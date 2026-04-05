from app import app
from flask import redirect, url_for, session, render_template
from . import Amodels
@app.route('/', methods = ["GET"])
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        user = Amodels.User.query.get(session['user_id'])

        if user.editing:
            """
            parties_data = [
                {
                    'game_name': 'Poker',
                    'date': '2024-01-15',
                    'player': 'player1',
                    'result': '+500$'
                },
                {
                    'game_name': 'Blackjack',
                    'date': '2024-01-14',
                    'player': 'player2',
                    'result': '-100$'
                },
                {
                    'game_name': 'Chess',
                    'date': '2024-01-13',
                    'player': 'player1',
                    'result': '1 место'
                },
                {
                    'game_name': 'Chess',
                    'date': '2024-01-13',
                    'player': 'player1',
                    'result': '1 место'
                }
            ]
            """
            parties_data = Amodels.Match.query.all()
            return render_template('index.html', parties=parties_data)
        else:
            notification = "Администратор сайта ещё не дал вам доступ к сайту, если вы случайный пользователь то вы его никогда и не получите. А если мой друг - то ждите :)"
            return render_template('notification.html', notification=notification)