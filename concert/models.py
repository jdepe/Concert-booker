from sqlalchemy.orm import backref
from . import db
from datetime import datetime, date, time
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	
    # Create the password_hash so that passwords aren't stored directly in the DB.
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')


class Event(db.Model):
    __tablename__='event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), )
    description = db.Column(db.String(500))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    location = db.Column(db.String(400))
    image = db.Column(db.String(400))
    price = db.Column(db.Integer)
    num_tickets = db.Column(db.Integer)
    genre = db.Column(db.String(80))
    status = db.Column(db.String(80))

    # Create the Comment db.relationship
	# relation to call event.comment and comment.event
    comments = db.relationship('Comment', backref='event')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    
    # add the foreign keys for user.id and event.id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __repr__(self):
       return "<Comment: {}>".format(self.text)


class Booking(db.Model):
    __tablename__='booking'
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    price = db.Column(db.Integer)


   

    