from Template_pageV2 import Page
from Recup_Qr import QR_seeker
from tkinter import *


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top=Page(self)
        self.withdraw()
        self.Carte()

    def Carte(self):
        self.top.Page_carte()

        self.Montants()

    def Montants(self):
        self.top.Page_montant(self.QR)

    def QR(self, montant):
        self.montant=montant
        self.top.Page_QR(self.récup_QR)
        print("yo")

    def récup_QR(self, QR):
        self.QRcode=QR







if __name__ == "__main__":
    root=MainApp()
    root.mainloop()