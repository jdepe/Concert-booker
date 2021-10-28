from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# create a SQLalchemy database object as global variable db
db = SQLAlchemy()

def create_app():
    app=Flask(__name__)

    bootstrap = Bootstrap(app)
 
    # create a secret key for the sesion object
    app.secret_key = 'secretkey'

    # configure and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///concertdb.sqlite'
    db.init_app(app)

    #initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    from .models import User  
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)
    from . import user_history
    app.register_blueprint(user_history.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    return app
