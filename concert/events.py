from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event, Comment
from .forms import EventForm, CommentForm
from . import db

bp = Blueprint('event', __name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    event = Event.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()
    # the template to be rendered
    return render_template('events/event_details.html', event=event, form=cform)

@bp.route('/create', methods= ['GET', 'POST'])
def create():
    print('Method type: ', request.method)
    form = EventForm()
    if form.validate_on_submit():
        event = Event(name=form.data, description=form.description.data, image=form.image.data, price=form.price.data)
        # add the object to the database session
        db.session.add(event)
        # commit to the database
        db.session.commit()
        print('Successfully create new event', 'success')
        # always redirect if the form is valid
        return redirect(url_for('event.create'))
    return render_template('events/event_create.html', form=form)

def get_event():
    # create an instance of the Event class to test the new classes.
    bliss_desc = """Bliss 'n' Eso"""
    img_loc = "static\image\featured.jpg"

    event = Event("Bliss n Eso", bliss_desc, img_loc, "120", "2022-1-1", "20:00", "Brisbane", "Hip-Hop", "Available", "$69")

    # Create a comment.
    comment = Comment("Simon", "Aussie hip-hop is the best!", '2021-10-10 12:00')
    event.set_comments(comment)
    comment = Comment("Anon", "Washed up", "2021-11-10 12:00")
    event.set_comments(comment)
    return event