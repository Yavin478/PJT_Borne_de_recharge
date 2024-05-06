from tkinter import *
from PIL import Image, ImageTk

#création de page
root = Tk()
root.title("PAGE")
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.destroy())

taille = (root.winfo_screenwidth(), root.winfo_screenheight())

#importation de l'image de fond et redimensionnement
back = Image.open("Static/Bg_508.jpg")
back_redimensionnee = back.resize((taille[0], taille[1]))
back_tk = ImageTk.PhotoImage(back_redimensionnee)




#importation de la flèche de fond et redimensionnement
fleche = Image.open("Static/fleche.png")
taille_fleche = [int(taille[0]/ 7), int(taille[1]/ 8)]
fleche_redimensionnee = fleche.resize((taille_fleche[0],taille_fleche[1]))
fleche_tk = ImageTk.PhotoImage(fleche_redimensionnee)

#création du canva de fond associé

canvas_background = Canvas(root, width=taille[0], height=taille[1])
canvas1 = Canvas(root, width=taille[0], height=taille[1])
canvas_background.place(x=0, y=0)
canvas1.place(x=0, y=0)


canvas_background.create_image(0, 0, image=back_tk, anchor="nw")
def toggle_visibility(): #fonction permmettant le cligonetement de la flèche
    if canvas1.itemcget(fleche_img, "state") == "hidden":
        canvas1.itemconfigure(fleche_img, state="normal")
    else:
        canvas1.itemconfigure(fleche_img, state="hidden")
    root.after(500, toggle_visibility)  # Changez ici le délai entre les clignotements en millisecondes

#création du canva de la flèche
fleche_img=canvas1.create_image(int((taille[0]-taille_fleche[0])), int((taille_fleche[1])/2), image=fleche_tk, anchor="nw")
toggle_visibility()  # Démarre le clignotement au lancement

#Création du texte
canvas1.create_text(taille[0] / 2, taille[1] / 2, text="Présenter un QR Code LYDIA", fill="black", font=("Impact", 60))
canvas1.create_text(taille[0] / 2, taille[1] /1.03, text="Echap pour annuler", fill="black", font=("Impact", 40))
root.mainloop()