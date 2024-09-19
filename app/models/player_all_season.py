from app.db import db

class PlayerAllSeasons(db.Model):
    __tablename__ = 'player-all-seasons'
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    season = db.Column(db.String(80), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    two_percent = db.Column(db.String(80), nullable=False)
    three_percent = db.Column(db.String(80), nullable=False)
    ATR = db.Column(db.Float, nullable=False)
    PPG_ratio = db.Column(db.Float, nullable=False)

    # def __repr__(self):
    #     return f'<User: name: {self.name}\tID_number{self.ID_number}\tage{self.age}>'
