INSERT INTO events(event_name, image_url, description, date, start_time, end_time) VALUES ('Cool Event 1', '/images/eighteenth_birthday.jpg', 'Cool description about event for 18th birthday','2022-12-01', '18:00:00', '20:00:00');
INSERT INTO events(event_name, image_url, description, date, start_time, end_time) VALUES ('Cool Event 2', '/images/conference.jpg', 'Cool description about event for conference','2022-11-10', '16:00:00', '21:00:00');

--------

INSERT INTO users(username) VALUES ('Stella');
INSERT INTO users(username) VALUES ('Barbara');
INSERT INTO users(username) VALUES ('Pearl');

--------

INSERT INTO invite_list(event_id, user_id) VALUES (1, 1);
INSERT INTO invite_list(event_id, user_id) VALUES (1, 2);
INSERT INTO invite_list(event_id, user_id) VALUES (1, 3);
