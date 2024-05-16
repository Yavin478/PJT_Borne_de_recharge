print("Démarrage 'boot.py'")

from Main_affichage import *

Entrer_log(setting.projet_path, "Logs", "Démarage Programe")
print("Time :",ctime())

root=MainApp()
root.mainloop()

if config.debugging :
    print("Attente de 3s")
    sleep(3)