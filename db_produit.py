import sqlite3

# for /produit_alimentaire/

def obtenir_tout_alimentaire():
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit_alimentaire")
    rows = cursor.fetchall()
    conn.close()
    return rows

def obtenir_alimentaire(id):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit_alimentaire WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()
    return row

def ajouter_alimentaire(id, libelle, categorie, prix):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    print(id, libelle, categorie, prix)
    cursor.execute("INSERT INTO Produit_alimentaire (id, libelle, categorie, prix) VALUES (?, ?, ?, ?)", (id, libelle, categorie, prix))
    conn.commit()
    conn.close()

def supprimer_alimentaire(id):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produit_alimentaire WHERE id=?", (id,))
    conn.commit()
    conn.close()

def mettre_a_jour_alimentaire(id, libelle, categorie, prix):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Produit_alimentaire SET libelle=?, categorie=?, prix=? WHERE id=?", (libelle, categorie, prix, id))
    conn.commit()
    conn.close()
    
# for /produit_techno/

def obtenir_tout_techno():
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit_techno")
    rows = cursor.fetchall()
    conn.close()
    return rows

def obtenir_techno(id):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit_techno WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()
    return row

def ajouter_techno(libelle, categorie, description, marque, prix):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produit_techno (libelle, categorie, description, marque, prix) VALUES (?, ?, ?, ?, ?)", (libelle, categorie, description, marque, prix))
    conn.commit()
    conn.close()
    
def supprimer_techno(id):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produit_techno WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
def mettre_a_jour_techno(id, libelle, categorie, description, marque, prix):
    conn = sqlite3.connect('boutique.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Produit_techno SET libelle=?, categorie=?, description=?, marque=?, prix=? WHERE id=?", (libelle, categorie, description, marque, prix, id))
    conn.commit()
    conn.close()
