from app import app
from flask import redirect, url_for, session, render_template
from . import Amodels
# TODO сделать редактирование профиля: "описание, видимое Имя (не логин)", возможно добавление фотографий в профиль, удаление профиля, сколько выйграл игр -- где участвовал
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        current_user_id = session['user_id']

        user = Amodels.User.query.get(current_user_id)

        return render_template('profile.html', user=user)