import sqlite3

def obtenir_toutes_entite_bd():
    conn = sqlite3.connect('entite.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entite")
    rows = cursor.fetchall()
    conn.close()
    return rows

def obtenir_entite_bd(id):
    conn = sqlite3.connect('entite.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entite WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()
    return row

def ajouter_entite_bd(id, label):
    conn = sqlite3.connect('entite.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entite (id, label) VALUES (?, ?)", (id, label))
    conn.commit()
    conn.close()

def supprimer_entite_bd(id):
    conn = sqlite3.connect('entite.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM entite WHERE id=?", (id,))
    conn.commit()
    conn.close()

def mettre_a_jour_entite_db(id, label):
    conn = sqlite3.connect('entite.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE entite SET label=? WHERE id=?", (label, id))
    conn.commit()
    conn.close()