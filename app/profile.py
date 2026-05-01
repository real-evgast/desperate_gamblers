from app import app, db
from flask import redirect, url_for, session, render_template, request
from . import Amodels
from .Amodels import User


# TODO сделать редактирование профиля: видимое Имя (не логин), удаление профиля, сколько выйграл игр -- где участвовал
@app.route('/profile/<name_user>', methods = ["GET", "POST"])
def profile(name_user):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        user = Amodels.User.query.filter_by(username=name_user).first()
        participated_wins = 0

        matches = Amodels.User_match.query.filter_by(user_id=user.id).all()
        participated = len(matches)

        for match in matches:
            if match.winner_t_f:
                participated_wins +=1

        number_of_matches = len(Amodels.Match.query.all())

        editing_description = False
        if user.id == session['user_id']:
            editing_description = True

        if request.method == "GET":
            return render_template('profile.html', user=user, participated=participated,
                                   participated_wins=participated_wins, number_of_matches=number_of_matches,
                                   editing_description=editing_description)
        else:
            description = request.form.get('description')
            user.description = description
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('profile', name_user=user.username))
