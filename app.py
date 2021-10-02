from flask import Flask

from extensions import db
from config import app_config


def create_app(config_name):
    app = Flask('fast')
    app.config.from_object(app_config.get(config_name, 'development'))

    init_extensions(app)
    init_blueprints(app)

    return app


def init_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def init_blueprints(app):
    from fastlyc.v1 import blueprint
    app.register_blueprint(blueprint, url_prefix='/api/v1')


if __name__ == "__main__":
    app = create_app('development')
    app.run(host="0.0.0.0", port=5000)
