print("Demarrage 'API_lydia.py'")
from Requetes import *

#### Fonction de vérification d'une transaction lydia ####

def Lydia_check(token_public,montant,phone,order_id,Qrcode):

    #Convertit les données scannées du qrcode en un format comprehensible pour la requête Json
    paymentData = json.dumps(Qrcode)

    # Les données à envoyer à l'API
    data = {
        'vendor_token': token_public,
        'amount': montant,
        'phone': phone,
        'order_id': order_id,
        'paymentData': paymentData,
        'currency': 'EUR'
    }

    # Configuration optionnelle : désactiver la vérification SSL pour cet exemple.
    # En production, assurez-vous que SSL est activé et correctement configuré.
    requests.packages.urllib3.disable_warnings()

    # Effectuer la requête POST
    response = requests.post(config_lydia.url, data=data, verify=False)

    # Vérifier la réponse
    if response.status_code == 200:
        # Convertir la réponse en JSON
        response_data = response.json()
        print("Réponse data :",response_data)
        try :
            if response_data['error'] == "0":
                print("Transaction réussie.")
                print("Identifiant de la transaction :", response_data['transaction_identifier'])
                Entrer_log(setting.projet_path, "Logs", "Identifiant de la transaction :" + str(response_data['transaction_identifier']))
                if config.debugging :
                    print("Identifiant de la transaction :", response_data['transaction_identifier'])

                return response_data['transaction_identifier']
        except :
            print("Erreur lors de la transaction :", response_data['status'], response_data['message'])
            Entrer_log(setting.projet_path, "Logs","Erreur lors de la transaction :" + str(response_data['status']) +"  :  " + str(response_data['message']))
            return None

    else:
        print("Erreur de requête HTTP :", response.status_code)
        return None


'''
## Test de la fonction lydia check
token_public = "660e5b8b4c353994613407"
phone='33782977418'
montant=4
order_id=1
Qrcode=["SLebMnW8pk9MlSRO2RYvv04BOw/Eq2mdi21fhEQeEkeC7mYjUzhvAer6XWnuCrTRU6pKsLc7Dxe8hdSo07YhZQ8g5zGHwhB8xo4tKKD0hQvC6EQHCUXJo3SRlmRKn913Ar40gWe2v31OIdbipJcAzTtZW7V3KxPbu5OLRh4epWU=","3"]
transaction_identifier=Lydia_check(token_public,montant,phone,order_id,Qrcode)
'''
