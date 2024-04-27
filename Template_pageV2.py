from tkinter import *
from PIL import Image, ImageTk
from Constante import *


class Page(Toplevel):

    def __init__(self, *args, **kwargs):  # fonction initialisation => création de la page et attributs
        super().__init__(*args, **kwargs)
        self.Setup()
        self.taille_ecran = Size().renvoi()
        self.canvas = Canvas(self, width=self.taille_ecran[0], height=self.taille_ecran[1])
        self.canvas.pack(fill=BOTH, expand=True)
        self.Npage = list(range(2))

        self.BG()
        self.Instruction()
        self.Fleche()

    def Instruction(self):
        self.titre = self.canvas.create_text(self.taille_ecran[0] / 2,
                                             self.taille_ecran[1] / 2 * (1 - decalage_label / ratio_square), anchor="n",
                                             font=(type_police, int(taille_police / ratio_square)))

        self.indic = self.canvas.create_text(self.taille_ecran[0] / 2,
                                             self.taille_ecran[1] / 2, anchor="center",
                                             font=(type_police, int(taille_police / ratio_square)),
                                             state="hidden")

        self.esc = self.canvas.create_text(self.taille_ecran[0] / 2,
                                           self.taille_ecran[1] / 2 * (1 + decalage_label_esc / ratio_square),
                                           anchor="n",
                                           text="Appuyez sur ESC pour annuler",
                                           state="hidden",
                                           font=(type_police, int(taille_police_esc / ratio_square)))


    def Page_carte(self):
        self.montant=""
        self.canvas.itemconfig(self.titre, text=txt_titre["carte"])
        self.canvas.itemconfig(self.esc, state="normal")
        self.canvas.itemconfig(self.indic, state="hidden")
        self.canvas.coords(self.fleche_img, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche[0] - self.taille_fleche[1] / 2)])
        self.fleche_active = True

    def Page_montant(self,callback):
        self.montant=""
        self.montant_conf=False

        def keypress(event):
            if event.keysym=="BackSpace":
                self.montant=""
            elif event.keysym=="Return":
                callback(self.montant)
            else:
                self.montant += event.char
            update_text()

        # actualisation du texte taper au fur et à mesure ainsi que du canva qui l'affiche
        def update_text():
            montant_texte = self.montant + " \u20AC"  # Ajoute le symbole de l'euro au texte
            self.canvas.itemconfig(self.indic, text=montant_texte)

        self.canvas.itemconfig(self.titre, text=txt_titre["montant"])
        self.canvas.itemconfig(self.esc, state="normal")
        self.canvas.itemconfig(self.indic, state="normal", text=self.montant)
        self.canvas.coords(self.fleche_img, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche[2] - self.taille_fleche[1] / 2)])
        self.bind("<KeyPress>", keypress)
        self.fleche_active = True

    def Page_QR(self,callback):

        def keypress(event):
            if event.keysym == "Return":
                callback(self.QR)
            else:
                self.QR += str(event.char)

        self.QR=""

        self.canvas.itemconfig(self.indic, state="hidden")
        self.unbind("<KeyPress>")
        self.canvas.itemconfig(self.titre, text=txt_titre["Qr"])
        self.canvas.itemconfig(self.esc, state="normal")
        self.canvas.coords(self.fleche_img, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche[1] - self.taille_fleche[1] / 2)])
        self.fleche_active = True
        self.bind('<KeyPress>', keypress)




    def Page_confirmation(self):
        self.canvas.itemconfig(self.titre, text=txt_titre["terminée"])
        self.canvas.itemconfig(self.esc, state="hidden")
        self.fleche_active = False

    def Page_error(self):
        self.canvas.itemconfig(self.titre, text=txt_titre["error"])
        self.canvas.itemconfig(self.esc, state="hidden")
        self.fleche_active = False

    def Page_error(self):
        self.canvas.itemconfig(self.titre, text=txt_titre["error"][0])
        self.canvas.itemconfig(self.esc, state="hidden")
        self.fleche_active = False

    def Page_error_rezal(self):
        self.canvas.itemconfig(self.titre, text=txt_titre["error_rezal"])
        self.canvas.itemconfig(self.esc, state="hidden")
        self.fleche_active = False

    def Fleche(self):
        fleche = Image.open("Static/fleche.png")
        self.taille_fleche = [int(self.taille_ecran[0] / ratio_flèche), int(self.taille_ecran[1] / ratio_flèche)]
        fleche_redimensionnee = fleche.resize((self.taille_fleche[0], self.taille_fleche[1]))
        self.fleche_tk = ImageTk.PhotoImage(fleche_redimensionnee)
        self.fleche_img = self.canvas.create_image(
            int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
            int(self.taille_ecran[1] * h_fleche[0] - self.taille_fleche[1] / 2),
            image=self.fleche_tk, anchor="nw")
        self.fleche_active = False
        self.toggle_visibility()

    def toggle_visibility(self):
        if self.canvas.itemcget(self.fleche_img, "state") == "hidden" and self.fleche_active:
            self.canvas.itemconfigure(self.fleche_img, state="normal")
        else:
            self.canvas.itemconfigure(self.fleche_img, state="hidden")
        self.after(500, self.toggle_visibility)

    def BG(self):
        bg = self.resize_img(path_img_bg, self.taille_ecran)
        fg = self.resize_img(path_img_fg, [i / ratio_square for i in self.taille_ecran])
        bg.paste(fg, [int(i / 2 * (1 - 1 / ratio_square)) for i in self.taille_ecran], fg)
        self.bg_tked = ImageTk.PhotoImage(bg)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg_tked)

    def resize_img(self, path, dim):
        img = Image.open(path)
        img_resized = img.resize((int(dim[0]), int(dim[1])))
        return img_resized

    def Setup(self):
        self.title("Page")
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.quit_app())

        def callback(text):
            print(text)

        self.bind('<Key-a>', lambda e: self.Page_carte())
        self.bind('<Key-z>', lambda e: self.Page_montant(callback))
        self.bind('<Key-e>', lambda e: self.Page_QR(callback))
        self.bind('<Key-r>', lambda e: self.Page_confirmation())

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
