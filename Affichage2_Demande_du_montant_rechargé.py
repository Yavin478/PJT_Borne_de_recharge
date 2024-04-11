from tkinter import *
from PIL import Image, ImageTk


# Création de page
root = Tk()
root.title("PAGE")
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.destroy())

taille = (root.winfo_screenwidth(), root.winfo_screenheight())

#intégration du fond plus redimensionnement
back = Image.open("Static/Bg_508.jpg")
back_redimensionnee = back.resize((taille[0], taille[1]))
back_tk = ImageTk.PhotoImage(back_redimensionnee)

#intégration de la fleche + dimensionnement taille
fleche = Image.open("Static/fleche.png")
taille_fleche = [int(taille[0] / 7), int(taille[1] / 8)]
fleche_redimensionnee = fleche.resize((taille_fleche[0], taille_fleche[1]))
fleche_tk = ImageTk.PhotoImage(fleche_redimensionnee)


canvas1 = Canvas(root, width=taille[0], height=taille[1])
canvas1.pack(fill="both", expand=True)


canvas1.create_image(0, 0, image=back_tk, anchor="nw")

# Placement de la fleche en adaptant sa taille à l'écran
canvas1.create_image(int((taille[0] - taille_fleche[0])), int((taille[1] - taille_fleche[1])), image=fleche_tk,
                     anchor="nw")

#création du montant qui est afficher sur le canva
texte_saisi = ""

#récupération des chiffres du montant tapé sur le clavier
def keypress(event):
    global texte_saisi
    if event.keysym.startswith("KP"):  # Vérifie si la touche est du clavier numérique
        texte_saisi += event.keysym[-1]  # Ajoute le chiffre correspondant
    else:
        texte_saisi += event.char
    update_text()

#actualisation du texte taper au fur et à mesure ainsi que du canva qui l'affiche
def update_text():
    montant_texte = texte_saisi + " \u20AC"  # Ajoute le symbole de l'euro au texte
    canvas1.itemconfig(tu, text=montant_texte)
    yo.config(text=montant_texte)

yo = Label(root, text=texte_saisi)
yo.pack()

#affichage du montant tapé
tu = canvas1.create_text(taille[0] / 2, taille[1] / 1.7, text=texte_saisi + " \u20AC", fill="black", font=("Impact", 60))

#Ecriture du texte
canvas1.create_text(taille[0] / 2, taille[1] / 2, text="Choisisez le montant à recharger", fill="black", font=("Impact", 60))

canvas1.create_text(taille[0] / 2, taille[1] /1.03, text="Appuyer sur la touche échappe pour annuler", fill="black", font=("Impact", 40))

root.bind('<KeyPress>', keypress)
root.mainloop()