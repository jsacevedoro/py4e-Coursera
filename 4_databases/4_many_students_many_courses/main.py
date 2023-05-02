
import sqlite3
from json_to_db import populate
from create_db import create_database

def check_with_query(query_string):
    conn = sqlite3.connect('rosterdb.sqlite')
    cur = conn.cursor()
    cur.execute(query_string)
    data = cur.fetchall()
    print(data)
    return None

q1 = '''
    SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
'''

q2 = '''
    SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
'''


def main():
    create_database()
    populate()
    check_with_query(q1)
    check_with_query(q2)
    return None

main()