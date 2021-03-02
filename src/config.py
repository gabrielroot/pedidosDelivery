from decouple import config
import logging


class Config:
    LOG_LEVEL = config('LOG_LEVEL', default='INFO')
    TIMEZONE = config('TIMEZONE', default='America/Sao_Paulo')
    
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s][%(levelname)s] %(name)s '
                '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': LOG_LEVEL,
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout'
            },
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': LOG_LEVEL,
                'propagate': False
            },
        }
    }


class Development(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_ECHO = True


class Testing(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memmory:'


class Staging(Config):
    pass


class Production(Config):
    pass
