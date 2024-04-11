
import mysql.connector

# Définition du dictionnaire de connection à la BDD
# Nom d'utilisateur
# Mot de passe du nom d'utilisateur
# Nom de la BDD
# IP du serveur BDD
connection = {"user": 'pi',
              "password": 'pi',
              "database": 'Guinche',
              "host": '192.168.1.110'}   # IP de la BDD de test

serveurNet = "8.8.8.8"

# Définition des requêtes SQL

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

# Définition des fonctions d'exécution des requêtes
def SQL_SELECT(querry):
    _cnx=mysql.connector.connect(**connection)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _select=_cursor.fetchall()
    _cnx.close()
    return _select

def SQL_EXECUTE(querry):
    _cnx=mysql.connector.connect(**connection)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _cnx.commit()
    _cnx.close()
    ##DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_SQL.txt',querry+"\n")

def Recharge_montant(UID,montant):
    Money=SQL_SELECT(QUERRY_getMoney(UID))[0][0]
    SQL_EXECUTE(QUERRY_setMoney(UID,Money+montant))

