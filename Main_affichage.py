# AFFICHAGE
from Template_pageV2 import Page
from tkinter import *
from config_lydia import *

# LYDIA/BDD
from config import *
from main_lydia import *


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top = Page(self)
        self.withdraw()
        self.mode = "Carte"
        self.sleeping_mode = True
        self.L_presence_card = []
        self.Boucle()

    '''def Carte_test(self):
        self.L_presence_card.append(RFID_presence())
        if len(self.L_presence_card) > 3:
            self.L_presence_card = self.L_presence_card[1:]

        if not (True in self.L_presence_card):
            print("No RFID presence")
            self.mode = "No_card"
            self.sleeping_mode = True'''

    def Boucle(self):
        if self.sleeping_mode:
            self.sleeping_mode = False
            if self.mode == "Carte":
                self.Carte()
            elif self.mode == "Montant":
                self.Montants()
            elif self.mode == "QR":
                self.QR()
            elif self.mode == "Transaction":
                self.QR_transact()
            elif self.mode == "Error_QR":
                self.Error_QR()
            elif self.mode == "Error_Carte":
                self.Error_carte()
            elif self.mode == "Error_Montant":
                self.Error_montant()
            elif self.mode == "Error_Rezal":
                self.Error_rezal()
            elif self.mode == "Finish":
                self.Finish()
            elif self.mode == "No_card":
                self.Error_no_carte()
            else:
                print("wrong mode ducon")
            print("MODE : " + self.mode)

        if self.mode in ["Montant", "QR", "Transaction"]:
            self.Carte_test()

        self.after(100, self.Boucle)

    def Carte(self):
        print("Demande carte")
        self.top.Page_carte()

        self.UID = 0

        self.argent = 30

        print("carte trouvé")

        self.mode = "Montant"
        self.sleeping_mode = True

    def Montants(self):
        print("Demande Montant")
        self.top.Page_montant(self.argent)

    def Check_montants(self, montant):
        print("Montant trouvé")
        self.montant = int(montant)
        if self.montant > config.maxTransaction / 100 or (
                self.montant + self.argent) > config.maxMontant / 100 or self.montant == 0:  # Vérifie le montant de la recharge
            self.mode = "Error_Montant"
        else:
            self.mode = "QR"
        self.sleeping_mode = True

    def QR(self):
        print("Recherche QR")
        self.top.Page_QR()

    def QR_check(self, QR):
        print("QR Trouvée")
        try:
            self.QRcode = eval(QR)
            self.mode = "Transaction"
        except:
            self.mode = "Error_QR"
        self.sleeping_mode = True

    def QR_transact(self):
        print("Transaction")
        print(self.QRcode)
        print(type(self.QRcode))
        if Transaction_Lydia(box, self.UID, self.montant, self.Qrcode, token_public, phone):
            self.mode = "Finish"
        else:
            self.mode = "Error_QR"
        self.sleeping_mode = True

    def Error_QR(self):
        self.top.Page_error_QR()
        self.after(5000, self.rollback)

    def Error_carte(self):
        self.top.Page_error_carte()
        self.after(5000, self.rollback)

    def Error_montant(self):
        self.top.Page_error_montant()
        self.after(5000, self.rollback)

    def Error_rezal(self):
        self.top.Page_error_rezal()
        self.after(5000, self.rollback)

    def Finish(self):
        self.top.Page_confirmation()
        self.after(5000, self.rollback)

    def Error_no_carte(self):
        self.top.Page_error_no_carte()
        self.after(5000, self.rollback)

    def Annulée(self):
        self.top.Page_annulée()
        self.after(5000, self.rollback)

    def rollback(self):
        self.mode = "Carte"
        self.sleeping_mode = True


if __name__ == "__main__":
    root = MainApp()
    root.mainloop()
