from app.models.player import Player
from app.models.player_all_season import PlayerAllSeasons
from app.utils.statistics import *
from app.utils.calculations_and_more import filter_by_name
from app.db import db


def seed_data(all_data):
    try:
        for player in all_data:
            ATR = ratio_of_assists_to_turnovers(player["assists"], player["turnovers"])
            PPG_ratio = PPG_Ratio_of_player(player, all_data)
            new_module_player = Player(
                player_name=player['playerName'],
                team=player['team'],
                position=player['position'],
                points=player['points'],
                games=player['games'],
                two_percent=player['twoPercent'],
                three_percent=player['threePercent'],
                ATR=ATR,
                PPG_ratio=PPG_ratio,
                season=player['season'],
            )
            db.session.add(new_module_player)
        db.session.commit()

        for player_name in filter_by_name(all_data):
            statistics_dict = data_connection_all_seasons(all_data, player_name)
            seasons_play_str = seasons_player(all_data, player_name["playerName"])
            new_module_player_all_seasons = PlayerAllSeasons(
                player_name=player_name["playerName"],
                team=player_name["team"],
                position=player_name["position"],
                points=statistics_dict["points"],
                games=statistics_dict["games"],
                two_percent=statistics_dict["twoPercent"],
                three_percent=statistics_dict["threePercent"],
                ATR=statistics_dict["ATR"],
                PPG_ratio=statistics_dict["PPG_ratio"],
                season=seasons_play_str,
            )
            db.session.add(new_module_player_all_seasons)
        db.session.commit()
    except Exception as e:
        print(e)

    print("Seed data inserted.")
