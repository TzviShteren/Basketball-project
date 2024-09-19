from imp import new_module

from flask_sqlalchemy import SQLAlchemy
from app.models.player import Player
from app.models.player_all_season import PlayerAllSeasons
from app.api import ALL_PLAYERS_DATA
from app.utils.statistics import *

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
                games=player['games'],
                two_percent=player['twoPercent'],
                three_percent=player['fieldPercent'],
                ATR=ATR,
                PPG_ratio=PPG_ratio,
                season=player['season'],
            )
            db.session.add(new_module)
        db.session.commit()
    except Exception as e:
        print(e)

    print("Seed data inserted.")
