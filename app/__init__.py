import datetime
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

is_production = os.environ.get('FLASK_ENV') == 'production' or os.environ.get('VERCEL') == '1'

if is_production:
    app.config.from_object('app.config.ProductionConfig')
else:
    app.config.from_object('app.config.DevelopmentConfig')

if is_production and (not app.config.get('SECRET_KEY') or not app.config.get('SQLALCHEMY_DATABASE_URI')):
    raise RuntimeError('SECRET_KEY and DATABASE_URL must be set in production.')

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=31)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import profile, logout, create_match, register, index, login, delete_match
