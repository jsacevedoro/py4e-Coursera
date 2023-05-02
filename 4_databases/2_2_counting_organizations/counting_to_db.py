""" This application will read the mailbox data (mbox.txt) and 
count the number of email messages per organization (i.e. domain name of the email address) 
using a database with the following schema to maintain the counts.
SCHEMA: CREATE TABLE Counts (org TEXT, count INTEGER)"""


import sqlite3
import re
import pandas as pd

conn = sqlite3.connect('organizations.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')


fh = open("mbox.txt")

counts = dict()
for line in fh: 
    if re.search('^From:', line):
        # Greedy find for substrings with the form "@______"
        domain = re.findall('@(.+\S)', line)[0]
        cur.execute('SELECT count FROM Counts WHERE org == ?', (domain,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org == ?', (domain,))
        
conn.commit()   

# Print the data in the command line

# Query the whole table
cur.execute('SELECT * FROM Counts')
# Store 
df = cur.fetchall()
print(df)
# Get the names of the columns
col_names = [tup[0] for tup in cur.description]

df = pd.DataFrame(df, columns=col_names)     
print(df)

cur.close()