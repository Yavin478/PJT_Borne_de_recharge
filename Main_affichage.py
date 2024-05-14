print("Demarrage 'main_affichage.py'")

from Template_pageV2 import *

class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top = Page(self)
        self.withdraw()
        self.mode="Carte"
        self.sleeping_mode=True
        self.L_presence_card=[]
        self.Verif_Rezal=60
        self.Boucle()


    def Carte_test(self):
        self.L_presence_card.append(RFID_presence())
        if len(self.L_presence_card)>3:
            if not (True in self.L_presence_card[1:]):
                print("No RFID presence")
                self.mode = "No_card"
                self.sleeping_mode = True
                self.L_presence_card = []


    def Boucle(self):

        if self.Verif_Rezal(self):
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
                print("MODE : "+self.mode)

            if self.mode in ["Montant", "QR", "Transaction"]:
                self.Carte_test()

        self.after(100, self.Boucle)

    def Verif_Rezal(self):
        if self.Verif_Rezal>=60:   # Toutes les 60 secondes
            print("Vérif Rezal :",self.Verif_Rezal)
            self.Verif_Rezal=0
            self.Test_Rezal()

        self.Verif_Rezal += 1
        if (setting.rezalOn and setting.rezalNet):
            print("Rezal On :",setting.rezalOn)
            print("Rezal Net :", setting.rezalNet)
            return True
        else :
            return False

    def Test_Rezal(self):      # Mode de vérification du réseau
        try :
            if REZAL_pingServeur():  # Ping du serveur guinche pour s'assurer que la connection locale est toujours présente
                print("Connection à la BDD OK")
                DATA_setVariable("rezalOn", bool(REZAL_pingServeur()))
                if REZAL_pingInternet(): # Ping du serveur google pour s'assurer que la connection internet est toujours présente
                    print("Connection à internet OK")
                    DATA_setVariable("rezalNet", bool(REZAL_pingInternet()))
                    return None
                else :
                    print("La connection au serveur google a échoué")
                    DATA_setVariable("rezalNet", bool(False))
                    return None
            else:
                print("La connection au serveur Guinche a échoué")
                DATA_setVariable("rezalOn", bool(False))
                return None

        except Exception as e :
            print("Erreur de réseau : ",e)
            DATA_setVariable("rezalOn", bool(False))
            DATA_setVariable("rezalNet", bool(False))
            return None

    def Carte(self):
        self.top.Page_carte()
        RFID_getUID(self)


    def Check_Carte(self,uidstring):
        self.uidstring=uidstring
        self.UID=STRING_uidStrToInt(uidstring)
        print("UID check :", self.UID)

        if len(SQL_SELECT(QUERRY_getCarte(self.UID)))==0:    #test si la carte est déjà présente dans la bdd
            SQL_EXECUTE(QUERRY_addCarte(self.UID))

        self.argent=SQL_SELECT(QUERRY_getMoney(self.UID))[0][0]/100  #Pour convertir le montant en euros

        self.mode = "Montant"
        self.sleeping_mode = True

    def Montants(self):
        self.top.Page_montant(self.argent)

    def Check_montants(self, montant):
        print("Montant trouvé")
        self.montant=int(montant)
        if self.montant>config.maxTransaction/100 or (self.montant+self.argent)>config.maxMontant/100 or self.montant==0:   #Vérifie le montant de la recharge
            self.mode="Error_Montant"
        else:
            self.mode = "QR"
        self.sleeping_mode = True

    def QR(self):
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
        print(self.QRcode)
        print(type(self.QRcode))
        if Transaction_Lydia(setting.numeroBox, self.UID, self.montant, self.QRcode, token_public, phone):
            RFID_setArgent(int((self.montant+self.argent)*100),self.uidstring)               # Ecriture du nouveau montant sur la carte RFID
            self.mode="Finish"
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

