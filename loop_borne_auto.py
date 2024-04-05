"""

from datetime import datetime
Instruction_lydia="Présentez le QRCode lydia devant le scanner"
Echange_Max=5000 # valeur en centime
#drapeau indique si on laisse les gens se débucquer.
while drapeau :
    Id_carte=lecture_RFID()
    if Id_carte !='':
        argent_disponible=recuperation_argent(Id_carte)
        afficher("Argent disponible :"+argent_disponible)
        date=datetime.now()
        Qrcode=''
        afficher(Instruction_lydia)

        while Qrcode!='' and date<date+timedelta(seconds=57) :#voir si c'est supporté
            Qrcode=lecture_Qrcode()
        # on considère que l'on a le QRCode ou que l'on repart au début
        if Qrcode!='':
            #il faut récupérer les données nécessaires au paiement 
            # et surtout pour pouvoir modifier la BDD
            #on a donc :
            Argent_echange=dechiffrage_QrCode()

            if  Argent_echange <= Echange_Max:
                if Argent_echange>0 :
                    Validation_lydia=Transaction_Lydia(QrCode)# Ce programme doit effectuer la transaction et renvoyer une validation sous la forme d'un boolenn
                    if Validation_lydia :
                        RequêteSQL("incrémente la base de donnée avec la transaction (table rechargement)")
            
                        RequêteSQL("Add  argent_echange à la iD de carte associé")

                        argent_disponible=recuperation_argent(Id_carte)
                        afficher("Argent disponible :"+argent_disponible+"/n La carte a été rechargée")
                    else:
                        afficher("La Transaction n'a pas pu aboutir, vous êtes probablement pauvre.")
                else:
                    afficher("Ha Ha Ha , j'ai ton nom fdp tu ne peux pas te cacher. Je vais te trouver...")
            else :
                afficher("Somme échangée supérieure à"+Echange_Max/100+"€, tentez l'action avec un montant inférieur à"+Echange_Max/100)
        else:
            #On considèreque que le gars est parti et qu'il faut repartir du début
        
    else:
        afficher("Présentez la carte")
"""
#Dans le cadre du code de la borne automatique on remplace la fonction hint("text",int) par une fonction afficher("text",int) qui affichera à l'écran les infos
#cela permettra de profiter de l'écran de la borne et de tkinter.

#Il faut aussi changer  le code pour interagir avec le clavier si on a pas le mêm nombre de touche ou si elles sont attribués différemment.

#dans un 1er temps je retire le code qui n'est plus adapté à l'architecture matérielle de la borne.

