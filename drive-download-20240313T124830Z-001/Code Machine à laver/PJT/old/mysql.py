##############################################################################################
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                  Tag 166tt, Zt Rezal, KIN 215                              #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################

import MySQLdb

def check_qrcode_unique(flash):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
	print(2)
	cur = db.cursor()
	print(3)
	cur.execute("SELECT * FROM `qrcodes_unitaires` WHERE `key` = '" + str(flash)+"';")
	print(4)
	donnee = cur.fetchone()
	print(5)
	if donnee[2]==0:
		print(donnee)
		print(6)
		cur.execute("UPDATE `qrcodes_unitaires` SET `used`= 1 WHERE `key`='"+ str(flash)+"';")
		print(7)
		db.commit()	
		return(True)
	else:
		print(8)
		return(False)

def fetch_all(table):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
	cur.execute("SELECT * FROM " + str(name))
	db.close()
	return cur.fetchall()

def update_status(id):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
	cur.execute("UPDATE `machines` SET `etat` = 1 WHERE `machines`.`id` = " + str(id) + ";")
	db.commit()
	db.close()

def find_transaction():
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
	#cur.execute("SELECT * FROM `LavageKIN`.`machines` WHERE `machines`.`erreur` = 0 AND `machines`.`started` = 0")
	cur.execute("SELECT * FROM `transactions` WHERE `erreur` IS NOT NULL AND `started`=0;")
	db.close()
	return cur.fetchall()

def find_sec_code(code):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
        cur.execute("SELECT * FROM `transactions` WHERE `code_sechage`=" + code + " AND `code_sechage_used`='0';")
        db.close()
        return cur.fetchall()

def insert_code(code,id_machine,id_transaction):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
	#request = "UPDATE `machines` SET `code_sechage` = " + code + " WHERE `id` = " + str(id) + ";"
	#request = "UPDATE transactions, machines SET machines.etat = 1, transactions.code_sechage = " + code + " WHERE machines.id = " + id_machine + " AND transactions.id = " + id_transaction + ";"
	#print request
        cur.execute("UPDATE transactions, machines SET machines.etat = 1, transactions.code_sechage = " + code + " WHERE machines.id = " + id_machine + " AND transactions.id = " + id_transaction + ";")
        db.commit()
        db.close()

def start_machine(id_machine):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
        cur.execute("UPDATE `machines` SET `etat` = 1 WHERE `machines`.`id` = " + str(id_machine) + ";")
        db.commit()
	cur.execute("UPDATE `transactions` SET `started` = 1 WHERE `id_machine` = " + str(id_machine) + ";")
        db.commit()
        db.close()

def mark_sec_used(code):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
        cur.execute("UPDATE `transactions` SET `code_sechage_used` = 1 WHERE `code_sechage` = " + code + ";")
        db.commit()
        db.close()

def insert_new_l(id_machine):
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
        cur.execute("INSERT INTO `LavageKIN`.`transactions` (`id_machine`) VALUES ('" + str(id_machine) + "');")
        db.commit()
        db.close()

def mark_m_cancel():
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
        cur.execute("UPDATE `transactions` SET `started` = '-1' WHERE `started` = 0 AND `erreur` IS NOT NULL;")
        db.commit()
        db.close()

def mark_m_cancel_all():
        db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
        cur.execute("UPDATE `transactions` SET `started` = '-1' WHERE `started` = 0 AND `erreur` IS NULL;")
        db.commit()
        db.close()

def get_order_id():
	db = MySQLdb.connect(host="localhost",user="lydia",passwd="rezal@K1N",db="LavageKIN")
        cur = db.cursor()
        cur.execute("SELECT `id` FROM `transactions` WHERE `started` = 0 AND `erreur` IS NULL;")
        db.close()
        return cur.fetchall()

#print find_transaction()
