print("Démarrage 'boot.py'")

from Main_affichage import *

root=MainApp()
root.mainloop()

if config.debugging :
    print("Attente de 3s")
    sleep(3)