from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')

### search function - need the database and a form
#  @mainbp.route('/search')
#  def search():
#      if request.args['search'] is not "":
#          queryString = f"%{request.args['search']}%"
#          destinations = Destination.query.filter(Destination.description.like(queryString)).all()
#      if nothing has been searched
#     return redirect(url_for('main.index'))