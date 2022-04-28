from tkinter import *
from tkinter import ttk
from modules.add_etudiant import *
from modules.add_filiere import *
from modules.modify_etudiant import *
from modules.modify_filiere import *
from modules.delete_etudiant import *
from modules.delete_filiere import *

def Interface(root):
        root.title("Gestion des étudiants & filières")
        # Taille de la fenetre
        root.geometry("1000x600+0+0")
        # La fenetre ne peut pas etre "resizable"
        root.resizable(0,0)

        # Le titre à l'intérieur de la fenetre
        root_title = Label(root, text="Panneau de gestion des étudiants & filières",font=("Montserrat",25))
        root_title.pack(side=TOP,pady=5)

        # Parti de visualisation des etudiants
        frame_etudiants = Frame(root,bd=1,relief=RIDGE,bg="#b2bec3")
        frame_etudiants.place(x=30,y=65,width=600,height=300)
        etudiants_scrollY = Scrollbar(frame_etudiants, orient=VERTICAL)

        table_etudiants = ttk.Treeview(frame_etudiants,yscrollcommand=etudiants_scrollY.set)
        etudiants_scrollY.pack(side=RIGHT,fill=Y)
        etudiants_scrollY.config(command=table_etudiants.yview)

            # Les colonnes de la table etudiants
        table_etudiants['columns'] = ("id","nom","prenom","filiere","age")

        table_etudiants.heading("id",text="Id. de l'étudiant")
        table_etudiants.column("id", width=120, anchor="center")

        table_etudiants.heading("nom", text="Nom")
        table_etudiants.column("nom", width=120, anchor="center")

        table_etudiants.heading("prenom", text="Prénom")
        table_etudiants.column("prenom", width=120, anchor="center")

        table_etudiants.heading("filiere", text="Filière")
        table_etudiants.column("filiere", width=120, anchor="center")

        table_etudiants.heading("age", text="Age")
        table_etudiants.column("age", width=120, anchor="center")

        table_etudiants['show']='headings'
        table_etudiants.pack(fill=BOTH,expand=1)

        # Récuperer les étudiants & les afficher dans la table_etudiants
        get_etudiants_for_tree(table_etudiants)

        # Parti de visualisation des filières
        frame_filieres = Frame(root, bd=1, relief=RIDGE, bg="#b2bec3")
        frame_filieres.place(x=650, y=65, width=320, height=300)
        filieres_scrollY = Scrollbar(frame_filieres, orient=VERTICAL)
        table_filieres = ttk.Treeview(frame_filieres)

        filieres_scrollY.pack(side=RIGHT, fill=Y)
        filieres_scrollY.config(command=table_filieres.yview)

            # Les colonnes de la table filières
        table_filieres['columns'] = ('id', 'filiere')

        table_filieres.heading("id",text="Id. de la filière")
        table_filieres.column("id", width="100", anchor="center")

        table_filieres.heading("filiere", text="La filière")
        table_filieres.column("filiere", width="220", anchor="center")

        table_filieres['show']='headings'
        table_filieres.pack(fill=BOTH,expand=1)

        # Récuperer les filieres & les afficher dans la table_filieres
        get_filieres_for_tree(table_filieres)

        # Styler les boxs Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#b2bec3",
                        rowheight=25,
                        fieldbackground="#b2bec3"
                        )
        style.map("Treeview",
                  background=[('selected','#636e72')]
                  )

        # Les bouttons des actions
        frame_bouttons = Frame(root,bd=1,relief=RIDGE)
        frame_bouttons.place(x=200,y=385,width=600,height=200)
        frame_bouttons_title = Label(frame_bouttons, text="Options",font=("Open Sans Condensed",13)).pack()

        ajouter_etudiant = Button(frame_bouttons,text="Ajouter un étudiant").place(x=50,y=40,width=150,height=60)
        ajouter_filiere = Button(frame_bouttons, text="Ajouter une filière",command=lambda: ajouter_filiere_Interface(table_filieres)).place(x=50, y=120, width=150, height=60)

        modifier_etudiant = Button(frame_bouttons, text="Modifier un étudiant",command= lambda:modifier_etudiant_Interface(table_etudiants)).place(x=225, y=40, width=150, height=60)
        modifier_filiere = Button(frame_bouttons, text="Modifier une filière",command= lambda:modifier_filiere_Interface(table_etudiants,table_filieres)).place(x=225, y=120, width=150, height=60)

        supprimer_etudiant = Button(frame_bouttons, text="Supprimer un étudiant",command= lambda:delete_etudiant(table_etudiants)).place(x=400, y=40, width=150, height=60)
        supprimer_filiere = Button(frame_bouttons, text="Supprimer une filière",command= lambda:delete_filiere(table_filieres)).place(x=400, y=120, width=150, height=60)


root = Tk()
fenetre = Interface(root)
root.mainloop()