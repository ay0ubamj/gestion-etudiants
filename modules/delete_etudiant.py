from modules.actions import *

def delete_etudiant(table_etudiant):
    if not len(get_selected_row_in_tree(table_etudiant)):
        messagebox.showerror('Erreur', 'Veuillez séléctionner un étudiant !')
    else:
        row = get_selected_row_in_tree(table_etudiant)
        res = messagebox.askquestion('Supprimer l\'étudiant', 'Vous êtes sûre de vouloir supprimer cet étudiant ?')
        if res == 'yes':
            exec = cursor.execute("DELETE FROM etudiants WHERE idEtudiant = ?", (row[0],))
            get_etudiants_for_tree(table_etudiant)
            messagebox.showinfo('Supprimer l\'étudiant', 'L\'étudiant a été supprimé avec succès !')
        get_etudiants_for_tree(table_etudiant)