from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from app.routes.api_routes import bp_api as main_bp
        app.register_blueprint(main_bp)

    return app