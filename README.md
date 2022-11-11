# project_2_event_planner

TECHNOLOGIES USED
HTML -  to render the web pages to the user
PYTHON - to take user input and data and manipulate it
PYSCOPG2 - to connect to the events database
FLASK - to allow python to connect with HTML pages 
SQL - to manipulate and retrieve data from the database

APPROACH TAKEN
I started off with 5 main pages in mind:
    1. Homepage - to display the the upcoming events
    2. About Us - gives information about the site
    3. Event Page - shows information about the event
    4. Create Event - a page for a user to input information to create an event
    5. Random Event - fun functionality that takes you to a random event that has been created

I created 3 tables:
    1. list of events
    2. list of users
    3. invite list which displays which users are attending which events - connected with foreign key

When a a user navigates to create an event, the event is then added to the events table in the DB, the invitees are checked against the current users and if they do not exist, they are added to the users list. From this, the invite list is updated.

As these tables are updated, the homepage information that displays event information is updated, the random event function will have more events to randomly choose from and the event page will display the new event infomration when clicked.

INSTALLATION INSTRUCTIONS
- pip install flask
- pip install psycopg2
- download schema.sql and seed.sql files
- connect to db 'event_db' using --> psql event_db
- run: psql event_db < schema.sql
- run: psql event_db < seed.sql
- run in python command line: python event_planner.py

UNSOLVED PROBLEMS
- Currently the invite list only takes in a name that cannot be repeated, so two people with the same name cannot attend the same event
- Invite list is case sensitive

I WOULD LIKE TO ADD:
- Option to click attending for an event
- Weather API to display weather for the day of the event
- Display events on homepage by date of the event, not date created
- Option to log in to see your events
- Option to create private events