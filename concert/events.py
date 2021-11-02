from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Comment
from .forms import EventForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    event = Event.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()
    # The template to be rendered
    return render_template('events/event_details.html', event=event, form=cform)

@bp.route('/create', methods =['GET', 'POST'])
@login_required
def create():
    form = EventForm()
    if form.validate_on_submit():
        creator = current_user.id 
        # Call the function that checks and returns image
        db_file_path=check_upload_file(form)
        event = Event(name=form.name.data, 
                    description=form.description.data, 
                    price=form.price.data, 
                    date=form.date.data, 
                    time=form.time.data, 
                    location=form.location.data,
                    num_tickets=form.num_tickets.data,
                    genre=form.genre.data,
                    status=form.status.data,
                    image=db_file_path,
                    creator_id = creator)
                
        # Add the object to the database session
        db.session.add(event)
        # Commit to the database
        db.session.commit()
        flash(f'Successfully created new event!', 'success')
        # Always redirect if the form is valid
        return redirect(url_for('main.index'))
    return render_template('events/event_create.html', form=form)


@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    event_to_edit = Event.query.get(id)
    form = EventForm()

    if form.validate_on_submit():
        creator = current_user.id 
        # Call the function that checks and returns image
        db_file_path=check_upload_file(form)
        event_to_edit.name=form.name.data
        db.session.commit() 
        event_to_edit.description=form.description.data
        db.session.commit() 
        event_to_edit.price=form.price.data
        db.session.commit()
        event_to_edit.date=form.date.data
        db.session.commit() 
        event_to_edit.time=form.time.data
        db.session.commit() 
        event_to_edit.location=form.location.data
        db.session.commit()
        event_to_edit.num_tickets=form.num_tickets.data
        db.session.commit()
        event_to_edit.genre=form.genre.data
        db.session.commit()
        event_to_edit.status=form.status.data
        db.session.commit()
        event_to_edit.image=db_file_path
        db.session.commit()
        
        flash(f'Successfully edited {event_to_edit.name}!', 'success')
        # Always redirect if the form is valid
        return redirect(url_for('main.myevents'))

    form.name.data = event_to_edit.name
    form.description.data = event_to_edit.description
    form.price.data = event_to_edit.price
    form.date.data = event_to_edit.date
    form.time.data = event_to_edit.time
    form.location.data = event_to_edit.location
    form.num_tickets.data = event_to_edit.num_tickets
    form.genre.data = event_to_edit.genre
    form.status.data = event_to_edit.status
    form.image.data = event_to_edit.image

    return render_template('events/event_edit.html', form=form)

@bp.route('/delete/<id>')
def delete(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    flash(f'Successfully deleted!', 'success')
    return redirect(url_for('main.myevents'))


def check_upload_file(form):
    # Get file data from the form  
    fp=form.image.data
    filename=fp.filename
    # Get the current path of the module file… store image file relative to this path  
    BASE_PATH=os.path.dirname(__file__)
    # Upload file location – directory of this file/static/image
    upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
    # Store relative path in DB as image location in HTML is relative
    db_upload_path='/static/image/' + secure_filename(filename)
    # Save the file and return the db upload path  
    fp.save(upload_path)
    return db_upload_path


@bp.route('/<event>/comment', methods = ['GET', 'POST'])  
def comment(event):  
    form = CommentForm()  
    #get the destination object associated to the page and the comment
    event_obj = Event.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,  
                        event=event_obj,
                        user=current_user) 
      #here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      flash('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('events.show', id=event))



