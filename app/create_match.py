import sqlalchemy
from . import Amodels
from app import app, db
from flask import session, render_template, request, redirect, url_for
@app.route('/create_match', methods = ["GET", "POST"])
def create_match():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        this_user = Amodels.User.query.get(session['user_id'])
        if this_user.editing:
            if request.method == "GET":
                list_user_tuples = Amodels.User.query.with_entities(Amodels.User.username).all()
                list_user = [user[0] for user in list_user_tuples]

                list_user_id_tuples = Amodels.User.query.with_entities(Amodels.User.id).all()
                list_user_id = [user_id[0] for user_id in list_user_id_tuples]

                list_games_tuples = Amodels.Games.query.with_entities(Amodels.Games.game_name).all()
                list_games = [game_name[0] for game_name in list_games_tuples]

                list_game_id_tuples = Amodels.Games.query.with_entities(Amodels.Games.id).all()
                list_game_id = [game_id[0] for game_id in list_game_id_tuples]

                list_games_type_tuples = Amodels.Games.query.with_entities(Amodels.Games.id).all()
                list_games_type = [game_type[0] for game_type in list_games_type_tuples]

                all_user_id = []
                for i in range(len(list_user_id)):
                    all_user_id.append(list_user_id[i])
                    all_user_id.append(list_user[i])

                if not request.cookies.get('match_id_for_editing'):
                    return render_template('create_match.html', list_user_id=list_user_id,
                                           list_user=list_user, list_game=list_games, list_game_id=list_game_id,
                                           list_games_type=list_games_type, zip=zip, editing=False)
                else:
                    current_match = Amodels.Match.query.filter_by(id=request.cookies.get('match_id_for_editing')).first()
                    return render_template('create_match.html', list_user_id=list_user_id,
                                           list_user=list_user, list_game=list_games, list_game_id=list_game_id,
                                           list_games_type=list_games_type, zip=zip, editing=True,
                                           current_match=current_match)

            else:
                game_id = int(request.form.get('game_name'))
                players_ids_str = request.form.getlist('players')
                players_scores_str = request.form.getlist('scores')
                winner_flags_str = request.form.getlist('winner_flags')

                players_ids = []
                if players_ids_str:
                    for i in players_ids_str:
                        players_ids.append(int(i))

                players_scores = []
                if players_scores_str[0] != '':
                    for i in players_scores_str:
                        players_scores.append(int(i))

                winner_flags = []
                if winner_flags_str:
                    for i in winner_flags_str:
                        if i == 'true':
                            winner_flags.append(True)
                        else:
                            winner_flags.append(False)

                print(f'game_id = {game_id}\n'
                      f'winner_flags  = {winner_flags}\n'
                      f'player_ids = {players_ids}\n'
                      f'players_scores = {players_scores}\n')

                if not request.cookies.get('match_id_for_editing'):

                    new_match = Amodels.Match(scores=players_scores)
                    db.session.add(new_match)
                    db.session.flush()

                    for i in range(len(players_ids)):
                        db.session.add(Amodels.User_match(match_id=new_match.id, user_id=players_ids[i-1], winner_t_f=winner_flags[i-1]))

                    db.session.add(Amodels.Game_match(match_id=new_match.id, games_id=game_id))
                    db.session.commit()
                    return redirect(url_for('index'))

                else:
                    current_match = Amodels.Match.query.filter_by(id=request.cookies.get('match_id_for_editing')).first()
                    current_match.scores = players_scores
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
                    db.session.commit()

                    for i in range(len(players_ids)):
                        db.session.add(Amodels.User_match(match_id=current_match.id, user_id=players_ids[i-1], winner_t_f=winner_flags[i-1]))
                    db.session.add(Amodels.Game_match(match_id=current_match.id, games_id=game_id))
                    db.session.add(current_match)
                    db.session.commit()
                    return redirect(url_for('index'))
        else:
            notification = "Администратор сайта ещё не дал вам доступ к сайту, если вы случайный пользователь то вы его никогда и не получите. А если мой друг - то ждите :)"
            return render_template('notification.html', notification=notification)
