from myapp import app
from flask import render_template
from myapp.utils import make_map

@app.route('/')
@app.route('/index')
def index():
    make_map()
    return render_template('index.html', title = 'Nepal visualization', text = 'Nepal map')
