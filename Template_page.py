from tkinter import *
from PIL import Image, ImageTk

# constants/path
path_img_bg = "Static/Bg_Bapt'ss.png"
path_img_fg = "Static/Cadre_Bapt'ss.png"

ratio_square = 1.5


class Page(Tk):

    # Mise en page ou appel de fonction

    def __init__(self):  # fonction initialisation => création de la page et attributs
        Tk.__init__(self)
        self.setup()
        self.images = []
        self.canv = Canvas(self, width=taille_ecran[0], height=taille_ecran[1])
        self.canvas()

    def setup(self):
        self.title("Page")
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.destroy())

    def canvas(self):  # création du canvas + ajout widgets
        self.canv.pack()
        self.create_img(taille_ecran, path_img_bg)
        self.create_img([i/ratio_square for i in taille_ecran], path_img_fg, centre=True)

        # FONCTION DE CREATION

    def create_img(self, taille, path, pos=(0, 0), centre=False):
        if centre:
            pos=[int(taille_ecran[i]-taille[i])/2 for i in range(2)]

        photo_image = self.resize_img(path, taille)
        self.images.append(photo_image)  # Conserver une référence à l'image
        self.canv.create_image(pos[0], pos[1], anchor="nw", image=photo_image)

        # FONCTION UTILITAIRE


    def resize_img(self, path, dim):  # fonction d'importation d'image et redimensionnement
        img = Image.open(path)
        img_resized = img.resize((int(dim[0]), int(dim[1])))
        img_tked = ImageTk.PhotoImage(img_resized)
        return img_tked


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
    taille_ecran=Size().renvoi()
    page = Page()
    page.mainloop()
