from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Booking

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = Event.query.all()  
    return render_template('index.html', events=events)

@mainbp.route('/my_events')
def myevents():
    events = Event.query.all()  
    return render_template('myevents.html', events=events)

@mainbp.route('/rock')
def rock():
    events = Event.query.filter_by(genre='rock').all()  
    if events == []:
        flash(f'No events of that genre exist', 'warning')
        return redirect(url_for('main.index')) 
    return render_template('rock.html', events=events)

@mainbp.route('/pop')
def pop():
    events = Event.query.filter_by(genre='pop').all()  
    if events == []:
        flash(f'No events of that genre exist', 'warning')
        return redirect(url_for('main.index')) 
    return render_template('pop.html', events=events)

@mainbp.route('/electronic')
def electronic():
    events = Event.query.filter_by(genre='electronic').all()  
    if events == []:
        flash(f'No events of that genre exist', 'warning')
        return redirect(url_for('main.index')) 
    return render_template('electronic.html', events=events)

@mainbp.route('/hiphop')
def hiphop():
    events = Event.query.filter_by(genre='hip hop').all()  
    if events == []:
        flash(f'No events of that genre exist', 'warning')
        return redirect(url_for('main.index')) 
    return render_template('hiphop.html', events=events)
    
@mainbp.route('/my_bookings')
def mybookings():
    events = Event.query.all() 
    bookings = Booking.query.all() 
    print(bookings)
    print(events)
    return render_template('mybookings.html', events=events, booking=bookings)

@mainbp.route('/search')
def search():
    if request.args['search'] is not "":
        queryString = f"%{request.args['search']}%"
        events = Event.query.filter(Event.description.like(queryString)).all()
        return render_template('index.html', events=events)
    # if nothing has been searched
    return redirect(url_for('main.index'))

