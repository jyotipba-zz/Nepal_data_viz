from myapp import app
from flask import render_template,url_for
from bokeh.embed import server_document


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title = 'Nepal visualization')


@app.route('/visualization')
def visual():

	script = server_document(url='http://localhost:5006/run')
	#print(script)
	return render_template('visual.html', script=script)

@app.route('/about')
def about():
    return render_template('about.html', title = 'Nepal visualization')
