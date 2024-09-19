from flask import Flask, jsonify
from app.db import db
from flask_migrate import Migrate
from app.utils.calculations_and_more import read_json_file
from app.seed import seed_data
from app.api import get_all_players_information_from_api
import os
import json

ALL_PLAYERS_DATA = read_json_file()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# init the database - extra option
with app.app_context():
    db.create_all()
    seed_data(ALL_PLAYERS_DATA)


migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello World!'


# app.register_blueprint(users_bp)
# app.register_blueprint(todos_bp)

def check_and_create_json_file():
    # Check if the JSON file already exists
    JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), 'app/json_file/data.json')
    if not os.path.exists(JSON_FILE_PATH):
        # Sample data to write into the new json file
        data = jsonify(get_all_players_information_from_api())
        # Write the sample data to a new json file
        with open(JSON_FILE_PATH, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print("JSON file created successfully.")

if __name__ == '__main__':
    check_and_create_json_file()
    app.run(debug=True)