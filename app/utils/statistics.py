from app.utils.calculations_and_more import *
import statistics


# from app.models.player_all_season import PlayerAllSeasons


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


def data_connection_all_seasons(data, player_name):
    list_of_season_player = filter_by_name(data, player_name)
    relevant_information = {"points": 0, "games": 0, "two_percent": 0, "three_percent": 0, "ATR": 0, "PPG_ratio": 0}
    for season_player in list_of_season_player:
        ATR = ratio_of_assists_to_turnovers(season_player["assistPercent"], season_player["turnoverPercent"])
        PPG_ratio = PPG_Ratio_of_player(season_player, data)
        relevant_information["games"] += season_player["games"],
        relevant_information["two_percent"] += season_player["two_percent"],
        relevant_information["three_percent"] += season_player["three_percent"],
        relevant_information["points"] += season_player["points"],
        relevant_information["ATR"] += ATR,
        relevant_information["PPG_ratio"] += PPG_ratio
    the_len_of_list_of_season_player = len(list_of_season_player)
    relevant_information["two_percent"] /= the_len_of_list_of_season_player
    relevant_information["three_percent"] /= the_len_of_list_of_season_player
    relevant_information["ATR"] /= the_len_of_list_of_season_player
    relevant_information["PPG_ratio"] /= the_len_of_list_of_season_player


def PPG_Ratio_of_player(player, data):
    dict_of_average = average_shooting(data)
    points_per_game = player[""] / player["games"]
    str_of_key = f"{player['season']}-{player['position']}"
    if str_of_key in dict_of_average:
        return points_per_game / dict_of_average[str_of_key]
    return 0
