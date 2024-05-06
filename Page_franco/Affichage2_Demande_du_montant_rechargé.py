from tkinter import *
from PIL import Image, ImageTk

# Création de la fenêtre principale
root = Tk()
root.title("PAGE")
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.destroy())  # Permet de quitter la fenêtre avec la touche "Échap"

# Récupération des dimensions de l'écran
taille = (root.winfo_screenwidth(), root.winfo_screenheight())

# Importation et redimensionnement de l'image de fond
back = Image.open("Static/Bg_508.jpg")
back_redimensionnee = back.resize((taille[0], taille[1]))
back_tk = ImageTk.PhotoImage(back_redimensionnee)

# Importation et redimensionnement de la flèche
fleche = Image.open("Static/fleche.png")
taille_fleche = [int(taille[0] / 7), int(taille[1] / 8)]
fleche_redimensionnee = fleche.resize((taille_fleche[0], taille_fleche[1]))
fleche_tk = ImageTk.PhotoImage(fleche_redimensionnee)

# Création du canevas pour afficher l'image de fond
canvas1 = Canvas(root, width=taille[0], height=taille[1])
canvas_background = Canvas(root, width=taille[0], height=taille[1])
canvas1.pack(fill="both", expand=True)

canvas_background.create_image(0, 0, image=back_tk, anchor="nw")

# Fonction pour faire clignoter la flèche
def toggle_visibility():
    if canvas1.itemcget(fleche_img, "state") == "hidden":
        canvas1.itemconfigure(fleche_img, state="normal")
    else:
        canvas1.itemconfigure(fleche_img, state="hidden")
    root.after(500, toggle_visibility)  # Changez ici le délai entre les clignotements en millisecondes

# Création de la flèche sur le canevas
fleche_img = canvas1.create_image(int((taille[0] - taille_fleche[0])), int((taille[1] - taille_fleche[1])), image=fleche_tk, anchor="nw")
toggle_visibility()  # Démarre le clignotement au lancement

# Initialisation de la variable pour le texte saisi
texte_saisi = ""

# Gestion de l'événement de pression d'une touche
def keypress(event):
    global texte_saisi
    if event.keysym == "BackSpace":  # Vérifie si la touche pressée est la touche "Retour Arrière"
        texte_saisi = texte_saisi[:-1]  # Supprime le dernier caractère du texte saisi
    elif event.keysym.startswith("KP"):  # Vérifie si la touche est du clavier numérique
        texte_saisi += event.keysym[-1]  # Ajoute le chiffre correspondant
    else:
        texte_saisi += event.char
    update_text()  # Met à jour le texte affiché

# Fonction pour supprimer le dernier caractère du texte saisi



# Fonction pour mettre à jour le texte affiché
def update_text():
    montant_texte = texte_saisi + " \u20AC"  # Ajoute le symbole de l'euro au texte
    canvas1.itemconfig(tu, text=montant_texte)

# Étiquette pour afficher le texte saisi
yo = Label(root, text=texte_saisi)
yo.pack()

# Texte initial sur le canevas
tu = canvas1.create_text(taille[0] / 2, taille[1] / 1.7, text=texte_saisi + " \u20AC", fill="black", font=("Impact", 60))

# Texte explicatif sur le canevas
canvas1.create_text(taille[0] / 2, taille[1] / 2, text="Choisissez le montant à recharger", fill="black", font=("Impact", 60))
canvas1.create_text(taille[0] / 2, taille[1] / 1.03, text="Appuyez sur la touche échap pour annuler", fill="black", font=("Impact", 40))

# Association de la fonction keypress à l'événement de pression d'une touche
root.bind('<KeyPress>', keypress)
root.mainloop()
