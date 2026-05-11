from app import app
from flask import redirect, url_for, session, render_template, request, make_response
from . import Amodels
from .Amodels import User


@app.route('/', methods=["GET", "POST"])
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        user = Amodels.User.query.get(session['user_id'])

        if user.editing:
            if request.method == "GET":
                parties_data = Amodels.Match.query.all()
                parties_data.reverse()
                res = make_response(render_template('index.html', parties=parties_data, user=user))
                res.set_cookie('match_id_for_editing', max_age=0)
                res.set_cookie('match_id_for_delete', max_age=0)
                return res

            else:
                type = int(request.form.get('type'))
                match_id = request.form.get('match_id')
                if type == 2:
                    res = make_response(redirect(url_for('create_match')))
                    res.set_cookie('match_id_for_editing', str(match_id))
                    return res
                else:
                    res = make_response(redirect(url_for('delete_match')))
                    res.set_cookie('match_id_for_delete', str(match_id))
                    return res
        else:
            notification = "Администратор сайта еще не дал вам доступ к сайту. Если вы случайный пользователь, вы его не получите. Если вы мой друг - ждите :)"
            return render_template('notification.html', notification=notification)
