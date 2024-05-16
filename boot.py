print("Démarrage 'boot.py'")

from Main_affichage import *


def is_rotation_complete():
    # Cette fonction doit être adaptée à la manière dont vous vérifiez l'état de la rotation
    result = subprocess.run(["xrandr"], capture_output=True, text=True)
    print("Résultat :",result)
    return "right" in result.stdout  # Ajustez cette condition selon votre cas

# Attendre que la rotation soit complète
while not is_rotation_complete():
    print("time")
    time.sleep(1)  # Attend une seconde avant de vérifier à nouveau

# Le reste de votre script


root=MainApp()
root.mainloop()

if config.debugging :
    print("Attente de 3s")
    sleep(3)