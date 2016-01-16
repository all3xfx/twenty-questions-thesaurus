# all the imports
import sqlite3
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


# routes
@app.route('/')
def index():
    """
    Renders index page
    """
    return render_template('index.html')


@app.route('/<string:page_name>/')
def static_page(page_name):
    """
    Renders static pages
    """
    return render_template('%s.html' % page_name)


@app.route('/det-pos', methods=['POST'])
def determine_pos():
    return redirect(url_for('determine_similar_word'))


@app.route('/det-simword', methods=['POST'])
def determine_similar_word():
    return redirect(url_for('determine_similar_word'))

# runs app
if __name__ == '__main__':
    app.run()