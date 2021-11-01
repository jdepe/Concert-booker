from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = Event.query.all()  
    return render_template('index.html', events=events)

@mainbp.route('/my_events')
def myevents():
    events = Event.query.all()  
    return render_template('myevents.html', events=events)

@mainbp.route('/search')
def search():
    if request.args['search'] is not "":
        queryString = f"%{request.args['search']}%"
        events = Event.query.filter(Event.description.like(queryString)).all()
        return render_template('index.html', events=events)
    # if nothing has been searched
    return redirect(url_for('main.index'))
