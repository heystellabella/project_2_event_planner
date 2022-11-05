DROP TABLE IF EXISTS events;

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name TEXT,
    image_url TEXT,
    description TEXT,
    date TIMESTAMP,
    start_time TIME,
    end_time TIME,
    invite_list TEXT
);

DROP TABLE IF EXISTS users; 

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    user_name TEXT,
    user_email TEXT,
    user_password TEXT
);
