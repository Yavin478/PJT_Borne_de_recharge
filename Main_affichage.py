print("Demarrage 'main_affichage.py'")

class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top=Page(self)
        self.withdraw()
        self.mode="Carte"
        self.sleeping_mode=True
        self.inactivity_refresh(None)
        self.Boucle()

    def inactivity_refresh(self,event):
        self.before = time()
        print("Inactivity Refresh")

    def inactivity_test(self):
        if time()-self.before>4:
            print('reset')
            self.mode="Carte"
            self.sleeping_mode=True
            self.inactivity_refresh(None)


    def Boucle(self):
        if self.sleeping_mode:
            self.sleeping_mode = False
            if self.mode=="Carte":
                self.Carte()
            elif self.mode=="Montant":
                self.Montants()
            elif self.mode=="QR":
                self.QR()
            elif self.mode=="Transaction":
                self.QR_transact()
            elif self.mode=="Error_QR":
                self.Error_QR()
            elif self.mode=="Error_Carte":
                self.Error_carte()
            elif self.mode=="Error_Montant":
                self.Error_montant()
            elif self.mode=="Error_Rezal":
                self.Error_rezal()
            elif self.mode=="Finish":
                self.Finish()
            else:
                print("wrong mode ducon")
            self.inactivity_refresh(None)
        self.inactivity_test()
        self.after(100, self.Boucle)

    def Carte(self):
        print("Demande carte")
        self.top.Page_carte()
        RFID_getUID(self)



    def Check_Carte(self,uid):
        print("carte trouvee")
        print(uid)
        self.UID=STRING_uidStrToInt(uid)
        self.Montants()

        self.mode="Montant"
        self.sleeping_mode = True

    def Montants(self):
        print("Demande Montant")
        self.top.Page_montant(self.argent)

    def Check_montants(self, montant):
        print("Montant trouvé")
        self.montant=int(montant)
        if self.montant>config.maxTransaction/100:
            self.mode="Error_Montant"
        else:
            self.mode="QR"
        self.sleeping_mode = True

    def QR(self):
        print("Recherche QR")
        self.top.Page_QR()

    def QR_check(self,QR):
        print("QR Trouvée")
        try:
            self.QRcode = eval(QR)
            self.mode = "Transaction"
        except:
            self.mode="Error_QR"
        self.sleeping_mode = True

    def QR_transact(self):
        print("Transaction")
        print(self.QRcode)
        print(type(self.QRcode))
        if Transaction_Lydia(box, self.UID, self.montant, self.Qrcode, token_public, phone):
            self.mode="Finish"
        else:
            self.mode="Error_QR"
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

    def rollback(self):
        self.mode = "Carte"
        self.sleeping_mode = True

