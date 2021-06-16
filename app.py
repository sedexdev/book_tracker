import os
from flask import Flask
from extensions import db


def import_blueprints():
    global core_blueprint

    from core.views import core_blueprint


def register_extensions(app):
    db.init_app(app)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    import_blueprints()
    register_extensions(app)

    app.register_blueprint(core_blueprint)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app, db


config = os.environ['APP_SETTINGS']
app, database = create_app(config)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
