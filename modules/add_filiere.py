from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modules.actions import *

def ajouter_filiere_Interface(table):
    def ajouter_filiere():
        # La variable
        Nom_filiere = nom_filiere.get().replace(" ", "").upper()

        if Nom_filiere == '':
            messagebox.showerror('Erreur', 'Veuillez remplir les champs vides !')
        else:
            if check_filiere_already_exist(Nom_filiere) == 0:
                insert_filiere(Nom_filiere)
                messagebox.showinfo('Ajout de la filière', 'La filière a été ajouté avec succès !')
                get_filieres_for_tree(table)
                frame_ajout_filiere.destroy()
            else:
                messagebox.showerror('Erreur', 'Cette filière existe déja !')

    # Fenetre d'ajout d'étudiants
    frame_ajout_filiere = Toplevel()
    frame_ajout_filiere.geometry("300x150+0+0")
    frame_ajout_filiere.resizable(0, 0)
    title = Label(frame_ajout_filiere, text="Ajouter une nouvelle filière", font=("Montserrat", 12)).pack(pady=15)

    # Label
    Label(frame_ajout_filiere, text='Nom de la filière : ').place(x=25, y=65)
    nom_filiere = Entry(frame_ajout_filiere)
    nom_filiere.focus()
    nom_filiere.place(x=125, y=65, width=150, height=20)

    Button(frame_ajout_filiere, text='Ajouter la filière', bg="#00b894", activebackground="#55efc4",command=ajouter_filiere).place(x=80, y=105, width=150, height=25)
