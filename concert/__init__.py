from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.exceptions import InternalServerError


# create a SQLalchemy database object as global variable db
db = SQLAlchemy()

# Create custom error pages
# Page not found
def page_not_found(e):
    return render_template('404.html'), 404
# Internal server error
def internal_server_error(e):
    return render_template('500.html'), 500
# Resource permanently deleted
def page_gone(e):
    return render_template('410.html'), 410

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

    # Add the error handlers
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(410, page_gone)

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)
    from . import auth
    app.register_blueprint(auth.bp)
    return app
