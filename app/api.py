import json
import requests
from app.utils.calculations_and_more import list_of_season
API_URL = "https://nba-stats-db.herokuapp.com/api/"
def get_all_players_information_from_api():
    result = []
    for season in list_of_season:
        result += requests.get(API_URL + f"playerdata/season/{season}").json()["results"]
    return result
def filtering_for_relevant_information(data):




