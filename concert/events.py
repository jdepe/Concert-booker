from flask import Blueprint, render_template
from .models import Event, Comment

bp = Blueprint('event', __name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    event = get_event()
    return render_template('events/event_details.html', event=event)

@bp.route('/create')
def create():
    return render_template('events/event_create.html')

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