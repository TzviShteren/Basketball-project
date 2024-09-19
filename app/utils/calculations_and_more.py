list_of_position = ["PG", "SG", "SF", "PF", "C"]
list_of_season = [2022, 2023, 2024]


def filter_by_season(data, season: int):
    return list(filter(lambda d: d["season"] == season, data))


def filter_by_position(data, position: str):
    return list(filter(lambda d: d["position"] == position, data))


def filter_by_name(data, name: str):
    return list(filter(lambda d: d["playerName"] == name, data))
