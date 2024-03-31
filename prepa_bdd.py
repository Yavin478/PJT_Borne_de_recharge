
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
def QUERRY_getIdLydia(UID,date):
    return (("SELECT id FROM recharge_lydia WHERE UID_carte= '{}' AND date= '{}';").format(UID,date))

def QUERRY_setIdLydia(UID,date):
    return (("INSERT INTO recharge_lydia (UID_carte,date) VALUES ('{}','{}');").format(UID,date))

def QUERRY_getTime():
    return (("SELECT NOW();"))

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

## Procédure rechargement

# 1) Récupération de l'UID de la carte à recharger et du temps courant de la BDD
UID=35028059
current_date=SQL_SELECT(QUERRY_getTime())[0][0]

print(current_date)

# 2) Insertion de l'id de la transaction a effectuée avec l'UID de la carte
SQL_EXECUTE(QUERRY_setIdLydia(UID,current_date))

# 3) Récupération de l'id de cette transaction
id=SQL_SELECT(QUERRY_getIdLydia(UID,current_date))[0][0]
print(id)