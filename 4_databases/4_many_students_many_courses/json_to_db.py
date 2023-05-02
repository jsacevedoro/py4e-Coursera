'''This application will read roster data in JSON format, parse the file, 
and then produce an SQLite database that contains a User, Course, 
and Member table and populate the tables from the data file'''

import json
import sqlite3

def populate():
    # Extract the data from json file
    str_data = open('roster_data.json').read()
    data = json.loads(str_data)

    # Create the conexion with the db
    conn = sqlite3.connect('rosterdb.sqlite')
    cur = conn.cursor()

    # Populte according json schema and db schema
    for entry in data:
        name = entry[0]
        course = entry[1]
        role = entry[2]

        cur.execute('''INSERT OR IGNORE INTO User (name)
            VALUES ( ? )''', ( name, ) )
        cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
        user_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', ( course, ) )
        cur.execute('SELECT id FROM Course WHERE title = ? ', (course, ))
        course_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
            ( user_id, course_id, role ) )

    conn.commit()

    return None