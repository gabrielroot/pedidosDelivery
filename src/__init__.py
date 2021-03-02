import os
import logging.config

from flask import Flask, jsonify
from decouple import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(environment=config('APPLICATION_ENV', default='Development')):
    app = Flask(__name__)

    config_name = f'src.config.{environment}'
    app.config.from_object(config_name)

    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join(BASE_DIR, 'migrations'))
    ma.init_app(app)

    logging.config.dictConfig(app.config['LOGGING'])
    logger.info(f'loading application with configuration {config_name}')

    register_blueprints(app)
    register_handlers(app)

    return app


def register_blueprints(app):
    from src.url import v1

    app.register_blueprint(v1)


def register_handlers(app):

    @app.errorhandler(422)
    def handle_validation_error(error):
        return jsonify({'errors': error.data['messages']}), 400

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({'message': error.description}), 404

    @app.errorhandler(500)
    def handle_internal_error(error):
        logger.error(error)
        return jsonify({'message': 'internal server error, please contact suport team'}), 500
