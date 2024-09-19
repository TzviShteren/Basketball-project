from ..db import db


class FantasyTeams(db.Model):
    __tablename__ = 'fantasy-teams'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    games = db.Column(db.Integer(80), nullable=False)
    twoPercent = db.Column(db.String(80), nullable=False)
    threePercent = db.Column(db.String(80), nullable=False)
    ATR = db.Column(db.String(80), nullable=False)
    PPG_Ratio = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
