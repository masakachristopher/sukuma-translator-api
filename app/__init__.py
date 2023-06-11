from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.config.Config')
    
    @app.route('/')
    def landing():
        return 'Local tribe language translation app'

    # Register blueprints
    from src.routes.translation_route import translation_bp
    app.register_blueprint(translation_bp)

    return app
