from imp import new_module
from flask_sqlalchemy import SQLAlchemy
from app.models.player import Player
from app.models.player_all_season import PlayerAllSeasons
from app.api import ALL_PLAYERS_DATA
from app.utils.statistics import *
from app.utils.calculations_and_more import list_of_names, filter_by_name

db = SQLAlchemy()
AVERAGE_SHOOTING = average_shooting(ALL_PLAYERS_DATA)


def seed_data(ALL_PLAYERS_DATA):
    try:
        for player in ALL_PLAYERS_DATA:
            ATR = ratio_of_assists_to_turnovers(player["assistPercent"], player["turnoverPercent"])
            PPG_ratio = PPG_Ratio_of_player(player, ALL_PLAYERS_DATA)
            new_module = Player(
                player_name=player['player_name'],
                team=player['team'],
                position=player['position'],
                points=player['points'],
                games=player['games'],
                two_percent=player['twoPercent'],
                three_percent=player['fieldPercent'],
                ATR=ATR,
                PPG_ratio=PPG_ratio,
                season=player['season'],
            )
            db.session.add(new_module)
        db.session.commit()


        for player_name in filter_by_name(ALL_PLAYERS_DATA):
            statistics_dict = data_connection_all_seasons(ALL_PLAYERS_DATA, player_name)
            seasons_play_str = seasons_player(ALL_PLAYERS_DATA, player_name["player_name"])
            new_module = PlayerAllSeasons(
                player_name=player_name["player_name"],
                team=player_name["team"],
                position=player_name["position"],
                points=statistics_dict["points"],
                games=statistics_dict["games"],
                two_percent=statistics_dict["twoPercent"],
                three_percent=statistics_dict["fieldPercent"],
                ATR=statistics_dict["ATR"],
                PPG_ratio=statistics_dict["PPG_ratio"],
                season=seasons_play_str,
            )
    except Exception as e:
        print(e)


    print("Seed data inserted.")
