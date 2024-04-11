from tkinter import *
from PIL import Image, ImageTk
from Constante import *


class Page(Toplevel):

    # Mise en page ou appel de fonction

    def __init__(self, *args, **kwargs):  # fonction initialisation => création de la page et attributs
        super().__init__(*args, **kwargs)
        self.setup()
        self.images = []
        self.label = []
        self.taille_ecran = Size().renvoi()
        self.canv = Canvas(self, width=self.taille_ecran[0], height=self.taille_ecran[1])
        self.canvas()

    def setup(self):
        self.title("Page")
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.quit_app())

    def canvas(self):  # création du canvas + ajout widgets
        self.canv.pack()
        self.create_img(self.taille_ecran, path_img_bg)
        self.create_img([i / ratio_square for i in self.taille_ecran], path_img_fg, [i / 2 for i in self.taille_ecran], "center")
        self.create_label("salut!",pos=[self.taille_ecran[0]/2,self.taille_ecran[1]/2*(1-decalage_label/ratio_square)], ancre="n")

        # FONCTION DE CREATION

    def create_img(self, taille, path, pos=(0, 0), ancre="nw"):
        photo_image = self.resize_img(path, taille)
        self.images.append(photo_image)
        self.canv.create_image(pos[0], pos[1], anchor=ancre, image=photo_image)

    def create_label(self, text, police=type_police, pos=(0, 0), ancre="Center", taille=taille_police):
        self.canv.create_text(pos[0], pos[1], anchor=ancre, text=text, font=(police, int(taille/ratio_square)))

        # FONCTION UTILITAIRE

    def resize_img(self, path, dim):  # fonction d'importation d'image et redimensionnement
        img = Image.open(path)
        img_resized = img.resize((int(dim[0]), int(dim[1])))
        img_tked = ImageTk.PhotoImage(img_resized)
        return img_tked


    def quit_app(self):
        self.master.destroy()


class Size:

    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.root.attributes("-fullscreen", True)

    def renvoi(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.destroy()
        return width, height


if __name__ == '__main__':  # lancement du programme
    root = Tk()
    app = Page(root)
    root.withdraw()
    root.mainloop()
