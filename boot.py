print("Démarrage 'boot.py'")

from Main_affichage import *

Entrer_log(setting.projet_path, "Logs_prg", "Démarage Programe")

# root=MainApp()
# root.mainloop()

while True:
    print("Test presence :",RFID_presence())

if config.debugging :
    print("Attente de 3s")
    sleep(3)