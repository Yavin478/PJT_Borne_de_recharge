#AFFICHAGE
from Template_pageV2 import Page
from tkinter import *
from time import sleep

#LYDIA/BDD
from config import *
from prepa_bdd import *
from API_Lydia import *
from finalisation_bdd import *

from Config_Affichage import *



class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top=Page(self)
        self.withdraw()
        self.Carte()

    def Carte(self):
        self.top.Page_carte()

        self.UID=35028059

        self.Montants()

    def Montants(self):
        self.top.Page_montant(self.Check_montants)

    def Check_montants(self, montant):
        self.montant=int(montant)
        if self.montant>max_transaction:
            self.Error_montant()
        else:
            self.QR()

    def QR(self):
        self.top.Page_QR(self.QR_transact)

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

        current_date = SQL_SELECT(QUERRY_getTime())[0][0]
        SQL_EXECUTE(QUERRY_setIdLydia(current_date))

        order_id = SQL_SELECT(QUERRY_getIdLydia(current_date))[0][0]

        transaction_identifier = Lydia_check(token_public, self.montant, phone, order_id, self.QRcode)

        if transaction_identifier:
            montant = self.montant * 100  # en centime pour la bdd
            Recharge_montant(self.UID, montant)
            date_recharge = SQL_SELECT(QUERRY_getTime())[0][0]
            SQL_EXECUTE(QUERRY_setRecharge(self.UID, montant, box, date_recharge))
            id_recharge = SQL_SELECT(QUERRY_getIdRecharge(date_recharge))[0][0]
            SQL_EXECUTE(QUERRY_setTransactionLydia(order_id, id_recharge, transaction_identifier))
            self.Finish()
        else:
            self.Error_QR()

    def Error_QR(self):
        self.top.Page_error_QR()
        sleep(5)
        self.top.Page_carte()

    def Error_carte(self):
        self.top.Page_error_carte()
        sleep(5)
        self.top.Page_carte()

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