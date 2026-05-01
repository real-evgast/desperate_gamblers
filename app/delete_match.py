import sqlalchemy
from . import Amodels
from app import app, db
from flask import session, request, redirect, url_for, render_template

from .Amodels import User


@app.route('/delete_match')
def delete_match():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        user = Amodels.User.query.get(session['user_id'])
        if user.editing == True:
            current_match = Amodels.Match.query.filter_by(id=request.cookies.get('match_id_for_delete')).first()
            running = True
            while running:
                current_user_match = Amodels.User_match.query.filter_by(match_id=current_match.id).first()
                try:
                    db.session.delete(current_user_match)
                except sqlalchemy.orm.exc.UnmappedInstanceError:
                    running = False
                else:
                    db.session.commit()

            db.session.delete(Amodels.Game_match.query.filter_by(match_id=current_match.id).first())
            db.session.delete(current_match)
            db.session.commit()

            return redirect(url_for('index'))

        else:
            notification = "Какой не угомонный :)"
            return render_template('notification.html', notification=notification)
