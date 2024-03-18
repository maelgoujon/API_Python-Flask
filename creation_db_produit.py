import sqlite3

# Connect to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('boutique.db')

# Create a cursor object
c = conn.cursor()

# Create table Produit alimentaire
c.execute('''
    CREATE TABLE Produit_alimentaire (
        ID INT PRIMARY KEY NOT NULL,
        LIBELLE TEXT,
        CATEGORIE TEXT,
        PRIX FLOAT
    )
''')

# Create table Produit techno
c.execute('''
    CREATE TABLE Produit_techno(
        ID INT PRIMARY KEY NOT NULL,
        LIBELLE TEXT,
        CATEGORIE TEXT,
        DESCRIPTION TEXT,
        MARQUE TEXT,
        PRIX FLOAT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()