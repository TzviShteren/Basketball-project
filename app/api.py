import json
import requests
from app.utils.calculations_and_more import list_of_season


def get_all_players_information_from_api():
    result = []

    API_URL = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season="
    for season in list_of_season:
        result += requests.get(f"{API_URL}{season}").json()
    return result



