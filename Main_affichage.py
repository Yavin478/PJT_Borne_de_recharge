#AFFICHAGE
from Template_pageV2 import Page
from tkinter import *
from time import *
from config import*


from config_lydia import *

#LYDIA/BDD
from config import *

from main_lydia import *
from STRING import*



class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top=Page(self)
        self.withdraw()
        self.Carte()

    def Carte(self):
        self.top.Page_carte()

        self.UID=0

        self.argent=30

        self.Montants()

    def Montants(self):
        self.top.Page_montant()

    def Check_montants(self, montant):
        self.montant=int(montant)
        if self.montant>config.maxTransaction/100:
            self.Error_montant()
        else:
            self.QR()

    def QR(self):
        self.top.Page_QR()

    def QR_check(self,QR):
        flag=True
        try:
            self.QRcode = eval(QR)
        except:
            flag=False
        if flag:
            self.QR_transact()
        else:
            self.Error_QR()

    def QR_transact(self):
        print(self.QRcode)
        print(type(self.QRcode))
        if Transaction_Lydia(box, self.UID, self.montant, self.Qrcode, token_public, phone):
            self.Finish()
        else:
            self.Error_QR()

    def Error_QR(self):
        self.top.Page_error_QR()
        self.after(5000, self.Carte)

    def Error_carte(self):
        self.top.Page_error_carte()
        self.after(5000, self.Carte)

    def Error_montant(self):
        self.top.Page_error_montant()
        self.after(5000, self.Carte)

    def Error_rezal(self):
        self.top.Page_error_rezal()

    def Finish(self):
        self.top.Page_confirmation()
        self.after(5000, self.Carte)



if __name__ == "__main__":
    root=MainApp()
    root.mainloop()