DROP TABLE IF EXISTS events cascade;

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name TEXT,
    image_url TEXT,
    description TEXT,
    date TIMESTAMP,
    start_time TIME,
    end_time TIME
    -- invite_list TEXT
);

DROP TABLE IF EXISTS users cascade; 

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    username TEXT
    -- user_email TEXT,
    -- user_password TEXT
);

DROP TABLE IF EXISTS invite_list cascade; 

CREATE TABLE invite_list(
    event_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    -- FOREIGN KEY (username) REFERENCES users(username)
);
