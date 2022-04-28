from modules.actions import *

def delete_filiere(table_filiere):
    if not len(get_selected_row_in_tree(table_filiere)):
        messagebox.showerror('Erreur', 'Veuillez séléctionner une filière !')
    else:
        row = get_selected_row_in_tree(table_filiere)
        if check_etudiant_for_filiere(row[0]) == 0:
            query = "DELETE FROM filieres WHERE idfiliere = ?"
            res = messagebox.askquestion('Supprimer la filière', 'Vous êtes sûre de vouloir supprimer cette filière ?')
            if res == 'yes':
                exec = cursor.execute(query, (row[0],))
                messagebox.showinfo('Supprimer la filière', 'La filière a été supprimé avec succès !')
            get_filieres_for_tree(table_filiere)
        else:
            messagebox.showwarning('Attention !', 'Vous ne pouvez pas supprimer une filière qui contient des étudiants !')

