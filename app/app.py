from flask import Flask
from app.db import db
from flask_migrate import Migrate
from api import get_all_players_information_from_api as data_from_api
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# init the database - extra option
with app.app_context():
    db.create_all()
    db.seed_data(data_from_api)


migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello World!'


# app.register_blueprint(users_bp)
# app.register_blueprint(todos_bp)

if __name__ == '__main__':
    app.run(debug=True)