from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modules.actions import *

def ajouter_etudiant_Interface(table):
    def ajouter_etudiant():
        # Les variables
        Nom = nom_input.get().replace(" ", "")
        Prenom = prenom_input.get().replace(" ", "")
        Age = age_input.get()
        Filiere = filiere_input.get()
        Filiere_id = get_filiere_id(Filiere)

        if Nom == '' or Prenom == '' or Age == '':
            messagebox.showerror('Erreur', 'Veuillez remplir tous les champs !')
        else:
            try:
                age = int(Age)
            except:
                messagebox.showerror('Erreur', 'L\'âge doit être une valeur numérique !')
            else:
                insert_etudiant(Nom, Prenom, Filiere_id, Age)
                messagebox.showinfo('Ajout de l\'étudiant','L\'étudiant a été ajouté avec succès !')
                get_etudiants_for_tree(table)
                frame_ajout_etudiant.destroy()


    # Fenetre d'ajout d'étudiants
    frame_ajout_etudiant = Toplevel()
    frame_ajout_etudiant.geometry("400x300+0+0")
    frame_ajout_etudiant.resizable(0, 0)
    title = Label(frame_ajout_etudiant, text="Ajouter un nouveau étudiant", font=("Montserrat", 12)).pack(pady=15)

    # Les labels
    Label(frame_ajout_etudiant, text='Nom: ').place(x=50, y=65)
    nom_input = Entry(frame_ajout_etudiant)
    nom_input.focus()
    nom_input.place(x=120, y=65, width=200, height=20)

    Label(frame_ajout_etudiant, text='Prénom: ').place(x=50, y=95)
    prenom_input = Entry(frame_ajout_etudiant)
    prenom_input.place(x=120, y=95, width=200, height=20)

    Label(frame_ajout_etudiant, text='Age: ').place(x=50, y=125)
    age_input = Entry(frame_ajout_etudiant)
    age_input.place(x=120, y=125, width=200, height=20)

    Label(frame_ajout_etudiant, text='Filière: ').place(x=50, y=155)
    filieres_list = get_filieres()
    #filiere_input = StringVar()
    #filiere_input.set('')
    #filiere_label = OptionMenu(frame_ajout_etudiant, filiere_input, *filieres_list)
    filiere_input = ttk.Combobox(frame_ajout_etudiant,state="readonly",values=filieres_list)
    filiere_input.place(x=120, y=155, width=200, height=20)

    Button(frame_ajout_etudiant, text='Ajouter l\'étudiant', bg="#00b894", activebackground="#55efc4",command=ajouter_etudiant).place(x=125, y=200, width=150, height=25)

    if not len(get_filieres()):
        frame_ajout_etudiant.destroy()
        messagebox.showerror('Erreur','On ne peut pas ajouter un étudiant s\'il n\'y a pas de filière.\n\n Ajouter une filière d\'abord !')

