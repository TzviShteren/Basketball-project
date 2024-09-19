from app.db import db


class FantasyTeams(db.Model):
    __tablename__ = 'fantasy-teams'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), nullable=False)
    player_ids = db.Column(db.String(100), nullable=False)

