from . import Amodels
from app import app, db
from flask import session, render_template, request, redirect, url_for
@app.route('/create_match', methods = ["GET", "POST"])
def create_match():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        if request.method == "GET":
            list_user_tuples = Amodels.User.query.with_entities(Amodels.User.username).all()
            list_user = [user[0] for user in list_user_tuples]

            list_user_id_tuples = Amodels.User.query.with_entities(Amodels.User.id).all()
            list_user_id = [user_id[0] for user_id in list_user_id_tuples]

            list_games_tuples = Amodels.Games.query.with_entities(Amodels.Games.game_name).all()
            list_games = [game_name[0] for game_name in list_games_tuples]

            list_game_id_tuples = Amodels.Games.query.with_entities(Amodels.Games.id).all()
            list_game_id = [game_id[0] for game_id in list_game_id_tuples]

            all_user_id = []
            for i in range(len(list_user_id)):
                all_user_id.append(list_user_id[i])
                all_user_id.append(list_user[i])

            return render_template('create_match.html', list_user_id=list_user_id,
                                   list_user=list_user, list_game=list_games, list_game_id=list_game_id, zip=zip)
        else:
            game_id = request.form.get('game_name')
            winner_id = request.form.get('winner')
            winner_score = request.form.get('winner_score')

            players_ids_str = request.form.getlist('players')
            players_scores_str = request.form.getlist('scores')

            if players_scores_str[-1] == "":
                players_scores_str.pop(-1)

            players_scores = [int(winner_score)]
            players_ids = [int(winner_id)]

            if players_scores_str:
                for i in players_scores_str:
                    players_scores.append(int(i))

            if players_ids_str:
                for i in players_ids_str:
                    players_ids.append(int(i))

            print(f'game_id = {game_id}\n'
                  f'players_scores = {players_scores}\n'
                  f'players_ids = {players_ids}\n')

            new_match = Amodels.Match(scores=players_scores)
            db.session.add(new_match)
            db.session.flush()

            for i in players_ids:
                if i == players_ids[0]:
                    db.session.add(Amodels.User_match(user_id=i, match_id=new_match.id, winner_t_f=True))
                else:
                    db.session.add(Amodels.User_match(user_id=i, match_id=new_match.id, winner_t_f=False))

            db.session.add(Amodels.Game_match(games_id=game_id, match_id=new_match.id))
            db.session.commit()


            return redirect(url_for('index'))