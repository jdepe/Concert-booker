from flask import Blueprint, render_template, url_for

bp = Blueprint('event', __name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    return render_template('events/event_details.html')

@bp.route('/create')
def create():
    return render_template('events/event_create.html')