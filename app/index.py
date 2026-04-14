from app import app
from flask import redirect, url_for, session, render_template
from . import Amodels
# TODO удаление матчей или редактирование
@app.route('/', methods = ["GET"])
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        user = Amodels.User.query.get(session['user_id'])

        if user.editing:
            parties_data = Amodels.Match.query.all()
            return render_template('index.html', parties=parties_data)
        else:
            notification = "Администратор сайта ещё не дал вам доступ к сайту, если вы случайный пользователь то вы его никогда и не получите. А если мой друг - то ждите :)"
            return render_template('notification.html', notification=notification)