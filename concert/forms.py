from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField
from wtforms.fields.html5 import DateField, TimeField, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed




# allowed files
ALLOWED_FILES = {'PNG','JPG','png','jpg','JPEG','jpeg'}
choices = [('rock', 'Rock'), ('pop', 'Pop'), ('electronic', 'Electronic'), ('hip hop', 'Hip Hop')]

# The event creation form
class EventForm(FlaskForm):
  name = StringField('Event Name', validators=[InputRequired(), Length(max=80, message="Maximum characters reached (80)")])
  description = TextAreaField('Description', validators=[InputRequired(), Length(max=500, message="Maximum characters reached (500)")])
  price = IntegerField('Price', validators=[InputRequired()])
  date = DateField('Event Date', validators=[InputRequired()], format='%Y-%m-%d')
  time = TimeField('Event Start Time', validators=[InputRequired()], format='%H:%M')
  location = StringField('Event Location', validators=[InputRequired()])
  num_tickets = IntegerField('Total tickets', validators=[InputRequired()])
  genre = SelectField(u'Genre', choices=choices)
  status = SelectField(u'Event Status', choices=[('upcoming', 'Upcoming'), ('inactive', 'Inactive'), ('booked', 'Booked'), ('cancelled', 'Cancelled')])
  image = FileField('Cover Image', validators=[FileRequired(), FileAllowed(ALLOWED_FILES, message=f'Accepted file types: {ALLOWED_FILES}')])
  submit = SubmitField("Create")

# User login
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

# User register
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = EmailField("Email Address", validators=[InputRequired()])
    phone = StringField("Phone Number")
    address = StringField("Street Address")
    # Linking password and confirm fields to ensure the data is equal
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # Submit button
    submit = SubmitField("Register")
    
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')

class BookingForm(FlaskForm):
  qty = IntegerField('How many tickets to purchase', [InputRequired()])
  cost = IntegerField('Ticket Cost',validators=[InputRequired()])
  confirm = SubmitField('Confirm')

