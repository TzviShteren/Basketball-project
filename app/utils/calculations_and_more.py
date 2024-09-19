from os.path import split

list_of_position = ["PG", "SG", "SF", "PF", "C"]
list_of_season = [2022, 2023, 2024]


def filter_by_season(data, season: int):
    return list(filter(lambda d: d["season"] == season, data))


def filter_by_position(data, position: str):
    return list(filter(lambda d: d["position"] == position, data))


def filter_by_name(data, name: str):
    return list(filter(lambda d: d["playerName"] == name, data))


def list_of_names(data):
    map_names = map(lambda d: d["playerName"], data)
    return list(set(map_names))


#Seasons a player has played
def seasons_player(data, name: str):
    filter_season = filter_by_name(data, name)
    seasons = list(map(lambda d: str(d["season"]), filter_season))
    return ", ".join(seasons)
