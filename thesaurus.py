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

# runs app
if __name__ == '__main__':
    app.run()