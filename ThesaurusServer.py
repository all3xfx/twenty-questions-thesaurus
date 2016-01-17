# all the imports
import sqlite3
from SynonymInterface import SynonymInterface
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, make_response


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
current_synonym = None
synonyms = []


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
    global synonym_graph
    synonym_graph = SynonymInterface(request.form['pos'])
    return redirect(url_for('determine_original_similar_word'))


@app.route('/orig_sim_word', methods=['POST'])
def determine_original_similar_word():
    global current_synonym
    current_synonym = request.form['simword']
    global synonyms
    synonyms = synonym_graph.find_synonyms(current_synonym)[:5]
    return render_template('sim_word.html', syns=synonyms)


@app.route('/sim_word', methods=['POST'])
def determine_similar_word():
    global current_synonym
    current_synonym = request.form['simword']
    global synonyms
    synonyms = SynonymInterface.find_synonyms(current_synonym)[:5]
    return render_template('sim_word.html', syns=synonyms)


@app.route('/<string:page_name>/')
def static_page(page_name):
    """
    Renders static pages
    """
    return render_template('%s.html' % page_name)

# runs app
if __name__ == '__main__':
    app.run()

