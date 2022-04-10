from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config, ConfigLogger
import logging
import logging.config as logconfig

import logging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import endpoints
from app import models

db.create_all()
db.session.commit()
logconfig.dictConfig(ConfigLogger.LOGGING_CONFIG)
logger = logging.getLogger('nest')
logger.info('App is starting')
