from app import *
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        current_user_id = session['user_id']

        user = User.User.query.get(current_user_id)

        return render_template('profile.html', user=user)