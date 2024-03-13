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

def start():
	lcd = initialize_lcd()
	return lcd

def disp(lcd,t,l):
	clear_lcd(lcd)
	if t == 1:
		if l == 1:
			write_line(lcd,"Bienvenue",1)
			write_line(lcd,"Pour continuer : *",3)
			write_line(lcd,"For English, press #",4)
		if l == 2:
			clear_lcd(lcd)
			write_line(lcd,"Welcome",1)
			write_line(lcd,"To continue, press *",3)
			write_line(lcd,"Pour le Francais : #",4)
		else:
			return False
		return True
	elif t == 2:
		if l == 1:
			write_line(lcd,"Choisir entre :",1)
			write_line(lcd,"* - Lavage",2)
			#write_line(lcd,"# - Sechage",3)
		elif l == 2:
			write_line(lcd,"Choose mode",1)
			write_line(lcd,"* - Washing",2)
			#write_line(lcd,"# - Drying",3)
		else:
			return False
		return True
	elif t == 3:
		if l == 1:
			write_line(lcd,"Scannez le QR Code",2)
			write_line(lcd,"Payez 2.5E avec",3)
			write_line(lcd,"l'app. Lydia",4)
		elif l == 2:
			write_line(lcd,"Scan Lydia QR Code",1)
			write_line(lcd,"Pay 2.5E with",3)
			write-line(lcd,"the Lydia app.",4)
		else:
			return False
		return True
	elif t == 4:
		if l == 1:
			write_line(lcd,"Validation en cours",1)
		elif l == 2:
			write_line(lcd,"Validating payment",1)
		else:
			return False
		return True
	elif t == 5:
		if l == 1:
			#write_line(lcd,"Paiement valide !",1)
			write_line(lcd,"Choix machine :",1)
			write_line(lcd,"Machine A : *",2)
			write_line(lcd,"Machine B : 0",3)
			write_line(lcd,"Machine C : #",4)
		elif l == 2:
			#write_line(lcd,"Payment OK !",1)
			write_line(lcd,"Choose machine :",1)
			write_line(lcd,"Machine A : *",2)
			write_line(lcd,"Machine B : #",3)
		else:
			return False
		return True
	elif t == 6:
		if l == 1:
			write_line(lcd,"Lancement du lavage!",1)
			#write_line(lcd,"Code a noter :",2)
			write_line(lcd,"A bientot !",4)
		elif l == 2:
			write_line(lcd,"Starting program !",1)
			#write_line(lcd,"Code to keep :",2)
			write_line(lcd,"See you soon !",4)
		else:
			return False
		return True
	elif t == 7:
		if l == 1:
			write_line(lcd,"Entrer le code:",1)
			write_line(lcd,"Valider avec *",2)
		elif l == 2:
			write_line(lcd,"Enter code",1)
			write_line(lcd,"Validate with *",2)
		else:
			return False
		return True
	elif t == 8:
		if l == 1:
			write_line(lcd,"Debut sechage!",2)
		elif l == 2:
			write_line(lcd,"Starting program !",2)
		else:
			return False
		return True
	elif t == 9:
		if l == 1:
			write_line(lcd,"Probleme paiement!",1)
			write_line(lcd,"Annulation...",2)
		elif l == 2:
			write_line(lcd,"Payment problem!",1)
			write_line(lcd,"Canceling...",2)
		else:
			return False
		return True
	elif t == 10:
		if l == 1:
			write_line(lcd,"Code non reconnu!",2)
		elif l == 2:
			write_line(lcd,"Code not recognized",2)
		else:
			return False
		return True
	elif t == 11:
		if l == 1:
			write_line(lcd,"Code expire!",2)
		elif l == 2:
			write_line(lcd,"Code expired!",2)
		else:
			return False
		return True
	elif t == 12:
		if l == 1:
			write_line(lcd,"Choix :",1)
			write_line(lcd,"0 pour valider",3)
		elif l == 2:
			write_line(lcd,"Choice :",1)
			write_line(lcd,"0 to confirm",3)
	elif t == 13:
		if l == 1:
			write_line(lcd,"Admin reconnu",1)
			write_line(lcd,"Demarrage",2)
		elif l == 2:
			write_line(lcd,"Admin recognized",1)
			write_line(lcd,"Starting",2)
	elif t == 14:
		if l == 1:
			write_line(lcd,"Pb reseau",1)
			write_line(lcd,"Contacter admin",2)
			write_line(lcd,"support@rezal.fr",3)
		elif l == 2:
			write_line(lcd,"Network pb",1)
			write_line(lcd,"Contact admin",2)
			write_line(lcd,"support@rezal.fr",3)
	elif t == 53:
		if l == 1:
			write_line(lcd, "Verification",1)
		if l == 2:
			write_line(lcd, "Checking", 1)
		return True
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
	disp(lcd,5,l)
	key = sel_mode(["*","0","#"])
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
	disp(lcd,53,1)
	if flash == "[7a2dd0c7f7168e58b1ee438d078ad32b]":
		disp(lcd,13,l)
		start_m(id_machine)
		#write_m("admin")
 		sleep(5)
	else:
		if len(flash) == 38:
			if check_qrcode_unique(flash):
				print(10)
				#start_m(id_machine)
				print(11)
				start_machine(str(id_machine))
                	        print(12)
				disp(lcd,6,l)
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
			post_request_status = post_value(str(flash),order_id)
			if post_request_status == False:
				clear_lcd(lcd)
				write_line(lcd,"POST Error",2)
				write_line(lcd,"Aborting",3)
				mark_m_cancel_all()
				sleep(5)
				return False
			disp(lcd,4,l)
			transaction = find_transaction()
			#print transaction
			while transaction == ():
				transaction = find_transaction()
				#print transaction
			if transaction[-1][5] == 0:
				#disp(lcd,5,l)
				#key = sel_mode(["A","B"])
				#if key == "A":
		                #        start_m(1)
				#	id_machine = 1
		                #elif key == "B":
		                #        start_m(2)
				#	id_machine = 2
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
			print delta
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

while 1:
	l = 1
	main(1)
