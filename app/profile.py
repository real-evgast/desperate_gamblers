from app import app
from flask import redirect, url_for, session, render_template
from . import Amodels
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        current_user_id = session['user_id']

        user = Amodels.User.query.get(current_user_id)

        return render_template('profile.html', user=user)