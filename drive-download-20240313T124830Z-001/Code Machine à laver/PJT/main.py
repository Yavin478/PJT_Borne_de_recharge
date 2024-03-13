# coding: utf-8
##############################################################################################
#											     #
#												#
#                                                                                            #
#                                                                                            #
#   				  Tag 166tt, Zt Rezal, KIN 215                               #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################

from keyboard import *
from php import *
from relais import *
from times import *
from mysql import *
from lcd import *
from qrcode import *
from files import *
from network import *
from datetime import datetime

def log(msg):
	now = datetime.now()
	with open("babass.log","a") as f:
		text = now.strftime("[%d/%m/%Y %H:%M:%S] ")+msg
		print(text)
		f.write(text+"\n")

def start():
	lcd = initialize_lcd()
	return lcd

def disp(lcd,t,l2):
	clear_lcd(lcd)
	if t == 3:
		write_line(lcd,"Scannez le QR Code",2)
		write_line(lcd,"Payez 2.5E avec",3)
		write_line(lcd,"l'app. Lydia",4)


	elif t == 4:
		write_line(lcd,"Validation en cours",1)

	elif t == 5:
		#write_line(lcd,"Paiement valide !",1)
		write_line(lcd,"Choix machine :",1)
		write_line(lcd,"Machine A : *",2)
		write_line(lcd,"Machine B : 0",3)
		write_line(lcd,"Machine C : #",4)

	elif t == 6:
		write_line(lcd,"Lancement du lavage!",1)
		#write_line(lcd,"Code a noter :",2)
		write_line(lcd,"A bientot !",4)

	elif t == 7:
		write_line(lcd,"Il te reste:",1)
		write_line(lcd,str(l2)+" machines",2)

	elif t == 9:
		write_line(lcd,"Probleme paiement!",1)
		write_line(lcd,"Annulation...",2)

	elif t == 10:
		write_line(lcd,"Code non reconnu!",2)

	elif t == 11:
		write_line(lcd,"Code expire!",2)

	elif t == 12:
		write_line(lcd,"Choix :",1)
		write_line(lcd,"0 pour valider",3)

	elif t == 13:
		write_line(lcd,"Admin reconnu",1)
		write_line(lcd,"Demarrage",2)

	elif t == 14:
		write_line(lcd,"Pb reseau",1)
		write_line(lcd,"Contacter le rezal",2)

	elif t == 53:
		write_line(lcd, "Verification",1)


	elif t == 101:	# erreur 201
		write_line(lcd,"Erreur : 201",1)
		write_line(lcd,"Fonds indisponibles",2)
		write_line(lcd,"Verifiez le solde de",3)
		write_line(lcd,"votre compte Lydia.",4)
	elif t == 102:	# erreur 206
		write_line(lcd,"Erreur : 206",1)
		write_line(lcd,"QR Code expire !",2)
		write_line(lcd,"Regenerez un nouveau",3)
		write_line(lcd,"QR Code.",4)
	elif t == 103:	# erreur 207
		write_line(lcd,"Erreur : 207",1)
		write_line(lcd,"Transaction refusee",2)
		write_line(lcd,"par la banque !",3)
		write_line(lcd,"Verifiez le plafond.",4)
	elif t == 104:	# erreur 208
		write_line(lcd,"Erreur : 208",1)
		write_line(lcd,"Compte lydia bloque",2)
		write_line(lcd,"Utilisez un autre",3)
		write_line(lcd,"compte Lydia.",4)
	elif t == 105:	# erreur 213
		write_line(lcd,"Erreur : 213",1)
		write_line(lcd,"Limites de paiement",2)
		write_line(lcd,"atteintes ! Veuillez",3)
		write_line(lcd,"valider le compte.",4)
	elif t == 106:	# erreur 214
		write_line(lcd,"Erreur : 214",1)
		write_line(lcd,"QR Code deja utilise",2)
		write_line(lcd,"Regenerez un nouveau",3)
		write_line(lcd,"QR Code.",4)
	else:
		return False

