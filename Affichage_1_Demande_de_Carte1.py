from tkinter import *
from PIL import Image, ImageTk
from time import sleep
root = Tk()


# Création de page
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
taille_fleche = [int(taille[0]/ 7), int(taille[1]/ 8)]
fleche_redimensionnee = fleche.resize((taille_fleche[0],taille_fleche[1]))
fleche_tk = ImageTk.PhotoImage(fleche_redimensionnee)


canvas1 = Canvas(root, width=taille[0], height=taille[1])
canvas1.pack(fill="both", expand=True)

#Création du fond
canvas1.create_image(0, 0, image=back_tk, anchor="nw")

# Placement de la fleche en adaptant sa taille à l'écran
canvas1.create_image(int((taille[0]-taille_fleche[0])), int((taille[1]-taille_fleche[1])/2), image=fleche_tk, anchor="nw")


#Ecriture du texte
canvas1.create_text(taille[0] / 2, taille[1] / 2, text="Veulliez placer votre carte sur la droite", fill="black", font=("Impact", 60))
#canvas1.create_text(taille[0] / 2, taille[1] /1.03, text="Appuyer sur la touche échappe pour annuler", fill="black", font=("Impact", 40))
root.mainloop()