import sqlite3 as lite
import os


def QUERRY_setMontant(UID, montant):
    return (("UPDATE cartes SET ArgentCarte = '{}' WHERE UID='{}';").format(montant, UID))


def QUERRY_getArgent(UID):
    return (("SELECT ArgentCarte FROM cartes WHERE UID = '{}';").format(UID))


def QUERRY_Rechargement(UID, montant):
    montant_pre_recharge = execution(QUERRY_getArgent(UID))[0]['ArgentCarte']
    montant_recharge = int(montant) + int(montant_pre_recharge)
    return QUERRY_setMontant(UID, montant_recharge)


def execution(QUERRY):
    db = "data.sqlite"
    if os.path.exists(db):
        con = lite.connect("data.sqlite")
        print("connection réussie !")
    else:
        print("connection échouée : le fichier '" + db + "' est introuvable !")
        quit()

    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute(QUERRY)
    con.commit()
    con.close()
    return

#execution(QUERRY_Rechargement(input("UID :"), input("Montant :")))
