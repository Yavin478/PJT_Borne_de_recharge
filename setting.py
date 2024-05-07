print("Démarrage 'setting.py'")

class setting: #Définition des variables reliée à l'objet setting définissant les paramètres de la box. Ces paramètres sont sauvegardés et résistent au reboot
    nomBox='B'
# Nom de la box (Données par la BDD au démarrage), il définie le rôle de la box selon la première lettre (ATTENTION: Première lettre toujours en majuscule)
    numeroBox=100
# Numéro de la box, permet d'identifié de façon unique les boxs (clé primaire) pour la BDD
    version=0
# Version du système, permet de savoir quand une MAJ est a faire
    rezalOn=True
# Paramètre indiquand au système si la box a ping le serveur (010)
    rezalMode=True
# Paramètre indiquand si la box est en mode hors ligne ou pas (001)
    rezalNet=True
# Paramètre indiquant si la box à ping un réseau internet(100)
    IP="0.0.0.0"
# IP de la box
    MAC="00:00:00:00:00"
# Adresse MAC de la box
    produits={}
# Dictionnaire des produits de la box
    connection={}
# Définition du dictionnaire de connection à la BDD
    connection["user"]='pi'
# Nom d'utilisateur
    connection["password"]='pi'
#Mot de passe du nom d'utilisateur
    connection["database"]='Guinche'
# Nom de la BDD
    connection["host"]="192.168.1.110"
# IP du serveur BDD
    serveurNet="8.8.8.8"
# Adresse IP DNS google qui répond au ping
    minMontant = 100
# Montant en centimes minimal à pouvoir mettre pendant une transaction
    maxTransaction = 9900
# Montant max à pouvoir être mis sur une carte
    maxMontant = 15000
# Montant en centime maximal à pouvoir être contenu sur une carte
    debugging = False
# Variable pour avoir des affichages dans la console pour savoir à où le code en est


