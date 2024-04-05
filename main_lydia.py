
from prepa_bdd import *
from API_Lydia import *

# 1) Détection et récupération de l'UID de la carte à recharger et du temps courant de la BDD
UID=35028059

# 2) Récupération du montant de l'argent actuel sur la carte
argent_carte=SQL_SELECT(QUERRY_getArgent(UID))[0][0]

# 3) Vérification et récupération du montant saisi par l'utilisateur
montant=10

# 4) Récupération de la date courrante et insertion de l'id de la transaction a effectuée avec l'UID de la carte
current_date=SQL_SELECT(QUERRY_getTime())[0][0]
SQL_EXECUTE(QUERRY_setIdLydia(UID,current_date))

# 5) Récupération de l'id de cette transaction
order_id=SQL_SELECT(QUERRY_getIdLydia(UID,current_date))[0][0]

# 6) Récupération des infos du Qrcode
paymentData=''

# 7) Vérification de la transaction avec l'API lydia
# check=Lydia_check(token_public,montant,phone,order_id,paymentData)

# 8) Si paiement refusé (check = None): restart le prg

# 9) Si paiement validé (check != None): MAJ montant de la carte BDD

# 10) MAJ de la table recharge_lydia dans la BDD

