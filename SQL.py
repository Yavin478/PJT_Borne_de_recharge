print("Demarrage 'SQL.py'")

#### Définition des requêtes SQL ####

# Préparation BDD
def QUERRY_getIdLydia(date):
    return (("SELECT id FROM recharge_lydia WHERE date= '{}';").format(date))

def QUERRY_setIdLydia(date):
    return (("INSERT INTO recharge_lydia (date) VALUES ('{}');").format(date))

def QUERRY_getTime():
    return (("SELECT NOW();"))

# Finalisation BDD
def QUERRY_getMoney(UID):
    return (("SELECT ArgentCarte FROM cartes WHERE UID='{}';").format(UID))

def QUERRY_setMoney(UID,Money):
    return (("UPDATE cartes SET ArgentCarte='{}' WHERE UID='{}'").format(Money,UID))

def QUERRY_setRecharge(UID, montant, box, date):
    return (("INSERT INTO recharge (UID, montant, box, date) VALUES ('{}','{}','{}','{}');").format(UID, montant, box, date))

def QUERRY_getIdRecharge(date):
    return (("SELECT id FROM recharge WHERE date='{}';").format(date))

def QUERRY_setTransactionLydia(order_id,id_recharge,transaction_identifier):
    return (("UPDATE recharge_lydia SET id_recharge='{}', transaction_identifier='{}'WHERE id='{}'").format(id_recharge,transaction_identifier,order_id))
