from flask import Flask

def create_app():
    app=Flask(__name__)
    
    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)
    from . import user_history
    app.register_blueprint(user_history.bp)

    return app
