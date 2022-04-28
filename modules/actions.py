import sqlite3 as s
from tkinter import messagebox

# Connexion à la BD et création du curseur
connection = s.connect('Database.db')
cursor = connection.cursor()

def get_etudiants_for_tree(table):
    # Insérer tous les étudiants de la BD dans le TreeView des étudiants
    data = cursor.execute("SELECT idEtudiant,nom,prenom,nomFiliere,age FROM etudiants INNER JOIN filieres ON etudiants.idFiliereFK = filieres.idFiliere ORDER BY idEtudiant")
    rows = data.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('','end',values=row)
    else:
        table.delete(*table.get_children())
    connection.commit()

def get_filieres_for_tree(table):
    # Insérer toutes les filieres de la BD dans le TreeView des filières
    data = cursor.execute("SELECT * FROM filieres ORDER BY idFiliere")
    rows = data.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('', 'end', values=row)
    else:
        table.delete(*table.get_children())
    connection.commit()

def get_filieres():
    # Retourne la liste de toute les filières
    data = cursor.execute("SELECT * FROM filieres")
    rows = data.fetchall()
    result = []
    if len(rows) != 0:
        for row in rows:
            result.append(row[1])
    connection.commit()
    return result

def get_filiere_id(filiere):
    # Retourne l'id d'une filière donnée comme paramètre
    data = cursor.execute("SELECT * FROM filieres")
    rows = data.fetchall()
    for row in rows:
        if row[1] == filiere:
            return int(row[0])

def insert_etudiant(nom,prenom,id_filiere,age):
    # Inserer l'etudiant
    r_id = cursor.execute('SELECT MAX(idEtudiant) FROM etudiants')
    id = r_id.fetchone()[0]
    if id==None:
        idEtudiant=1
    else:
        idEtudiant=int(id)+1

    cursor.execute("INSERT INTO etudiants(idEtudiant, nom, prenom, idFiliereFK, age) VALUES(?, ?, ?, ?, ?)", (idEtudiant,nom, prenom, id_filiere, age,))
    connection.commit()

def insert_filiere(filiere):
    # Inserer la filière
    max_id = cursor.execute('SELECT MAX(idFiliere) FROM filieres')
    idFiliere = max_id.fetchone()[0]
    if idFiliere == None:
        idFiliere = 1
    else:
        idFiliere += 1
    cursor.execute("INSERT INTO filieres(idFiliere, nomFiliere) VALUES(?, ?)",(idFiliere, filiere))
    connection.commit()

def get_selected_row_in_tree(table):
    cursor = table.focus()
    content = table.item(cursor)
    row = content['values']
    return row

def update_etudiant(id, nv_nom, nv_prenom, nv_id_filiere, nv_age):
    cursor.execute("UPDATE etudiants SET nom = ?,prenom = ?,idFiliereFK = ?,age = ? WHERE idEtudiant = ?", (nv_nom, nv_prenom, nv_id_filiere, nv_age, id,))
    connection.commit()

def update_filiere(id, nv_nom):
    cursor.execute("UPDATE filieres SET nomFiliere = ? WHERE idFiliere = ?", (nv_nom, id,))
    connection.commit()

def check_etudiant_for_filiere(idFiliere):
    data = cursor.execute("SELECT * FROM etudiants INNER JOIN filieres ON etudiants.idFiliereFK = filieres.idFiliere WHERE idFiliere = ?", (idFiliere,))
    rows = data.fetchall()
    if not len(rows):
        return 0
    else:
        return 1

def check_filiere_already_exist(nomFiliere):
    data = cursor.execute("SELECT EXISTS(SELECT * FROM filieres WHERE nomFiliere = ?)",(nomFiliere,))
    return data.fetchone()[0]