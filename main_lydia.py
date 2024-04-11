from config import *
from prepa_bdd import *
from API_Lydia import *
from finalisation_bdd import *

box=100

# 1) Détection et récupération de l'UID de la carte à recharger et du temps courant de la BDD
UID=35028059

# 2) Vérification et récupération du montant saisi par l'utilisateur
montant=4    # montant en euros

# 3) Récupération de la date courrante et insertion de l'id de la transaction a effectuée avec l'UID de la carte
current_date=SQL_SELECT(QUERRY_getTime())[0][0]
SQL_EXECUTE(QUERRY_setIdLydia(current_date))

# 4) Récupération de l'id de cette transaction
order_id=SQL_SELECT(QUERRY_getIdLydia(current_date))[0][0]

# 5) Récupération des infos du Qrcode
Qrcode=["e979DUNgS06Fw0y1z27T7azBoNcZ/XUKZ53sqFpmjKsfEuDvBfG0TsS8iZPzIFrI3hfj4pEzUFEZTFXyDhFIP7WiTsXl6N0wUkYAZYg4iknywcva5fHGuGdeStBRR8O/BQDs8BtUqMNj8PBZyYEFiPNv4F+9ooNUVVaTVyDWTIo=","3"]

# 6) Vérification de la transaction avec l'API lydia
transaction_identifier=Lydia_check(token_public,montant,phone,order_id,Qrcode)

# 7) Si paiement validé (check != None): MAJ montant de la carte BDD et table lydia
if transaction_identifier:
    montant=montant * 100  # en centime pour la bdd
    Recharge_montant(UID,montant)
    date_recharge = SQL_SELECT(QUERRY_getTime())[0][0]
    SQL_EXECUTE(QUERRY_setRecharge(UID, montant, box, date_recharge))
    id_recharge=SQL_SELECT(QUERRY_getIdRecharge(date_recharge))[0][0]
    SQL_EXECUTE(QUERRY_setTransactionLydia(order_id,id_recharge,transaction_identifier))
    print("Mise à jour de la BDD effectuée avec succès")

# 8) Si paiement refusé (check = None): restart le prg
else :
    print("Problème survenu lors de la transaction ")



