INSERT INTO events(event_name, image_url, description, date, start_time, end_time) VALUES ('South East Asia Trip!', 'https://images.unsplash.com/photo-1628128573898-262b312f707e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80', 'The girls take on South East Asia! First stop Singapore, then bali and then Thailand.','2022-12-01', '18:00:00', '20:00:00');
INSERT INTO events(event_name, image_url, description, date, start_time, end_time) VALUES ('Family Christmas Dinner', 'https://images.unsplash.com/photo-1608835149345-b4d77bc490ae?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1472&q=80', 'Christmas dinner with the whole family. Everyone be there or be square - and bring a plate!','2022-12-25', '16:00:00', '21:00:00');

--------

INSERT INTO users(username) VALUES ('Stella');
INSERT INTO users(username) VALUES ('Barbara');
INSERT INTO users(username) VALUES ('Pearl');
INSERT INTO users(username) VALUES ('Mum');
INSERT INTO users(username) VALUES ('Dad');
INSERT INTO users(username) VALUES ('That Weird Uncle');
INSERT INTO users(username) VALUES ('Grandma');
INSERT INTO users(username) VALUES ('Cousin Shirley');
INSERT INTO users(username) VALUES ('Aunt Agnes');

--------

INSERT INTO invite_list(event_id, user_id) VALUES (1, 1);
INSERT INTO invite_list(event_id, user_id) VALUES (1, 2);
INSERT INTO invite_list(event_id, user_id) VALUES (1, 3);
INSERT INTO invite_list(event_id, user_id) VALUES (2, 4);
INSERT INTO invite_list(event_id, user_id) VALUES (2, 5);
INSERT INTO invite_list(event_id, user_id) VALUES (2, 6);
INSERT INTO invite_list(event_id, user_id) VALUES (2, 7);
INSERT INTO invite_list(event_id, user_id) VALUES (2, 8);
INSERT INTO invite_list(event_id, user_id) VALUES (2, 9);