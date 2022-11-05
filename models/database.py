import psycopg2

# SQL SELECT FOR RETURNING SOMETHING
def sql_select(sql_query, params = []):
    conn = psycopg2.connect('dbname=event_db')
    cur = conn.cursor()
    cur.execute(sql_query, params)
    # storing the fetched data in a variable so you can still close the connection and cursor within the function
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def sql_select_fetchone(sql_query, params = []):
    conn = psycopg2.connect('dbname=event_db')
    cur = conn.cursor()
    cur.execute(sql_query, params)
    # storing the fetched data in a variable so you can still close the connection and cursor within the function
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

# SQL SELECT FOR INSERTING OR UPDATING
def sql_select_action(sql_query, params = []):
    conn = psycopg2.connect('dbname=event_db')
    cur = conn.cursor()
    cur.execute(sql_query, params)
    # storing the fetched data in a variable so you can still close the connection and cursor within the function
    conn.commit()
    cur.close()
    conn.close()
    return

# SQL TO INSERT NEW EVENTS:

def insert_event(event_name, date, start_time, end_time, description, image_url, invite_list):
    
    return sql_select_action('INSERT INTO events (event_name, date, start_time, end_time, description, image_url, invite_list) VALUES (%s, %s, %s, %s, %s, %s, %s)', [event_name, date, start_time, end_time, description, image_url, invite_list])

def delete_event(event_id):
    return sql_select_action('DELETE FROM events where event_id = %s', [event_id])