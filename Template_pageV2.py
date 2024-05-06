from tkinter import *
from PIL import Image, ImageTk
from Config_Affichage import *

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
                                             font=(type_police, int(taille_police / ratio_square)),
                                             justify = CENTER)

        self.indic = self.canvas.create_text(self.taille_ecran[0] / 2,
                                             self.taille_ecran[1] / 2, anchor="center",
                                             font=(type_police, int(taille_police_indic / ratio_square)),
                                             state="hidden",
                                             justify = CENTER)

        self.esc = self.canvas.create_text(self.taille_ecran[0] / 2,
                                           self.taille_ecran[1] / 2 * (1 + decalage_label_esc / ratio_square),
                                           anchor="n",
                                           text="Appuyez sur ESC pour annuler",
                                           state="hidden",
                                           font=(type_police, int(taille_police_esc / ratio_square)),
                                           justify = CENTER)

    def cancel_canvas(self):
        self.canvas.itemconfig(self.indic, state="hidden")
        self.canvas.itemconfig(self.esc, state="hidden")
        self.unbind("<KeyPress>")
        self.QR = ""
        self.montant=""
        self.fleche_active = False


    def Page_carte(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["carte"])
        self.canvas.coords(self.fleche_img, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche["carte"] - self.taille_fleche[1] / 2)])
        self.fleche_active = True

    def Page_montant(self,callback):
        self.cancel_canvas()

        def keypress(event):
            if event.keysym=="BackSpace":
                self.montant=""
                update_text()
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
                                             int(self.taille_ecran[1] * h_fleche["montant"] - self.taille_fleche[1] / 2)])
        self.bind("<KeyPress>", keypress)
        self.fleche_active = True

    def Page_QR(self,callback):
        self.cancel_canvas()

        def keypress(event):
            if event.keysym == "Return":
                callback(self.QR)
            else:
                self.QR += str(event.char)


        self.canvas.itemconfig(self.titre, text=txt_titre["Qr"])
        self.canvas.itemconfig(self.esc, state="normal")
        self.canvas.coords(self.fleche_img, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche["QR"] - self.taille_fleche[1] / 2)])
        self.fleche_active = True
        self.bind('<KeyPress>', keypress)

    def Page_confirmation(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["terminée"])
        self.canvas.itemconfig(self.indic, state="normal", text=txt_indic["terminée"])

    def Page_error_QR(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_QR"])
        self.canvas.itemconfig(self.indic, text=txt_indic["error_QR"])

    def Page_error_montant(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_montant"])
        self.canvas.itemconfig(self.indic, text=txt_indic["error_montant"])
        self.canvas.itemconfig(self.indic, state="normal")

    def Page_error_carte(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_carte"])
        self.canvas.itemconfig(self.indic, state="normal", text=txt_indic["error_carte"])

    def Page_error_rezal(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_rezal"])
        self.canvas.itemconfig(self.indic, state="normal", text=txt_indic["error_rezal"])

    def Fleche(self):
        fleche = Image.open("Static/fleche.png")
        self.taille_fleche = [int(self.taille_ecran[0] / ratio_flèche), int(self.taille_ecran[1] / ratio_flèche)]
        fleche_redimensionnee = fleche.resize((self.taille_fleche[0], self.taille_fleche[1]))
        self.fleche_tk = ImageTk.PhotoImage(fleche_redimensionnee)
        self.fleche_img = self.canvas.create_image(
            int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
            int(self.taille_ecran[1] * h_fleche["carte"] - self.taille_fleche[1] / 2),
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

    def callback(text):
        print(text)

    def binding(top):
        top.bind('<Key-a>', lambda e: top.Page_carte())
        top.bind('<Key-z>', lambda e: top.Page_montant(callback))
        top.bind('<Key-e>', lambda e: top.Page_QR(callback))
        top.bind('<Key-r>', lambda e: top.Page_confirmation())
        top.bind('<Key-t>', lambda e: top.Page_error_QR())
        top.bind('<Key-y>', lambda e: top.Page_error_carte())
        top.bind('<Key-u>', lambda e: top.Page_error_montant())
        top.bind('<Key-i>', lambda e: top.Page_error_rezal())


    root = Tk()
    app = Page(root)
    binding(app)
    root.withdraw()
    root.mainloop()
