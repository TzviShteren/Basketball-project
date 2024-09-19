from flask import Flask
from app.db import db
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# init the database - extra option
with app.app_context():
    db.create_all()


migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello World!'


# app.register_blueprint(users_bp)
# app.register_blueprint(todos_bp)

if __name__ == '__main__':
    app.run(debug=True)