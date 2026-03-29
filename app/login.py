from app import app
from flask import render_template, redirect, request, session, url_for
from werkzeug.security import check_password_hash
from . import Amodels
@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get('username')
        password = request.form.get('password')

        user = Amodels.User.query.filter_by(username=login).first()

        if user and check_password_hash(user.password, password):

            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return "Неверный логин или пароль"
    else:
        if 'user_id' not in session:
            return render_template('login.html')
        else:
            return redirect(url_for('index'))