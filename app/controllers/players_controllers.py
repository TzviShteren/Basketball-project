from urllib import request
from flask import Blueprint, request, jsonify
#from ..services.teams_srvice import create_todo as insert_todo

players_bp = Blueprint('players', __name__, url_prefix='/players')


@players_bp.route('/position=<position>/season=<season>', methods=['GET'])
def players_by_position(position, season=None):
    if season:
        return jsonify({"message": f"Fetching players for position: {position} and season: {season}"})
    else:
        return jsonify({"message": f"Fetching players for position: {position} in all seasons"})
