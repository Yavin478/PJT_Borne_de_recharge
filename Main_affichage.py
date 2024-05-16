print("Demarrage 'main_affichage.py'")

from Template_pageV2 import *


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top = Page(self)
        self.withdraw()
        self.mode = "Carte"
        self.sleeping_mode = True
        self.L_presence_card = []
        self.Boucle()

    def Carte_test(self):
        self.L_presence_card.append(RFID_presence())
        if len(self.L_presence_card) > 3 and self.mode!="No_card":
            print("Liste :",self.L_presence_card)
            if not (True in self.L_presence_card[1:]):
                print("No RFID presence")
                if self.mode=="Finish":
                    self.mode = "Carte"
                else:
                    self.mode = "No_card"
                self.sleeping_mode = True
            self.L_presence_card = []


    def Boucle(self):
        if self.sleeping_mode:
            if self.Verif_Rezal():
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
                elif self.mode == "Error_Matos":
                    self.Error_matos()
                elif self.mode == "Finish":
                    self.Finish()
                elif self.mode == "No_card":
                    self.Error_no_carte()
                else:
                    print("wrong mode ducon")
                Entrer_log(setting.projet_path, "Logs", "MODE : "+ str(self.mode))
                print("MODE : " + self.mode)
            else :
                print("error plus de coo")
                self.Error_rezal()


        if self.mode in ["Montant", "QR", "Transaction","Finish"]:
            self.Carte_test()

        self.after(100, self.Boucle)

    def Verif_Rezal(self):
        Entrer_log(setting.projet_path,"Logs" , "Test des connections")

        self.Test_Rezal()
        if (setting.rezalOn and setting.rezalNet):
            Entrer_log(setting.projet_path, "Logs", "Connections établies avec succès")
            return True
        else:
            Entrer_log(setting.projet_path, "Logs", "Connections non établies")
            return False

    def Test_Rezal(self):  # Mode de vérification du réseau
        try:
            if REZAL_pingServeur():  # Ping du serveur guinche pour s'assurer que la connection locale est toujours présente
                Entrer_log(setting.projet_path, "Logs", "Connection à la BDD OK")
                DATA_setVariable("rezalOn", bool(REZAL_pingServeur()))
                if REZAL_pingInternet():  # Ping du serveur google pour s'assurer que la connection internet est toujours présente
                    Entrer_log(setting.projet_path, "Logs", "Connection à internet OK")
                    DATA_setVariable("rezalNet", bool(REZAL_pingInternet()))
                    return None
                else:
                    Entrer_log(setting.projet_path, "Logs", "La connection au serveur google a échoué")
                    DATA_setVariable("rezalNet", bool(False))
                    return None
            else:
                Entrer_log(setting.projet_path, "Logs", "La connection au serveur Guinche a échoué")
                DATA_setVariable("rezalOn", bool(False))
                return None

        except Exception as e:
            Entrer_log(setting.projet_path, "Logs", str(e))
            DATA_setVariable("rezalOn", bool(False))
            DATA_setVariable("rezalNet", bool(False))
            return None

    def Carte(self):

        self.top.Page_carte()
        RFID_getUID(self)

    def Check_Carte(self, uidstring):
        self.uidstring = uidstring
        self.UID = STRING_uidStrToInt(uidstring)
        Entrer_log(setting.projet_path, "Logs", "UID d'une carte détectée : "+str(self.UID))

        if len(SQL_SELECT(QUERRY_getCarte(self.UID))) == 0:  # test si la carte est déjà présente dans la bdd
            SQL_EXECUTE(QUERRY_addCarte(self.UID))

        self.argent = SQL_SELECT(QUERRY_getMoney(self.UID))[0][0] / 100  # Pour convertir le montant en euros
        Entrer_log(setting.projet_path, "Logs", "Argent sur la carte : " + str(self.argent))

        self.mode = "Montant"
        self.sleeping_mode = True

    def Montants(self):
        if command_usb('keyboard','enable') and command_usb('scan','disable'):
            self.top.Page_montant(self.argent)
        else:
            self.mode = "Error_Matos"
            self.sleeping_mode = True


    def Check_montants(self, montant):
        self.montant = int(montant)
        Entrer_log(setting.projet_path, "Logs", "Montant de la recharge trouvé : " + str(self.montant))
        if self.montant > config.maxTransaction / 100 or (
                self.montant + self.argent) > config.maxMontant / 100 or self.montant == 0:  # Vérifie le montant de la recharge
            self.mode = "Error_Montant"
        else:
            self.mode = "QR"
        self.sleeping_mode = True

    def QR(self):
        if command_usb('keyboard','disable') and command_usb('scan','enable'):
            self.top.Page_QR()
        else:
            self.mode = "Error_Matos"
            self.sleeping_mode = True

    def QR_check(self, QR):
        Entrer_log(setting.projet_path, "Logs", "QR code scanné")
        try:
            self.QRcode = eval(QR)
            self.mode = "Transaction"
        except:
            self.mode = "Error_QR"
        self.sleeping_mode = True

    def QR_transact(self):

        if STRING_uidStrToInt(RFID_getUID(self, False))!=self.uidstring:
            self.mode = "Error_Carte"
            self.sleeping_mode = True
        else:
            Entrer_log(setting.projet_path, "Logs", "Identifiant du QR code : " + str(self.QRcode))
            if Transaction_Lydia(setting.numeroBox, self.UID, self.montant, self.QRcode, config_lydia.token_public,
                                 config_lydia.phone):
                Entrer_log(setting.projet_path, "Logs", "Transaction lydia éffectuée avec succès")
                RFID_setArgent(int((self.montant + self.argent) * 100),
                               self.uidstring)  # Ecriture du nouveau montant sur la carte RFID
                Entrer_log(setting.projet_path, "Logs",
                           "Ecriture du nouveau montant sur la carte RFID effectuée avec succès")
                self.mode = "Finish"
            else:
                self.mode = "Error_QR"
            self.sleeping_mode = True



    def Error_QR(self):
        self.top.Page_error_QR()
        self.after(5000, self.rollback, self.mode)

    def Error_carte(self):
        self.top.Page_error_carte()
        self.after(5000, self.rollback, self.mode)

    def Error_montant(self):
        self.top.Page_error_montant()
        self.after(5000, self.rollback, self.mode)

    def Error_rezal(self):
        self.top.Page_error_rezal()
        self.after(5000, self.rollback, self.mode)

    def Error_matos(self):
        self.top.Page_error_matos()
        self.after(5000, self.rollback, self.mode)

    def Finish(self):
        self.top.Page_confirmation()

    def Error_no_carte(self):
        self.top.Page_error_no_carte()
        self.after(5000, self.rollback, self.mode)

    def rollback(self, mode):
        if mode==self.mode:
            self.mode = "Carte"
            self.sleeping_mode = True

