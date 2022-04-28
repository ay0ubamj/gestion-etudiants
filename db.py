# Vous pouvez utiliser ce fichier pour créer les tables dans le cas où
# le fichier Database.db à été supprimer
'''
import sqlite3 as s
connection = s.connect('Database.db')
cursor = connection.cursor()

# Here we created our tables
cursor.execute("""CREATE TABLE etudiants(
                idEtudiant INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                idFiliereFK INTEGER NOT NULL,
                age INTEGER NOT NULL,
                FOREIGN KEY (idFiliereFK) REFERENCES filieres (idFiliere)
                )""")

cursor.execute("""CREATE TABLE filieres(
                idFiliere INTEGER PRIMARY KEY,
                nomFiliere TEXT NOT NULL
                )""")

connection.commit()
'''