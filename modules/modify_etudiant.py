from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modules.actions import *

def modifier_etudiant_Interface(table):
    if not len(get_selected_row_in_tree(table)):
        messagebox.showerror('Erreur', 'Veuillez séléctionner un étudiant !')
    else:
        def modifier_etudiant():
            id = id_etud.get()
            nv_nom = nom_input.get()
            nv_prenom = prenom_input.get()
            nv_age = age_input.get()
            nv_filiere_id = get_filiere_id(filiere_input.get())

            if nv_nom == '' or nv_prenom == '' or nv_age == '':
                messagebox.showerror('Erreur', 'Veuillez remplir tous les champs !')
            else:
                try:
                    age = int(nv_age)
                except:
                    messagebox.showerror('Erreur', 'L\'âge doit être une valeur numérique !')
                else:
                    update_etudiant(id, nv_nom, nv_prenom, nv_filiere_id, nv_age)
                    messagebox.showinfo('Modifier l\'étudiant',
                                        'Les données de l\'étudiant ont été modifier avec succès !')
                    get_etudiants_for_tree(table)
                    frame_modify_etudiant.destroy()

        # Fenetre d'ajout d'étudiants
        frame_modify_etudiant = Toplevel()
        frame_modify_etudiant.geometry("400x300+0+0")
        frame_modify_etudiant.resizable(0, 0)
        title = Label(frame_modify_etudiant, text="Modifier l'étudiant", font=("Montserrat", 12)).pack(pady=15)

        # Liste des valeurs de l'étudiant selectionné
        row = get_selected_row_in_tree(table)
        # Les variables
        id_etud = IntVar()
        id_etud.set(row[0])
        selected_nom = StringVar()
        selected_nom.set(row[1])
        selected_prenom = StringVar()
        selected_prenom.set(row[2])
        selected_age = IntVar()
        selected_age.set(row[4])
        selected_filiere = StringVar()
        selected_filiere.set(row[3])

        # Les labels
        Label(frame_modify_etudiant, text='Nom: ').place(x=50, y=65)
        nom_input = Entry(frame_modify_etudiant, textvariable=selected_nom)
        nom_input.focus()
        nom_input.place(x=120, y=65, width=200, height=20)

        Label(frame_modify_etudiant, text='Prénom: ').place(x=50, y=95)
        prenom_input = Entry(frame_modify_etudiant, textvariable=selected_prenom)
        prenom_input.place(x=120, y=95, width=200, height=20)

        Label(frame_modify_etudiant, text='Age: ').place(x=50, y=125)
        age_input = Entry(frame_modify_etudiant, textvariable=selected_age)
        age_input.place(x=120, y=125, width=200, height=20)

        Label(frame_modify_etudiant, text='Filière: ').place(x=50, y=155)
        filieres_list = get_filieres()
        filiere_input = ttk.Combobox(frame_modify_etudiant, state="readonly", values=filieres_list)
        filiere_input.set(selected_filiere.get())
        filiere_input.place(x=120, y=155, width=200, height=20)

        Button(frame_modify_etudiant, text='Modifier l\'étudiant', bg="#00b894", activebackground="#55efc4",
               command=modifier_etudiant).place(x=125, y=200, width=150, height=25)

