'''Script to Create the Database or empty if exists'''

import sqlite3

conn = sqlite3.connect("music_db.sqlite")
cur = conn.cursor()

tables = ["Artist", "Genre", "Album", "Track"]

for table in tables:
    cmd = 'DROP TABLE IF EXISTS {}'.format(table)
    cur.execute(cmd)


cur.execute('''
    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    )
''')

cur.execute('''
    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    )
''')

cur.execute('''
    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    )
''')

cur.execute('''
    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    )
''')

conn.commit()

