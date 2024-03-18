import sqlite3

# Connect to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('entite.db')

# Create a cursor object
c = conn.cursor()

# Create table ENTITE
c.execute('''
    CREATE TABLE ENTITE (
        ID INT PRIMARY KEY NOT NULL,
        LABEL TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()