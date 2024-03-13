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
            hint("REZAL REVENU",3)
            hint("TOUCHE POUR CONTINUER",4)
            _touche=CLAVIER_getRFID()
            if _touche==0:
                # La carte a été retirée
                break
            else:
                # On efface le message
                hint("",3); hint("",4)

        # rezalMode est à True, donc on fait la synchronisation des données de la carte avec celles de la BDD
        else:
            # on test si la carte est une carte d'appro
            if hashCodeType == CRYPT_hashage(config.codeAppro):
                hint("Carte d'Appro",2)
                try:
                    requests=SQL_SELECT(QUERRY_getCommandeEnCours(STRING_uidStrToInt(UID)))
                    if len(requests)==0:
                        hint("Pas de CMD en cours", 3)
                    else:
                        listeAutresPianss=[]
                        cmdOK=False
                        for request in requests:
                            #test du pianss
                            if request[0]==setting.nomBox:
                                hint("SYNCH BDD", 3)
                                SQL_EXECUTE(QUERRY_ajoutStock(request[2],request[3]))
                                SQL_EXECUTE(QUERRY_validationCommande(request[1]))
                                hint("Status valide!", 3)
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
                            hint(_ligne1,1)
                            hint(_ligne2,2)
                            hint(_ligne3,3)
                            while RFID_carteCheck():
                                hint(_ligne1, 1)
                                hint("RETIRER CARTE", 4)
                                sleep(0.3)
                                hint("", 1)
                                hint("", 4)
                                sleep(0.3)
                except: #Echec dans la querry
                    hint("ERR QUERRY",3) #Affichage utilisateur de l'initialisation de la carte dans la BDD
                while RFID_carteCheck():
                    hint("RETIRER CARTE", 4)
                    sleep(0.3)
                    hint("", 4)
                    sleep(0.3)
                break

            hint("UID: "+str(UID),2) #Affichage UID de la carte
            # Essais de récupération de l'argent de la carte de la BDD:
            try:
                argentSQL=SQL_SELECT(QUERRY_getArgent(STRING_uidStrToInt(UID)))[0][0]
            except: #Echec (la carte (UID) est absente de la BDD):
                hint("SYNCH CARTE BDD",4) #Affichage utilisateur de l'initialisation de la carte dans la BDD
                argentSQL=0 #Montant nul pour la carte
                SQL_EXECUTE(QUERRY_addCarte(STRING_uidStrToInt(UID))) #Création de la carte dans la BDD

            # Cas où les montants RFID et BDD sont différents:
            if argent!=argentSQL:
                hint("SYNCH RFID ARGENT",4) #Affichage synchronisation
                argent=argentSQL #Synchronisation des variables
                RFID_setArgent(argent,UID) #Synchronisaton RFID

            # Le codeGuinche est périmé:
            if hashCodeType!=CRYPT_hashage(config.codeGuinche):
                hint("SYNCH RFID H TYPE",4) #Affichage synchronisation
                RFID_setHashCodeType(config.codeGuinche,UID) #Ecriture RFID du Hash du codeGuinche sur la carte

            # Le hash de l'UID ne correspond pas au hash stocké sur la carte
            if hashUID!=CRYPT_hashage(UID):
                hint("SYNCH RFID H UID",4) #Affichage synchronisation
                RFID_setHashUID(UID) #Ecriture du hash de l'UID sur la carte
            # Le hash de l'argent ne correspond pas au hash stocké sur la carte
            if hashArgent!=CRYPT_hashage(argent):
                hint("SYNCH RFID ARGENT",4) #Affichage synchronisation
                RFID_setArgent(argent,UID) #Ecriture de l'argent sur la carte (Réecrit le hash de l'argent)

            # Si le montant de la carte dans la BDD est inérieur à 0 (Une triche pendant un mode hors ligne a été réalisé ou une désynchronisation a été faite)
            if argent<0:
                hint("APPELLER REZAL",3) #Le rezal doit regarder l'historique de la carte et vérifier que toute les caisses sont synchro
                hint("DESYNCH BDD",4) #Affichage problème (Si ce message s'affiche pendant un gala c'est pas bon: soit la personne est un tricheur, soit une box fonctionne en mode hors ligne)
                DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"DESYNCH BDD",str(STRING_uidStrToInt(UID)))) #Ajout du message dans les logs
                break #Arret de la transaction

    # Bloc de traitement des données de la carte en mode hors ligne ou sans réseau
    if not(setting.rezalOn) or not(setting.rezalMode):
        if setting.rezalMode: #Si la box ne ping plus mais est en rezalMode On
            hint("PERTE DU REZAL",4) #Affichage du problème
            REZAL_restart() #Redémarrage du système
        #Sinon la box est en rezalMode Off, qu'elle pingue ou non


        # On test si la carte est une carte d'appro
        if hashCodeType == CRYPT_hashage(config.codeAppro):
            hint("Carte d'Appro", 2)
            hint("!PAS DE REZAL!", 3)
            hint("appuyer pour reboot", 4)
            touche=CLAVIER_getRFID()
            REZAL_restart()

        # Si le codeGuinche est périmé, c'est une carte non encore initialisée
        if hashCodeType!=CRYPT_hashage(config.codeGuinche):
            hint("DESYNCH RFID H TYPE",2) #Affichage désynchronisation
            if not(setting.nomBox[0]=="C"): #Si la box n'est pas une caisse:
                break #Arret de la transaction
            #Si la babass est une caisse, on peut reset la carte, et elle sera synchronisée quand la babass retrouve la connexion
            hint("ENTRER POUR RESET",3) #Instruction pour l'utilisateur
            if not(CLAVIER_getRFID()==10): #Une autre touche que ENTER est saisie:
                break #Arret de la transaction
            hint("SYNCH RFID H TYPE",4) #Affichage synchronisation
            RFID_setHashCodeType(config.codeGuinche,UID) #Ecriture RFID du Hash du codeGuinche sur la carte
            DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addCarte(STRING_uidStrToInt(UID))) #Ajout de la carte dans la BDD pour une future synchronisation
            hint("SYNCH RFID H UID",4) #Affichage synchronisation
            RFID_setHashUID(UID)
            hint("SYNCH RFID ARGENT",4) #Affichage synchronisation
            RFID_setArgent(0,UID) #Mise à zero de l'argent RFID de la carte
            argent=0 #Synchronisation de la variable argent
            hashUID=CRYPT_hashage(UID) #Recalcul de la variable hash UID
            hashArgent=CRYPT_hashage(argent) #Recalcul de la variable hash argent
            hint("",3)
            hint("",4)

        #dans les 2 cas suivants, il y a possibilité d'une modification des données, qui ne peuvent être vérifiée contre celles de la base de donnée
        #on arrete donc la transaction (et on dit d'appeler le rezal)
        if hashUID!=CRYPT_hashage(UID): #Vérification du hash UID
            hint("DESYNCH H UID",2) #Affichage problème
            hint("APPELLER REZAL",3)
            break #Arret transaction
        if hashArgent!=CRYPT_hashage(argent): #Vérification du hash argent
            hint("DESYNCH H ARGENT",2) #Affichage problème
            hint("APPELLER REZAL",3)
            break #Arret transaction


    hint("Credit: "+STRING_montant(argent),3)
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
    else:
        reference,nombre,produit,montant=MENU_getCommande(argent) #Paramètres de la commande

    if montant==0: #Si la carte a été retirée
        break #Arret de la transaction
    newMontant=argent+montant #Calcul du nouveau montant de la carte
    # Si le nouveau montant est négatif:
    if newMontant<0:
        hint("CREDIT INSUFFISANT",2)
        hint("NE PAS SERVIR",3)
        break #Arret de la transaction
    # Si le nouveau montant n'est pas négatif, on effectue le débuquage sur la bdd puis sur la carte
    DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addArgent(STRING_uidStrToInt(UID),montant)+QUERRY_addTransaction(produit,nombre,setting.numeroBox,STRING_uidStrToInt(UID),montant,reference)) #Ajout des requetes pour la BDD
    hint("NE PAS RETIRER CARTE",4) #Avertissement sur lequel il faut lourdement insister en mode hors ligne!
    RFID_setArgent(newMontant,UID) #Ecriture du nouveau montant
