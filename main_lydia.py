import requests
import json
import API_Lydia,prepa_bdd,config

# 1) Détection et récupération de l'UID de la carte à recharger et du temps courant de la BDD
UID=35028059

# 2) Récupération du montant actuelle de la carte

# 3) Vérification et récupération du montant saisi par l'utilisateur
montant=10

# 4) Récupération de la date courrante et insertion de l'id de la transaction a effectuée avec l'UID de la carte
current_date=SQL_SELECT(QUERRY_getTime())[0][0]
SQL_EXECUTE(QUERRY_setIdLydia(UID,current_date))

# 5) Récupération de l'id de cette transaction
order_id=SQL_SELECT(QUERRY_getIdLydia(UID,current_date))[0][0]

# 6) Récupération du Qrcode
paymentData=''

# 7) Vérification de la transaction avec l'API lydia
Lydia_check(token_public,montant,phone,order_id,paymentData)


# 8) Si paiement refusé : restart le prg

# 9) Si paiement validé : MAJ montant de la carte BDD

# 10) MAJ recharge_lydia BDD