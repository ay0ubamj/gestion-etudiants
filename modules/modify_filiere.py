from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modules.actions import *

def modifier_filiere_Interface(table_etudiant,table_filiere):
    if not len(get_selected_row_in_tree(table_filiere)):
        messagebox.showerror('Erreur', 'Veuillez séléctionner une filière !')
    else:
        def modifier_filiere():
            id = id_filiere.get()
            Nom_filiere = nom_filiere.get().replace(" ", "").upper()

            if Nom_filiere == '':
                messagebox.showerror('Erreur', 'Veuillez remplir les champs vides !')
            else:
                if check_filiere_already_exist(Nom_filiere) == 0:
                    update_filiere(id, Nom_filiere)
                    messagebox.showinfo('Modifier la filière', 'Le nom de la filière a été modifier avec succès !')
                    get_etudiants_for_tree(table_etudiant)
                    get_filieres_for_tree(table_filiere)
                    frame_modify_filiere.destroy()
                else:
                    messagebox.showerror('Erreur', 'Cette filière existe déja !')

        # Fenetre d'ajout d'étudiants
        frame_modify_filiere = Toplevel()
        frame_modify_filiere.geometry("300x150+0+0")
        frame_modify_filiere.resizable(0, 0)
        title = Label(frame_modify_filiere, text="Modifier la filière", font=("Montserrat", 12)).pack(pady=15)

        # Liste des valeurs de l'étudiant selectionné
        row = get_selected_row_in_tree(table_filiere)
        # Les variables
        id_filiere = IntVar()
        id_filiere.set(row[0])
        selected_nom_filiere = StringVar()
        selected_nom_filiere.set(row[1])

        # Label
        Label(frame_modify_filiere, text='Nom de la filière : ').place(x=25, y=65)
        nom_filiere = Entry(frame_modify_filiere, textvariable=selected_nom_filiere)
        nom_filiere.focus()
        nom_filiere.place(x=125, y=65, width=150, height=20)

        Button(frame_modify_filiere, text='Modifier la filière', bg="#00b894", activebackground="#55efc4",command=modifier_filiere).place(x=80, y=105, width=150, height=25)