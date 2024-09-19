from app.utils.calculations_and_more import *
import statistics


def ratio_of_assists_to_turnovers(assist: float, turnover: float) -> float:
    return assist / turnover


# Creating a dict of average shooting positions for the season
def average_shooting(data):
    dict_of_average = {}
    for season in list_of_season:
        for position in list_of_position:
            according_to_season = filter_by_season(data, season)
            according_to_position_end_season = filter_by_position(according_to_season, position)

            # mean calculates the arithmetic mean (average) of a list of numbers.
            dict_of_average[f"{season}-{position}"] = statistics.mean(
                list(map(lambda x: x["fieldGoals"] / x["games"], according_to_position_end_season.values())))

    return dict_of_average


# def data_connection_all_seasons(data, player_name, dict_of_average):
#     list_of_season_player = filter_by_name(data, player_name)
#     relevant_information = {"season": 0, "points": 0, "games": 0, "assists": 0, "two_percent": 0, "three_percent": 0, "ATR": 0, "PPG_ratio":0}
#     for season_player in list_of_season_player:





def PPG_Ratio_of_player(player, data):
    dict_of_average = average_shooting(data)
    points_per_game = player["fieldGoals"] / player["games"]
    str_of_key = f"{player['season']}-{player['position']}"
    if str_of_key in dict_of_average:
        return points_per_game / dict_of_average[str_of_key]
    return 0