print("Demarrage 'loop.py'")
while True: #Seconde boucle infinie permettant d'utiliser la commande "break" pour arreter la transaction
    if setting.rezalOn and setting.rezalMode:
        REZAL_synchQUERRYToSQL() #Synchronisation des requêtes SQL de la box avec le serveur BDD
    RFID_waitRetireCarte() #Attente d'absence de cartes
    MENU_menuPrincipal() #Attente d'une carte et possibilité de naviguer dans les menus
    UID,argent,hashCodeType,hashUID,hashArgent=RFID_readCarte() #Multi lecture des données de la carte
    DATA_setVariable("rezalOn",bool(REZAL_pingServeur())) #Ping du serveur pour s'assurer que la connection est toujours présente

    # Bloc de traitement des données si la box est en ligne avec le serveur
    if setting.rezalOn:
        # Le rezal est revenu sur une box en mode hors ligne
        if not(setting.rezalMode):
            # Affichage du problème
            afficher("REZAL REVENU",3)
            afficher("TOUCHE POUR CONTINUER",4)
            _touche=CLAVIER_getRFID()
            if _touche==0:
                # La carte a été retirée
                break
            else:
                # On efface le message
                afficher("",3); afficher("",4)

        # rezalMode est à True, donc on fait la synchronisation des données de la carte avec celles de la BDD
        else:
            # on test si la carte est une carte d'appro
            if hashCodeType == CRYPT_hashage(config.codeAppro):
                afficher("Carte d'Appro",2)
                try:
                    requests=SQL_SELECT(QUERRY_getCommandeEnCours(STRING_uidStrToInt(UID)))
                    if len(requests)==0:
                        afficher("Pas de CMD en cours", 3)
                    else:
                        listeAutresPianss=[]
                        cmdOK=False
                        for request in requests:
                            #test du pianss
                            if request[0]==setting.nomBox:
                                afficher("SYNCH BDD", 3)
                                SQL_EXECUTE(QUERRY_ajoutStock(request[2],request[3]))
                                SQL_EXECUTE(QUERRY_validationCommande(request[1]))
                                afficher("Status valide!", 3)
                                cmdOK = True
                            else:
                                if request[0] not in listeAutresPianss:
                                    listeAutresPianss.append(request[0])
                        sleep(0.5)
                        if len(listeAutresPianss)!=0:
                            if cmdOK:
                                _ligne1="AUTRES PIANSS:"
                            else:
                                _ligne1="MAUVAIS PIANSS:"
                            _ligne2="Dest: "+",".join(listeAutresPianss)
                            _ligne3=""
                            if len(_ligne2)>20:
                                _ligne3=_ligne2[20:]
                                _ligne2=_ligne2[:20]
                            afficher(_ligne1,1)
                            afficher(_ligne2,2)
                            afficher(_ligne3,3)
                            while RFID_carteCheck():
                                afficher(_ligne1, 1)
                                afficher("RETIRER CARTE", 4)
                                sleep(0.3)
                                afficher("", 1)
                                afficher("", 4)
                                sleep(0.3)
                except: #Echec dans la querry
                    afficher("ERR QUERRY",3) #Affichage utilisateur de l'initialisation de la carte dans la BDD
                while RFID_carteCheck():
                    afficher("RETIRER CARTE", 4)
                    sleep(0.3)
                    afficher("", 4)
                    sleep(0.3)
                break

            afficher("UID: "+str(UID),2) #Affichage UID de la carte
            # Essais de récupération de l'argent de la carte de la BDD:
            try:
                argentSQL=SQL_SELECT(QUERRY_getArgent(STRING_uidStrToInt(UID)))[0][0]
            except: #Echec (la carte (UID) est absente de la BDD):
                afficher("SYNCH CARTE BDD",4) #Affichage utilisateur de l'initialisation de la carte dans la BDD
                argentSQL=0 #Montant nul pour la carte
                SQL_EXECUTE(QUERRY_addCarte(STRING_uidStrToInt(UID))) #Création de la carte dans la BDD

            # Cas où les montants RFID et BDD sont différents:
            if argent!=argentSQL:
                afficher("SYNCH RFID ARGENT",4) #Affichage synchronisation
                argent=argentSQL #Synchronisation des variables
                RFID_setArgent(argent,UID) #Synchronisaton RFID

            # Le codeGuinche est périmé:
            if hashCodeType!=CRYPT_hashage(config.codeGuinche):
                afficher("SYNCH RFID H TYPE",4) #Affichage synchronisation
                RFID_setHashCodeType(config.codeGuinche,UID) #Ecriture RFID du Hash du codeGuinche sur la carte

            # Le hash de l'UID ne correspond pas au hash stocké sur la carte
            if hashUID!=CRYPT_hashage(UID):
                afficher("SYNCH RFID H UID",4) #Affichage synchronisation
                RFID_setHashUID(UID) #Ecriture du hash de l'UID sur la carte
            # Le hash de l'argent ne correspond pas au hash stocké sur la carte
            if hashArgent!=CRYPT_hashage(argent):
                afficher("SYNCH RFID ARGENT",4) #Affichage synchronisation
                RFID_setArgent(argent,UID) #Ecriture de l'argent sur la carte (Réecrit le hash de l'argent)

            # Si le montant de la carte dans la BDD est inérieur à 0 (Une triche pendant un mode hors ligne a été réalisé ou une désynchronisation a été faite)
            if argent<0:
                afficher("APPELLER REZAL",3) #Le rezal doit regarder l'historique de la carte et vérifier que toute les caisses sont synchro
                afficher("DESYNCH BDD",4) #Affichage problème (Si ce message s'affiche pendant un gala c'est pas bon: soit la personne est un tricheur, soit une box fonctionne en mode hors ligne)
                DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"DESYNCH BDD",str(STRING_uidStrToInt(UID)))) #Ajout du message dans les logs
                break #Arret de la transaction

    # Bloc de traitement des données de la carte en mode hors ligne ou sans réseau
    if not(setting.rezalOn) or not(setting.rezalMode):
        if setting.rezalMode: #Si la box ne ping plus mais est en rezalMode On
            afficher("PERTE DU REZAL",4) #Affichage du problème
            REZAL_restart() #Redémarrage du système
        #Sinon la box est en rezalMode Off, qu'elle pingue ou non


        # On test si la carte est une carte d'appro
        if hashCodeType == CRYPT_hashage(config.codeAppro):
            afficher("Carte d'Appro", 2)
            afficher("!PAS DE REZAL!", 3)
            afficher("appuyer pour reboot", 4)
            touche=CLAVIER_getRFID()
            REZAL_restart()

        # Si le codeGuinche est périmé, c'est une carte non encore initialisée
        if hashCodeType!=CRYPT_hashage(config.codeGuinche):
            afficher("DESYNCH RFID H TYPE",2) #Affichage désynchronisation
            if not(setting.nomBox[0]=="C" or setting.nomBox[0]=="A"): #Si la box n'est pas une caisse:
                break #Arret de la transaction
            #Si la babass est une caisse, on peut reset la carte, et elle sera synchronisée quand la babass retrouve la connexion
            afficher("ENTRER POUR RESET",3) #Instruction pour l'utilisateur
            if not(CLAVIER_getRFID()==10): #Une autre touche que ENTER est saisie:
                break #Arret de la transaction
            afficher("SYNCH RFID H TYPE",4) #Affichage synchronisation
            RFID_setHashCodeType(config.codeGuinche,UID) #Ecriture RFID du Hash du codeGuinche sur la carte
            DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addCarte(STRING_uidStrToInt(UID))) #Ajout de la carte dans la BDD pour une future synchronisation
            afficher("SYNCH RFID H UID",4) #Affichage synchronisation
            RFID_setHashUID(UID)
            afficher("SYNCH RFID ARGENT",4) #Affichage synchronisation
            RFID_setArgent(0,UID) #Mise à zero de l'argent RFID de la carte
            argent=0 #Synchronisation de la variable argent
            hashUID=CRYPT_hashage(UID) #Recalcul de la variable hash UID
            hashArgent=CRYPT_hashage(argent) #Recalcul de la variable hash argent
            afficher("",3)
            afficher("",4)

        #dans les 2 cas suivants, il y a possibilité d'une modification des données, qui ne peuvent être vérifiée contre celles de la base de donnée
        #on arrete donc la transaction (et on dit d'appeler le rezal)
        if hashUID!=CRYPT_hashage(UID): #Vérification du hash UID
            afficher("DESYNCH H UID",2) #Affichage problème
            afficher("APPELLER REZAL",3)
            break #Arret transaction
        if hashArgent!=CRYPT_hashage(argent): #Vérification du hash argent
            afficher("DESYNCH H ARGENT",2) #Affichage problème
            afficher("APPELLER REZAL",3)
            break #Arret transaction


    afficher("Credit: "+STRING_montant(argent),3)
    # Si la box est une caisse, on entre dans un contexte d'ajout d'argent
    if setting.nomBox[0]=="C":
        montant=MENU_getMontant(argent) #Demande du montant à ajouter sur la carte
        produit="RechargeMontant" #Le produit est nommé RechargeMontant(utiliser pour différentier les requêtes SQL)
        nombre=1 #Une seule recharge (permet de standardiser les transactions mais est inutile ici)
        reference=-1 #Pas de référence
    # Si la box est une Kve, on entre dans un contexte de soustraction d'un montant libre
    elif setting.nomBox[0]=="K":
        montant=-MENU_getMontant(argent)#Demande du montant à retirer sur la carte
        produit="VenteMontant"#Le produit est nommé RechargeMontant(utiliser pour différentier les requêtes SQL)
        nombre=1 #Une seule recharge (permet de standardiser les transactions mais est inutile ici)
        reference=-1 #Pas de référence
    #Les autres cas correspondent à des babass à un pianss
    if setting.nomBox[0]=="A":
        montant=MENU_getMontant(argent) #Lance la récupération du QR code et donc du montant à ajouter sur la carte
        produit="RechargeMontantAutomatique" #Le produit est nommé RechargeMontantAutomatique pour différencier les paiements 
        nombre=1 #Une seule recharge (permet de standardiser les transactions mais est inutile ici)
        reference=-1 #Pas de référence
        Validation_lydia=Transaction_Lydia(QrCode, montant)# Ce programme doit effectuer la transaction et renvoyer une validation sous la forme d'un boolenn
        if Validation_lydia :
            RequêteSQL("incrémente la base de donnée avec la transaction (table rechargement)")

            RequêteSQL("Add  argent_echange à la iD de carte associé")
            argent_disponible=recuperation_argent(Id_carte)
            afficher("Argent disponible :"+argent_disponible+"/n La carte a été rechargée")
        else :
            afficher("La transaction à echoué")
    #Il faut modifier la fonction de pour récupérer le montant.
    else:
        reference,nombre,produit,montant=MENU_getCommande(argent) #Paramètres de la commande

    if montant==0: #Si la carte a été retirée
        break #Arret de la transaction
    newMontant=argent+montant #Calcul du nouveau montant de la carte
    # Si le nouveau montant est négatif:
    if newMontant<0:
        afficher("CREDIT INSUFFISANT",2)
        afficher("NE PAS SERVIR",3)
        break #Arret de la transaction
    # Si le nouveau montant n'est pas négatif, on effectue le débuquage sur la bdd puis sur la carte
    DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addArgent(STRING_uidStrToInt(UID),montant)+QUERRY_addTransaction(produit,nombre,setting.numeroBox,STRING_uidStrToInt(UID),montant,reference)) #Ajout des requetes pour la BDD
    afficher("NE PAS RETIRER CARTE",4) #Avertissement sur lequel il faut lourdement insister en mode hors ligne!
    RFID_setArgent(newMontant,UID) #Ecriture du nouveau montant
