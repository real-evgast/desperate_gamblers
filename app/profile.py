from app import app, db
from flask import redirect, url_for, session, render_template, request
from . import Amodels
from .Amodels import User


# TODO сделать редактирование профиля: видимое Имя (не логин), удаление профиля, сколько выйграл игр -- где участвовал
@app.route('/profile', methods = ["GET", "POST"])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        current_user_id = session['user_id']
        user = Amodels.User.query.get(current_user_id)

        if request.method == "GET":
            return render_template('profile.html', user=user)
        else:
            description = request.form.get('description')
            user.description = description
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('profile'))
