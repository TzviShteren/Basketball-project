from app.db import db


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    two_percent = db.Column(db.String(80), nullable=False)
    three_percent = db.Column(db.String(80), nullable=False)
    ATR = db.Column(db.Float, nullable=False)
    PPG_ratio = db.Column(db.Float, nullable=False)
    season = db.Column(db.Integer, nullable=False)
