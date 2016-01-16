# all the imports
from enum import Enum
import sqlite3
from SynonymInterface import SynonymInterface
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


# configuration
DATABASE = '/tmp/thesaurus.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# creates app
app = Flask(__name__)
app.config.from_object(__name__)

# connects to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# creating global variables
synonym_graph = None


# routes
@app.route('/')
def index():
    """
    Renders index page
    """
    return render_template('index.html')


@app.route('/det_pos', methods=['POST'])
def determine_pos():
    # initializes synonym graph
    synonym_graph = SynonymInterface("VERB")
    return synonym_graph


@app.route('/det_simword', methods=['POST'])
def determine_similar_word():
    return redirect(url_for('determine_similar_word'))


@app.route('/<string:page_name>/')
def static_page(page_name):
    """
    Renders static pages
    """
    return render_template('%s.html' % page_name)

# runs app
if __name__ == '__main__':
    app.run()