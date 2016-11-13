"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, send_file
from FlaskWebProject1 import app
from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired
from testPlot import plot
from StringIO import StringIO


class SearchForm(Form):
    keyword = StringField('Search for a keyword:', validators=[DataRequired()])
    #date1 = DateField('Type in a starting date YYYY-MM-DD', validators=[DataRequired(), ])
    #date2 = DateField('Type in an ending date YYYY-MM-DD', validators=[DataRequired()])
    source = StringField('Search for a source', validators=[DataRequired()])

    submit = SubmitField('Submit')

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/search', methods=['GET', 'POST'])
def search():
    """Renders the search page."""
    form = SearchForm()
    if form.validate_on_submit():
        session['keyword'] = form.keyword.data
        session['plot'] = True
        return redirect(url_for('search'))
    return render_template('search.html', form = form, keyword = session.get('keyword'), plot = session.get('plot'))
@app.route('/fig')
def fig(source = 'cnn.com', count = 10):
    fig = plot(session.get('keyword'), source, count)
    img = StringIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
