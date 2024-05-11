print("Démarrage 'boot.py'")

projet_path="/".join(__file__.split("/")[:-2])+"/"

print("Chemin :",projet_path)

## Fichier général de boot ##
from importation import *
from config import *
from setting import *
from REZAL import *
from DATA import *

## RFID ##
from MFRC522 import *
from STRING import *
from RFID import *

## BDD ##
from SQL import *
from Requetes import *

## Lydia ##
from config_lydia import *
from API_lydia.py import *
from main_lydia import *

## Affichage ##
from Config_Affichage import *
from Template_pageV2 import *
from Main_affichage import *


root=MainApp()
root.mainloop()

if config.debugging :
    print("Attente de 3s")
    sleep(3)



"""    while True:  # Boucle infinie du script
    try:
        exec(open(projet_path+'PJT_Borne_de_recharge/loop_borne_auto.py').read())  # Execution du script se répétant jusqu'à l'arrêt du système
    except:
        print("Erreur de boot")
        exec(open(projet_path+'PICONFLEX2000-CLIENT/error.py').read())  # Script de gestion et affichage des erreurs
"""