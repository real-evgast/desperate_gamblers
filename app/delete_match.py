import sqlalchemy
from . import Amodels
from app import app, db
from flask import session, request, redirect, url_for

@app.route('/delete_match')
def delete_match():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
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
