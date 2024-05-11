print("Démarrage 'boot.py'")

projet_path="/".join(__file__.split("/")[:-2])+"/"

print("Chemin :",projet_path)

from Main_affichage import +

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