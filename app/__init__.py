from flask import Flask
from instance.config import app_config
# from .api.v1.views import meetup_views, question_views
from .api.v1 import version_one as v1

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config)
    app.register_blueprint(v1)
    
    return app