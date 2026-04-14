from app import app, db
from flask import render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash
from . import Amodels
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password'); hashed_password = generate_password_hash(password)
        new_user = Amodels.User(username=username, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            notification = "Пользователь {username} успешно зарегистрирован!"
            return render_template('notification.html', notification=notification)
        except Exception:
            db.session.rollback()
            notification = "Ошибка при регистрации: логин уже занят."
            return render_template('notification.html', notification=notification)
    else:
        if 'user_id' not in session:
            return render_template('register.html')
        else:
            return redirect(url_for('index'))