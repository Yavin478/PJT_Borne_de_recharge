print("Démarrage 'boot.py'")

projet_path="/".join(__file__.split("/")[:-2])+"/"

print("Chemin :",projet_path)

## Loop ##
exec(open(projet_path+'PJT_Borne_de_recharge/config.py').read())
exec(open(projet_path+'PJT_Borne_de_recharge/importation.py').read())

## RFID ##
exec(open(projet_path+'PJT_Borne_de_recharge/MFRC522.py').read())
exec(open(projet_path+'PJT_Borne_de_recharge/STRING.py').read())
exec(open(projet_path+'PJT_Borne_de_recharge/RFID.py').read())

## BDD ##
exec(open(projet_path+'PJT_Borne_de_recharge/SQL.py').read())
exec(open(projet_path+'PJT_Borne_de_recharge/Requetes.py').read())

## Lydia ##
exec(open(projet_path+'PJT_Borne_de_recharge/config_lydia.py').read())
exec(open(projet_path+'PJT_Borne_de_recharge/API_lydia.py').read())
exec(open(projet_path+'PJT_Borne_de_recharge/main_lydia.py').read())

## Affichage ##



if config.debugging :
    print("Attente de 3s")
    sleep(3)


while True:  # Boucle infinie du script
    try:
        exec(open(projet_path+'PJT_Borne_de_recharge/loop_borne_auto.py').read())  # Execution du script se répétant jusqu'à l'arrêt du système
    except:
        print("Erreur de boot")
        #exec(open(projet_path+'PICONFLEX2000-CLIENT/error.py').read())  # Script de gestion et affichage des erreurs