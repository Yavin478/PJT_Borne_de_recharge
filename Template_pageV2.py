print("Demarrage 'Template_pageV2.py'")
from Config_Affichage import *

#programmater par le plus bo goss des 222 alias Bercerf'k 57

#wallah j'ai carry Poüllilian
#franco = gay
#Noan traveille???!!!
#Lerats?
#Carmona branle rien (sauf la boulangère 😬)



class Page(Toplevel):

    def __init__(self, master, *args, **kwargs):  # fonction initialisation => création de la page et attributs
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.Setup()
        self.taille_ecran = Size().renvoi()
        self.canvas = Canvas(self, width=self.taille_ecran[0], height=self.taille_ecran[1])
        self.canvas.pack(fill=BOTH, expand=True)
        self.Npage = list(range(2))

        self.BG()
        self.Instruction()
        self.Fleche()

    def Test_page_size(self):
        if self.taille_ecran!=Size().renvoi():
            self.quit_app()
        self.after(4000, self.Test_page_size)


    def Instruction(self):
        self.widget=[]

        self.titre = self.canvas.create_text(self.taille_ecran[0] / 2,
                                             self.taille_ecran[1] / 2 * (1 - (1 - decalage["titre"]) /ratio_square),
                                             anchor="center",
                                             font=(type_police, int(police['titre'] * min(self.taille_ecran) / ratio_square), "bold"),
                                             justify=CENTER)


        self.top = self.canvas.create_text(self.taille_ecran[0] / 2,
                                           self.taille_ecran[1] / 2 * (1 - (1 - decalage["top"]) /ratio_square),
                                           anchor="center",
                                           font=(type_police, int(police['top'] * min(self.taille_ecran) / ratio_square)),
                                           state="hidden",
                                           justify=CENTER)
        self.widget.append(self.top)

        self.bot = self.canvas.create_text(self.taille_ecran[0] / 2,
                                           self.taille_ecran[1] / 2 * (1 + (1 - decalage["bot"]) /ratio_square),
                                           anchor="center",
                                           text=txt_esc,
                                           state="hidden",
                                           font=(type_police, int(police['bot'] * min(self.taille_ecran) / ratio_square)),
                                           justify=CENTER)
        self.widget.append(self.bot)

        self.left = self.canvas.create_text(
            self.taille_ecran[0] / 2 * (1 - (1 - decalage["side"]) /ratio_square),
            self.taille_ecran[1] / 2,
            anchor="center",
            text=txt_indic["montant_in"],
            state="hidden",
            font=(type_police, int(police['side'] * min(self.taille_ecran) / ratio_square)),
            justify=CENTER)
        self.widget.append(self.left)

        self.right = self.canvas.create_text(
            self.taille_ecran[0] / 2 * (1 + (1 - decalage["side"]) /ratio_square),
            self.taille_ecran[1] / 2,
            anchor="center",
            text=txt_indic["montant_out"],
            state="hidden",
            font=(type_police, int(police['side'] * min(self.taille_ecran) / ratio_square)),
            justify=CENTER)
        self.widget.append(self.right)

        self.center = self.canvas.create_text(
            self.taille_ecran[0] / 2,
            self.taille_ecran[1] / 2,
            anchor="center",
            state="hidden",
            font=(type_police, int(police['center'] * min(self.taille_ecran) / ratio_square)),
            justify=CENTER)
        self.widget.append(self.center)

        self.imgtk = {i:self.creator_img(path[i], [self.taille_ecran[1] / ratio_img]*2) for i in ["smiley", "exclam", "cross"]}
        self.img=self.canvas.create_image(self.taille_ecran[0] / 2,
                                          self.taille_ecran[1] / 2 * (1+ decalage["img"] ),
                                          anchor="center")
        self.widget.append(self.img)

    def make_all_img(self):
        self.imgtk=[self.creator_img(path[i],self.taille_ecran/ratio_img) for i in ["smiley","exclam","cross"]]

    def cancel_canvas(self):
        for i in self.widget:
            self.canvas.itemconfig(i, state="hidden")
        self.canvas.itemconfig(self.bot, text=txt_esc)


        self.unbind("<KeyPress>")

        self.QR = ""
        self.montant = ""
        self.fleche_active = False
        self.flag = False
        self.compteur = 0

    def Page_carte(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["carte"])
        self.canvas.itemconfig(self.center, state="normal", text=txt_presentation)
        self.canvas.coords(self.fleche, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche["carte"] - self.taille_fleche[1] / 2)])
        self.fleche_active = True


    def Page_montant(self,inmo):
        self.cancel_canvas()
        self.dico={"&":1, "é":2, '"':3, "'":4, "(":5, "-":6, "è":7, "_":8, "ç":9, "à":0}

        def keypress(event):
            if event.keysym == "BackSpace":
                self.montant = ""
                update_text()
            elif event.keysym == "Return":
                self.master.Check_montants(self.montant)
            elif event.char in self.dico.keys():
                self.montant += str(self.dico[event.char])
                if len(self.montant) > len(str(config.maxTransaction // 100)):
                    self.montant = self.montant[1:]
                update_text()

        # actualisation du texte taper au fur et à mesure ainsi que du canva qui l'affiche
        def update_text():
            montant_texte = txt_indic["montant_out"] + self.montant + " \u20AC"  # Ajoute le symbole de l'euro au texte
            self.canvas.itemconfig(self.right, text=montant_texte)

        self.canvas.itemconfig(self.titre, text=txt_titre["montant"])
        self.canvas.itemconfig(self.bot, state="normal")
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["montant"])
        self.canvas.itemconfig(self.left, state="normal", text=txt_indic["montant_in"] + str(inmo) + " \u20AC")
        self.canvas.itemconfig(self.right, state="normal", text=txt_indic["montant_out"])
        self.canvas.coords(self.fleche, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche["montant"] - self.taille_fleche[1] / 2)])

        self.bind("<KeyPress>", keypress, add='+')
        self.fleche_active = True

    def Page_QR(self):
        self.cancel_canvas()

        def keypress(event):
            if event.keysym == "Return":
                self.flag = True
                self.master.QR_check(self.QR)
            else:
                self.QR += str(event.char)
        self.canvas.itemconfig(self.titre, text=txt_titre["Qr"])
        self.canvas.itemconfig(self.bot, state="normal")
        self.canvas.coords(self.fleche, [int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
                                             int(self.taille_ecran[1] * h_fleche["QR"] - self.taille_fleche[1] / 2)])
        self.fleche_active = True
        self.bind('<KeyPress>', keypress, add='+')

    def Page_confirmation(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["terminée"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["terminée"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['smiley'])
        self.canvas.itemconfig(self.bot, state="normal", text=txt_indic["quitter"])


    def Page_error_QR(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_QR"])
        self.canvas.itemconfig(self.top, state='normal', text=txt_indic["error_QR"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

    def Page_error_montant(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_montant"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["error_montant"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

    def Page_error_carte(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_carte"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["error_carte"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

    def Page_error_rezal(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_rezal"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["error_rezal"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

    def Page_error_matos(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_matos"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["error_rezal"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

    def Page_error_no_carte(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["annulée"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["no_card"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['cross'])


    def Fleche(self):
        self.taille_fleche = [int(self.taille_ecran[0] / ratio_flèche), int(self.taille_ecran[1] / ratio_flèche)]
        self.fleche_img=self.creator_img(path["fleche"],self.taille_fleche)
        self.fleche = self.canvas.create_image(
            int((self.taille_ecran[0] - self.taille_fleche[0] - décalage_flèche)),
            int(self.taille_ecran[1] * h_fleche["carte"] - self.taille_fleche[1] / 2),
            image=self.fleche_img, anchor="nw")
        self.fleche_active = False
        self.toggle_visibility()

    def toggle_visibility(self):
        if self.canvas.itemcget(self.fleche, "state") == "hidden" and self.fleche_active:
            self.canvas.itemconfigure(self.fleche, state="normal")
        else:
            self.canvas.itemconfigure(self.fleche, state="hidden")
        self.after(500, self.toggle_visibility)

    def BG(self):
        bg = self.resize_img(path['bg'], self.taille_ecran)
        fg = self.resize_img(path['fg'], [i / ratio_square for i in self.taille_ecran])
        bg.paste(fg, [int(i / 2 * (1 - 1 / ratio_square)) for i in self.taille_ecran], fg)
        self.bg_tked = ImageTk.PhotoImage(bg)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg_tked)

    def resize_img(self, path, dim):
        img = Image.open(path)
        img_resized = img.resize((int(dim[0]), int(dim[1])))
        return img_resized

    def creator_img(self, path, dim):
        img = self.resize_img(path, dim)
        img_tk = ImageTk.PhotoImage(img)
        return img_tk

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

