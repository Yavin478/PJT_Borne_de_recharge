print("Démarrage 'boot.py'")

from Main_affichage import *

sleep(5)

root=MainApp()
root.mainloop()

if config.debugging :
    print("Attente de 3s")
    sleep(3)