from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dbin import db  

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from main import main as main_blueprint
app.register_blueprint(main_blueprint)

from sorcers import sorcers as sorcers_blueprint
app.register_blueprint(sorcers_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
