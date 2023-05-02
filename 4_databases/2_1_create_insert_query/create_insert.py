"""
Making a database and insertting some data using sqlite library
"""

import sqlite3

# Connects to the database or create it if doesn't exists. The DB is in the same folder
conn = sqlite3.connect('ages.sqlite')
# Create a cursor object to interact with the database
cur = conn.cursor()

# DELETE the table if exists
cur.execute('DROP TABLE IF EXISTS Ages')

# Create the table
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

# Delete every row in the table
cur.execute('DELETE FROM Ages')

data_tuples =[
    ('Antonyo', 35),
    ('Carley', 15),
    ('Kandel', 26),
    ('Luiza', 24),
    ('Mindi', 32),
    ('Happy', 17),
]

# Insert the data
for tuple in data_tuples:
    cur.execute('INSERT INTO Ages (name, age) VALUES ( ?, ?)', tuple)

# Save the changes made to the DB
conn.commit()


