print("Démarrage 'loop_borne_auto.py'")

# Code V2 allégé spécialement pour la borne automatique.
# Dans le cadre du code de la borne automatique on remplace la fonction hint("text",int) par une fonction afficher("text",int) qui affichera à l'écran les infos
# cela permettra de profiter de l'écran de la borne et de tkinter.

# Il faut aussi changer  le code pour interagir avec le clavier si on a pas le même nombre de touche ou si elles sont attribués différemment.

# dans un 1er temps je retire le code qui n'est plus adapté à l'architecture matérielle de la borne.
# dans un 2e temps on crée un code fonctionnel
# ensuite on réimplémentera le code fonctionnel de la borne auto dans le code normal en lui faissant reconnaitre que c'est une borne plus ou moins loin dans le code.
# Le seul problème est que les architecture matériel ne seront pas les même bloquant ainsi la compatibilité

def afficher(text, int):
    print(text)


while True:  # Seconde boucle infinie permettant d'utiliser la commande "break" pour arreter la transaction
    if setting.rezalOn and setting.rezalMode:
        REZAL_synchQUERRYToSQL()  # Synchronisation des requêtes SQL de la box avec le serveur BDD

    DATA_setVariable("rezalOn", bool(REZAL_pingServeur()))  # Ping du serveur pour s'assurer que la connection est toujours présente

    # Bloc de traitement des données si la box est en ligne avec le serveur
    if setting.rezalOn:
        # Le rezal est revenu sur une box en mode hors ligne
        if not (setting.rezalMode):


    # Bloc de traitement des données de la carte en mode hors ligne ou sans réseau
    if not (setting.rezalOn) or not (setting.rezalMode):
        if setting.rezalMode:  # Si la box ne ping plus mais est en rezalMode On
            afficher("PERTE DU REZAL", 4)  # Affichage du problème
            REZAL_restart()  # Redémarrage du système
        # Sinon la box est en rezalMode Off, qu'elle pingue ou non

        # On test si la carte est une carte d'appro
        if hashCodeType == CRYPT_hashage(config.codeAppro):
            afficher("Carte d'Appro", 2)
            afficher("!PAS DE REZAL!", 3)
            afficher("appuyer pour reboot", 4)
            touche = CLAVIER_getRFID()
            REZAL_restart()

        # Si le codeGuinche est périmé, c'est une carte non encore initialisée
        if hashCodeType != CRYPT_hashage(config.codeGuinche):
            afficher("DESYNCH RFID H TYPE", 2)  # Affichage désynchronisation
            if not (setting.nomBox[0] == "C" or setting.nomBox[0] == "A"):  # Si la box n'est pas une caisse:
                break  # Arret de la transaction
            # Si la babass est une caisse, on peut reset la carte, et elle sera synchronisée quand la babass retrouve la connexion
            afficher("ENTRER POUR RESET", 3)  # Instruction pour l'utilisateur
            if not (CLAVIER_getRFID() == 10):  # Une autre touche que ENTER est saisie:
                break  # Arret de la transaction
            afficher("SYNCH RFID H TYPE", 4)  # Affichage synchronisation
            RFID_setHashCodeType(config.codeGuinche, UID)  # Ecriture RFID du Hash du codeGuinche sur la carte
            DATA_add(setting.projet_path + 'PICONFLEX2000-LOGS/LOG_QUERRY.txt', QUERRY_addCarte(STRING_uidStrToInt(UID)))  # Ajout de la carte dans la BDD pour une future synchronisation
            afficher("SYNCH RFID H UID", 4)  # Affichage synchronisation
            RFID_setHashUID(UID)
            afficher("SYNCH RFID ARGENT", 4)  # Affichage synchronisation
            RFID_setArgent(0, UID)  # Mise à zero de l'argent RFID de la carte
            argent = 0  # Synchronisation de la variable argent
            hashUID = CRYPT_hashage(UID)  # Recalcul de la variable hash UID
            hashArgent = CRYPT_hashage(argent)  # Recalcul de la variable hash argent
            afficher("", 3)
            afficher("", 4)

        # dans les 2 cas suivants, il y a possibilité d'une modification des données, qui ne peuvent être vérifiée contre celles de la base de donnée
        # on arrete donc la transaction (et on dit d'appeler le rezal)
        if hashUID != CRYPT_hashage(UID):  # Vérification du hash UID
            afficher("DESYNCH H UID", 2)  # Affichage problème
            afficher("APPELLER REZAL", 3)
            break  # Arret transaction
        if hashArgent != CRYPT_hashage(argent):  # Vérification du hash argent
            afficher("DESYNCH H ARGENT", 2)  # Affichage problème
            afficher("APPELLER REZAL", 3)
            break  # Arret transaction

    afficher("Credit: " + STRING_montant(argent), 3)
    # Si la box est une caisse, on entre dans un contexte d'ajout d'argent
    # if setting.nomBox[0]=="C":
    #    montant=MENU_getMontant(argent) #Demande du montant à ajouter sur la carte
    #    produit="RechargeMontant" #Le produit est nommé RechargeMontant(utiliser pour différentier les requêtes SQL)
    #    nombre=1 #Une seule recharge (permet de standardiser les transactions mais est inutile ici)
    #    reference=-1 #Pas de référence
    ## Si la box est une Kve, on entre dans un contexte de soustraction d'un montant libre
    # elif setting.nomBox[0]=="K":
    #    montant=-MENU_getMontant(argent)#Demande du montant à retirer sur la carte
    #    produit="VenteMontant"#Le produit est nommé RechargeMontant(utiliser pour différentier les requêtes SQL)
    #    nombre=1 #Une seule recharge (permet de standardiser les transactions mais est inutile ici)
    #    reference=-1 #Pas de référence
    # Les autres cas correspondent à des babass à un pianss
    if setting.nomBox[0] == "A":
        montant = MENU_getMontant(
            argent)  # Lance la récupération du QR code et donc du montant à ajouter sur la carte ( à faire sous forme d'une formualaire avec tkinter)
        if montant > 0:
            produit = "RechargeMontantAutomatique"  # Le produit est nommé RechargeMontantAutomatique pour différencier les paiements
            nombre = 1  # Une seule recharge (permet de standardiser les transactions mais est inutile ici)
            reference = -1  # Pas de référence
            Validation_lydia = Transaction_Lydia(
                montant)  # Ce programme doit demander le QRcode , et effectuer la transaction et renvoyer une validation sous la forme d'un booléen
            # le code main_lydia prend même en compte l'incrémentation de la bdd.
            if Validation_lydia:
                # RequêteSQL("incrémente la base de donnée avec la transaction (table rechargement)")
                # RequêteSQL("Add  argent_echange à la iD de carte associé")
                afficher("Argent disponible :" + argent_disponible + "/n La carte va être rechargée")
            else:
                afficher("La transaction à echoué")
                break  # Arret de la transaction
        else:
            afficher("montant invalide")
    # Il faut modifier la fonction de pour récupérer le montant.
    else:
        print("erreur de nomBox dans settingm o")
        # reference,nombre,produit,montant=MENU_getCommande(argent) #Paramètres de la commande
