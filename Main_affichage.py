class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top=Page(self)
        self.withdraw()
        self.Carte()

    def Carte(self):
        print("recherche carte")
        self.top.Page_carte()
        STRING_uidStrToInt(RFID_getUID(self))



    def Check_Carte(self,uid):
        print("carte reçu")
        print(uid)
        self.UID=STRING_uidStrToInt(uid)
        self.Montants()

    def Montants(self):
        print("demande montant")
        self.top.Page_montant()

    def Check_montants(self, montant):
        print("vérif motant")
        print(montant)
        self.montant=int(montant)
        if self.montant>config.maxTransaction/100:
            self.Error_montant()
        else:
            self.QR()

    def QR(self):
        print("demande QR_code")
        self.top.Page_QR()

    def QR_check(self,QR):
        print("vérif QR_code")
        print(QR)
        flag=True
        try:
            self.QRcode = eval(QR)
        except:
            flag=False
        if flag:
            print("QR:")
            print(self.QRcode)
            self.QR_transact()
        else:
            print("erreur QR code1")
            self.Error_QR()

    def QR_transact(self):
        if Transaction_Lydia(box, self.UID, self.montant, self.QRcode, token_public, phone):
            self.Finish()
        else:
            print("erreur QR code2")
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
