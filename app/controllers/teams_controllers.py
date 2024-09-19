from urllib import request
from flask import Blueprint, request, jsonify

# from ..services.teams_srvice import create_todo as insert_todo

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')


@teams_bp.route('/', methods=['POST'])
def create_team():
    pass


@teams_bp.route('<team_id>', methods=['PUT'])
def update_team(team_id):
    pass


@teams_bp.route('<team_id>', methods=['DELETE'])
def delete_team(team_id):
    pass


@teams_bp.route('compare', methods=['GET'])
def get_team_details(team_id):
    # aaa = request.args.to_dict()
    # team1ewsifrhy = request.args.get('team1')
    pass
