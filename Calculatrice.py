from tkinter import *

def show(valeur):
    # Ajouter le chiffre ou l'opérateur à l'affichage
    current_text = entry_var.get()
    entry_var.set(current_text + str(valeur))

def resultat():
    try:
        # Évaluer l'expression mathématique et afficher le résultat
        expression = entry_var.get()
        result = eval(expression)  # Calculer l'expression entrée
        entry_var.set(result)
    except:
        entry_var.set("Erreur")  # Si une erreur se produit (ex: division par 0)

def clear():
    # Effacer le contenu de l'affichage
    entry_var.set("")

root = Tk()
root.title("Calculatrice")

# Variable pour stocker le texte affiché dans l'entrée
entry_var = StringVar()

# Créer un champ d'entrée pour afficher l'expression et le résultat
Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4).grid(row=0, column=0, columnspan=4)

# Créer les boutons avec la fonction show pour les nombres et opérateurs
Button(root, text='7', padx=20, pady=20, command=lambda: show(7)).grid(row=1, column=0)
Button(root, text='8', padx=20, pady=20, command=lambda: show(8)).grid(row=1, column=1)
Button(root, text='9', padx=20, pady=20, command=lambda: show(9)).grid(row=1, column=2)
Button(root, text='/', padx=20, pady=20, command=lambda: show('/')).grid(row=1, column=3)

Button(root, text='4', padx=20, pady=20, command=lambda: show(4)).grid(row=2, column=0)
Button(root, text='5', padx=20, pady=20, command=lambda: show(5)).grid(row=2, column=1)
Button(root, text='6', padx=20, pady=20, command=lambda: show(6)).grid(row=2, column=2)
Button(root, text='*', padx=20, pady=20, command=lambda: show('*')).grid(row=2, column=3)

Button(root, text='1', padx=20, pady=20, command=lambda: show(1)).grid(row=3, column=0)
Button(root, text='2', padx=20, pady=20, command=lambda: show(2)).grid(row=3, column=1)
Button(root, text='3', padx=20, pady=20, command=lambda: show(3)).grid(row=3, column=2)
Button(root, text='-', padx=20, pady=20, command=lambda: show('-')).grid(row=3, column=3)

Button(root, text='0', padx=20, pady=20, command=lambda: show(0)).grid(row=4, column=0)
Button(root, text='C', padx=20, pady=20, command=clear).grid(row=4, column=1)  # Clear button
Button(root, text='=', padx=20, pady=20, command=resultat).grid(row=4, column=2)  # Button for result '='
Button(root, text='+', padx=20, pady=20, command=lambda: show('+')).grid(row=4, column=3)

root.mainloop()
