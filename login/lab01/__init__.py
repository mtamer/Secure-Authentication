#imports
import os

from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask_mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

#configuration setup
# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(os.environ['APP_SETTINGS'])

#extensions
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
db = SQLAlchemy(app)

#blueprints
from lab01.main.views import main_blueprint
from lab01.user.views import user_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(user_blueprint)

#flask-login
from models import User

login_manager.login_view = "user.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
