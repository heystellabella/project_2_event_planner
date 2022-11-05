from crypt import methods
from distutils.log import debug
from pydoc import describe
from symbol import star_expr
from tkinter.messagebox import RETRY
from urllib import request, response
import urllib.request as urllib
from socket import IP_MAX_MEMBERSHIPS
from flask import Flask, render_template, redirect, request

from models.database import sql_select
from models.database import sql_select_action
from models.database import sql_select_fetchone
from models.database import insert_event
from models.database import delete_event

import psycopg2
import random

app = Flask(__name__)

@app.route('/')
def home():
    events_result = sql_select('SELECT event_id, event_name, image_url, description, date, start_time, end_time FROM events' )
    event = []
    for row in events_result:
        event_id, event_name, image_url, description, date, start_time, end_time = row
        event.append([event_id, event_name, image_url, description, date, start_time, end_time])

    return render_template('homepage.html', event=event)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create_event')
def create_event():
    return render_template('create_event.html')

@app.route('/create_event_action', methods=['GET','POST'])
def create_event_action():
    # event_name = request.form.get('event_name')
    # date = request.form.get('date')
    # start_time = request.form.get('start_time')
    # end_time = request.form.get('end_time')
    # description = request.form.get('description')
    # image_url = request.form.get('image_url')
    # invite_list = request.form.get('invite_list')
    event_name = request.form['event_name']
    date = request.form['date']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    description = request.form['description']
    image_url = request.form['image_url']
    invite_list = request.form['invite_list']

    insert_event(event_name, date, start_time, end_time, description, image_url, invite_list)

    new_event_id = sql_select('SELECT count(event_id) FROM events')[0][0]
    print(f'NEW EVENT ID = {new_event_id}')
    return redirect(f'/event_page/{new_event_id}')

@app.route('/event_page/<event_id>')
def event_page(event_id):
    event_name, image_url, description, date, start_time, end_time, invite_list = sql_select_fetchone('SELECT event_name, image_url, description, date, start_time, end_time, invite_list from events where event_id = %s', [event_id])

    return render_template('event_page.html',event_name = event_name, image_url=image_url, description=description, date=date, start_time = start_time, end_time = end_time, invite_list = invite_list )

@app.route('/random_event')
def random_event_action():
    #number of events is a list[] containing a tuple()
    number_of_events_result = sql_select('SELECT count(event_id) FROM events')

    number_of_events = number_of_events_result[0][0]
    print(number_of_events)
    print(type(number_of_events))

    random_event_id = random.randint(1,number_of_events)
    return redirect(f'/event_page/{random_event_id}')

@app.route('/remove_event/<event_id>')
def remove_event(event_id):
    event_name = sql_select('SELECT event_name from events where event_id = %s', [event_id])
    return render_template('delete_event.html', event_id = event_id, event_name = event_name)

@app.route('/remove_event_action', methods = ['POST'])
def remove_event_action():
    event_id = request.form.get('event_id')
    print(event_id)
    delete_event(event_id)
    return redirect('/')

@app.route('/join_event_action', methods = ['POST'])
def join_event_action():
    new_invitee = request.form.get('name')

    return redirect('/event')

app.run(debug=True)