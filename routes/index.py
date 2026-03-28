from app import *
@app.route('/', methods = ["GET"])
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        current_user_id = session['user_id']

        user = User.User.query.get(current_user_id)

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
            parties_data = Match.Match.query.all()
            return render_template('index.html', parties=parties_data)
        else:
            return "Администратор сайта ещё не дал вам доступ к сайту, если вы случайный пользователь то вы его никогда и не получите. А если мой друг, то ждите :)"