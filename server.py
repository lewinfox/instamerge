from flask import Flask, render_template
import datetime
from app_secrets import app_secrets

client_id = app_secrets.get('client_id')
client_secret = app_secrets.get('client_id')

app = Flask(__name__)

@app.route('/')
def root(name=None):
    now = datetime.datetime.now()
    return render_template('index.html', name='Hello', now=now)

@app.route('/redirect')
def redirect():
    print('Redirect')
    return render_template('redirect.html')
