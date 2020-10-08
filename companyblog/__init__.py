from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)

###########################
###### DATABASE SETUP #####
###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEM_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)
######################
# LOGIN CONFIGS #####
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'






#######################################
from companyblog.core.views import core
from companyblog.users.views import users
from companyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)
