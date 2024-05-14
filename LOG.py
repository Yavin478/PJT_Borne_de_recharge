import os
import datetime
print('Importation de LOG.py')

def LOG_add(fichierName,contenu):
    _tmp=open(fichierName,"a")
    _tmp.write(str(contenu))
    _tmp.close()


def Entrer_log (projet_path,nom_fichier_log,contenu):
    os.makedirs('Log', exist_ok=True)
    LOG_add(projet_path+'/'+nom_fichier_log,contenu)

####Exemple d'entrée de log.txt
#Entrer_log(os.path.abspath(os.path.dirname(__file__)),'LOG.txt','self.mode=='+'carte'+' heure: '+str(datetime.datetime.now())+"\n")
####