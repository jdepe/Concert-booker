from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


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

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)

    return app
