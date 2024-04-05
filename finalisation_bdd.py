
import mysql.connector
import main_lydia

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
def QUERRY_getIdLydia(UID,date):
    return (("SELECT id FROM recharge_lydia WHERE UID_carte= '{}' AND date= '{}';").format(UID,date))

def QUERRY_setIdLydia(UID,date):
    return (("INSERT INTO recharge_lydia (UID_carte,date) VALUES ('{}','{}');").format(UID,date))

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
