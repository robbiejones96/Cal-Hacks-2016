"""
The flask application package.
"""

from flask import Flask, session
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
import FlaskWebProject1.views
bootstrap = Bootstrap(app)
