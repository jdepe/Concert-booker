from flask import Blueprint, render_template, url_for

bp = Blueprint('user_history', __name__, url_prefix='/user_history')

@bp.route('/')
def show():
    return render_template('user_history.html')