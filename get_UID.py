# Importation des modules nécessaires
from RFID import *

UID=STRING_uidStrToInt(RFID_getUID())
print("L'UID de la carte est: ",UID)