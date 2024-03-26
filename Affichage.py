from tkinter import *
from PIL import Image, ImageTk

def affichage_attente_CR(texte):
    canvas1.create_text(taille[0] / 2, taille[1] / 2, text=texte, fill="black", font=("Impact", 40))


root = Tk()

root.title("PAGE")

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.destroy())

taille = (root.winfo_screenwidth(), root.winfo_screenheight())


#back = Image.open("Static/background.png")
back = Image.open("Static/fond.jpg")
back_redimensionnee = back.resize((taille[0], taille[1]))
back_tk = ImageTk.PhotoImage(back_redimensionnee)

taille_carre = [int(taille[0]/1.5), int(taille[1]/1.5)]

#carre = Image.open("Static/joliecarre.png")
carre = Image.open("Static/cadre.png")
carre_redimensionnee = carre.resize((taille_carre[0], taille_carre[1]))
carre_tk = ImageTk.PhotoImage(carre_redimensionnee)

canvas1 = Canvas(root, width=taille[0], height=taille[1])
canvas1.pack(fill="both", expand=True)

canvas1.create_image(0, 0, image=back_tk, anchor="nw")

canvas1.create_image(int(taille[0]-taille_carre[0])/2, int(taille[1]-taille_carre[1])/2, image=carre_tk, anchor="nw")

#affichage_attente_CR()

root.mainloop()

affichage_attente_CR("text1")