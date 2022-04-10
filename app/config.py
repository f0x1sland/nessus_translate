import os
from pathlib import Path


class Config:
    VERSION = '0.1.0.0'
    basedir = Path(os.path.abspath(os.path.dirname(__file__))).parent.absolute()

    DB_FILE = 'db.sqlite'
    DEFAULT_LANG = 'en'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_FILE)


class ConfigLogger:
    LOG_FILE = 'nest.log'
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'default_formatter': {
                'format': '[%(asctime)s - %(name)s - %(levelname)s] - %(message)s'
            }
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.FileHandler',
                'formatter': 'default_formatter',
                'filename': LOG_FILE
            }
        },

        'loggers': {
            'nest': {
                'handlers': ['file_handler'],
                'level': 'DEBUG',
                'propagate': True
            }
        }

    }
