'''This application will read an iTunes export file in XML and produce a properly normalized database'''

import xml.etree.ElementTree as ET
import sqlite3


def get_value(entry, field):
    found = False
    for child in entry:
        # If found is True then the previous tag matched with the field, so in this tag there is the value we need
        if found : return child.text
        # If found the field set found to True preparing for catch in the next iteration
        if child.tag == 'key' and child.text == field:
            found = True
    # If didn't find the field, return None    
    return None


# Catch the xml directly
tree = ET.parse('Library.xml')
# Considering the xml schema, this is where the tracks are stored
all = tree.findall('dict/dict/dict')

# Connect to the database
conn = sqlite3.connect("music_db.sqlite")
cur = conn.cursor()

for entry in all:
    # We just need the elements whoose first tag is Track ID
    if entry[0].text != "Track ID": 
        continue
    else: 
        name = get_value(entry, "Name")
        artist = get_value(entry, "Artist")
        album = get_value(entry, "Album")
        genre = get_value(entry, "Genre")
        count = get_value(entry, "Play Count")
        rating = get_value(entry, "Rating")
        lenght = get_value(entry, "Total Time")
        
        
        if name is None or artist is None or album is None or genre is None:
            continue

        else:
            # Insert the Genre if doesn't exists and get its id anyways
            cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre, ))
            cur.execute('SELECT id from Genre WHERE name == ?', (genre, ))
            genre_id = cur.fetchone()[0]
            
            # Insert the Artist if doesn't exists and get its id anyways 
            cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist, ))
            cur.execute('SELECT id from Artist WHERE name == ?', (artist, ))
            artist_id = cur.fetchone()[0]

            # Insert the Album pulling the artist_id if doesn't exists and get its id anyways
            cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id ))
            cur.execute('SELECT id from Album WHERE title == ?', (album, ))
            album_id = cur.fetchone()[0]

            # Insert the track pulling all the other ids 
            cur.execute('''
                INSERT OR REPLACE INTO track 
                (title, album_id, genre_id, len, rating, count) 
                VALUES (?, ?, ?, ?, ?, ?)''',
                (name, album_id, genre_id, lenght, rating, count)
            )

        conn.commit()




        
            