def main_lavage(lcd,l):
	#print "lavage"
	#disp(lcd,3,l)
	#flash = get_qrcode()
	#post_value(flash)
	#post_value("plop")
	#print "Posted Variables !"
	log("Selection machine")

	disp(lcd,5,l)
	key = sel_mode(["*","0","#"])
	#key = "*"

	
	if key == "*":
		#start_m(1)
		id_machine = 1
		machine = "A"
	elif key == "#":
        #start_m(2)
		id_machine = 3
		machine = "C"
	elif key == "0":
		#start_m(2)
		id_machine = 2
		machine = "B"

	log("Machine "+machine+" selectionée")
	##disp(lcd,12,l)
	##write_line(lcd,machine,2)
	##key = sel_mode(["0"])
	insert_new_l(str(id_machine))
	order_id_tmp = get_order_id()
	order_id = int(order_id_tmp[-1][0])
	#print order_id
	disp(lcd,3,l)
	write_line(lcd,"Machine "+machine+" select.",1)
	flash = get_qrcode()
	if flash == False:	#On a attend le timeout
		return	#Retour à l'écran principal

	log("qr : "+flash)

	disp(lcd,53,1)

	if flash == "[7a2dd0c7f7168e58b1ee438d078ad32b]":
		log("Admin qr scanned. machine "+machine+" start")
		disp(lcd,13,l)
		start_m(id_machine)
		#write_m("admin")
		sleep(5)
	else:
		if len(flash) == 38:
			log("Unique qrcode scanned. Checking access")
			L=check_qrcode_unique(flash)
			if L[0]:
				log("Machine "+machine+" started")
				print(10)
				start_m(id_machine)
				print(11)
				start_machine(str(id_machine))
				print(12)
				disp(lcd,7,L[1])
				sleep(5)
				print(13)
				return(True)
			else:
				print(14)
				disp(lcd,11,l)
				sleep(5)
				print(15)
				return(False)

		if internet_on():
			#print flash
			#flash = "test"
			#print type(flash)
			log("Lydia qr scanned, request api")
			post_request_status = post_value(str(flash), order_id)
			log("Request status: "+str(post_request_status))
			if post_request_status == False:
				clear_lcd(lcd)
				write_line(lcd,"POST Error",2)
				write_line(lcd,"Aborting",3)
				mark_m_cancel_all()
				sleep(5)
				return False
			disp(lcd,4,l)

			log("Checking for transaction")
			transaction = find_transaction()
			#print transaction
			while transaction == ():
				transaction = find_transaction()
				#print transaction
			if transaction[-1][5] == 0:
				log("Transaction founded, starting machine "+machine)
				#disp(lcd,5,l)
				#key = sel_mode(["A","B"])
				#if key == "A":
		                #        start_m(1)
				#	id_machine = 1
		                #elif key == "B":
		                #        start_m(2)
				#	id_machine = 2
				print("Démarrage machine"+str(id_machine))
				start_m(id_machine) 
				#write_normal_m()
				#set_m_id(id_machine)
				code_gen = get_code()
				id_transaction = str(transaction[0][0])
				#print id_transaction
				insert_code(str(code_gen),str(id_machine),str(id_transaction))
				start_machine(str(id_machine))
				disp(lcd,6,l)
				#write_line(lcd,code_gen,3)
				sleep(15)
			else:
				disp(lcd,9,l)	# message de problème paiement affiché
				code_erreur = int(str(transaction[-1][5]))
				write_line(lcd,"Erreur : " + str(code_erreur),3)
				log("Error : " + str(code_erreur))
				sleep(3)	# pendant 3 secondes
				# affichage du détail de l'erreur :
				if code_erreur == 201:
					disp(lcd,101,l)
				elif code_erreur == 206:
					disp(lcd,102,l)
				elif code_erreur == 207:
					disp(lcd,103,l)
				elif code_erreur == 208:
					disp(lcd,104,l)
				elif code_erreur == 213:
					disp(lcd,105,l)
				elif code_erreur == 214:
					disp(lcd,106,l)
				mark_m_cancel()
				sleep(5)
		else:
			disp(lcd,14,l)
			sleep(5)

def main_sechage(lcd,l):
	#print "sechage"
	disp(lcd,7,l)
	code = type_code(lcd)
	if code != False:
		code_db = find_sec_code(code)
		if code_db == ():
			disp(lcd,10,l)
			sleep(5)
		else:
			now = get_timestamp()
			#print code_db
				#print (code_db[0][2]-datetime.datetime(1970,1,1,0,0,0)).total_seconds()
			delta = get_delta((code_db[0][2]-datetime.datetime(1970,1,1,0,0,0)).total_seconds(),now)
			print(delta)
			if delta < 86400:
				disp(lcd,8,l)
				start_m(3)
				start_machine(3)
				mark_sec_used(str(code))
				sleep(2)
			else:
				disp(lcd,11,l)
				sleep(5)

def main(l):
	lcd = start()
	main_lavage(lcd,l)
	##disp(lcd,1,l)
	##key = sel_mode(["*","#"])
	##if key == "*":
		##disp(lcd,2,l)
		#key = sel_mode(["*","#"])
		##key = sel_mode(["*"])
		##if key == "*":
			#if internet_on():
			##main_lavage(lcd,l)
			#else:
			#	disp(lcd,14,l)
			#	sleep(5)
		#elif key == "#":
		#	main_sechage(lcd,l)
		##elif key == "F":
		##	main(l)
	##elif key == "#":
		##if l == 1:
		##	main(2)
		##elif l == 2:
		##	main(1)

sleep(2)
log("Starting système")
while 1:
	l = 1
	main(1)
