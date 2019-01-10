from flask import Flask
from instance.config import app_config
from .api.v1.views import meetup_views, question_views

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config)
    
    app.register_blueprint(meetup_views.meetupv1)
    # app.register_blueprint(user_views.user_v1)
    app.register_blueprint(question_views.questionsv1)

    return app