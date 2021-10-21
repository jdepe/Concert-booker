from . import db
from datetime import datetime

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	# password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')

class Event(db.Model):
    __tablename__='event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    price = db.Column(db.String(3))
    # add the rest of the data attributes here

    # ... Create the Comments db.relationship
	# relation to call event.comments and comment.event
    comments = db.relationship('Comment', backref='event')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __repr__(self):
       return "<Comment: {}>".format(self.text)

class Booking(db.Model):
    __tablename__='booking'
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    # add the foriegn keys
    price = db.Column(db.String(3), db.ForeignKey('event.price'))


