import json
# 'C', 'SG-PG-SF', 'SF-SG', 'PG-SG', 'PF-C', 'SF-PF', 'SG-PG', 'PF-SF', 'C-PF', 'PG', 'PF', 'SG-SF', 'SF', 'SG'
list_of_position = ["PG", "SG", "SF", "PF", "C"]
list_of_season = [2022, 2023, 2024]


def filter_by_season(data, season: int):
    return list(filter(lambda d: d["season"] == season, data))


def filter_by_position(data, position: str):
    return list(filter(lambda d: position in d["position"].split("-"), data))


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


def read_json_file():
    try:
        with open("app/json_file/data.json", 'r') as json_file:
            data = json.load(json_file)
            return data
    except json.JSONDecodeError as e:
        print(f"Error reading the JSON file: {e}")
        return None
