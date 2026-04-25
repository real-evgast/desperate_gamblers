from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

# создание экземпляра приложения
app = Flask(__name__)

# Load config based on FLASK_ENV
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('app.config.ProductionConfig')
else:
    app.config.from_object('app.config.DevelopementConfig')

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=31)

# инициализирует расширения
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import profile, logout, create_match, register, index, login, delete_match
