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
            return f"Пользователь {username} успешно зарегистрирован!"
        except Exception:
            db.session.rollback()
            return f"Ошибка при регистрации: логин уже занят."
    else:
        if 'user_id' not in session:
            return render_template('register.html')
        else:
            return redirect(url_for('index'))