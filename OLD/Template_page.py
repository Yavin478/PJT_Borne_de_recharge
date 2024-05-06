from tkinter import *
from PIL import Image, ImageTk
from Config_Affichage import *


class Page(Toplevel):

    # Mise en page ou appel de fonction

    def __init__(self, *args, **kwargs):  # fonction initialisation => création de la page et attributs
        super().__init__(*args, **kwargs)
        self.Setup()
        self.canvas=[]
        self.taille_ecran = Size().renvoi()
        self.Default_Canvas()
        self.Canvas1()

    def Setup(self):
        self.title("Page")
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.quit_app())

    class canvas_class(Canvas):
        def __init__(self, master, type=None, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            self.master.Close_Canvas()
            if type==None:
                master.canvas.append(self)
            self.configure(self, width=self.master.taille_ecran[0], height=self.master.taille_ecran[1])
            self.widget=[]
            self.pack(fill=BOTH, expand=True)

        def create_img(self, taille, path, pos=(0, 0), ancre="nw"):
            photo_image = self.resize_img(path, taille)
            self.widget.append(photo_image)
            self.create_image(pos[0], pos[1], anchor=ancre, image=photo_image)

        def create_label_titre(self, text, police=type_police, pos=(0, 0), ancre="Center", taille=taille_police):
            self.create_text(pos[0], pos[1], anchor=ancre, text=text, font=(police, int(taille / ratio_square)))

        def resize_img(self, path, dim):  # fonction d'importation d'image et redimensionnement
            img = Image.open(path)
            img_resized = img.resize((int(dim[0]), int(dim[1])))
            img_tked = ImageTk.PhotoImage(img_resized)
            return img_tked


    def Default_Canvas(self):  # création du canvas + ajout widgets
        self.default_canvas = self.canvas_class(self,"BG")
        self.default_canvas.create_img(self.taille_ecran, path_img_bg)
        self.default_canvas.create_img([i / ratio_square for i in self.taille_ecran], path_img_fg, [i / 2 for i in self.taille_ecran], "center")

    def Canvas1(self):
        self.canvas1 = self.canvas_class(self)
        print("oub")
        self.canvas1.create_label_titre("salut!",pos=[self.taille_ecran[0]/2,self.taille_ecran[1]/2*(1-decalage_label/ratio_square)], ancre="n")

    def Canvas2(self):
        self.canvas2 = self.canvas_class(self)
        self.canvas2.create_label_titre("aurevoir!",pos=[self.taille_ecran[0]/2,self.taille_ecran[1]/2*(1-decalage_label/ratio_square)], ancre="n")

    def Close_Canvas(self):
        for i in self.canvas:
            if i.winfo_manager():
                i.pack_forget()

        # FONCTION DE CREATION


        # FONCTION UTILITAIRE

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
