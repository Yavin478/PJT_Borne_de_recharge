print("Démarrage 'boot.py'")

from Main_affichage import *


def is_rotation_complete():
    # Cette fonction doit être adaptée à la manière dont vous vérifiez l'état de la rotation
    result = subprocess.run(["xrandr"], capture_output=True, text=True)
    return "right" in result.stdout  # Ajustez cette condition selon votre cas

# Attendre que la rotation soit complète
while not is_rotation_complete():
    time.sleep(1)  # Attend une seconde avant de vérifier à nouveau

# Le reste de votre script


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