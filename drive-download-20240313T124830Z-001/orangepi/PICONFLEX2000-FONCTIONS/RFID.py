print("Demarrage 'RFID.py'")
def RFID_presence():
    #if config.debugging:
    #    print("## RFID_presence ##")
    MIFAREReader.MFRC522_StopCrypto1()
    (status,backBits)=MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    #if config.debugging:
    #    print(str(status)+"  /  "+str(backBits))
    return (status==MIFAREReader.MI_OK)
def RFID_carteCheck():
    if config.debugging:
        print("## RFID_carteCheck ##")
    _time=time()
    while (time()-_time<0.5):
        if RFID_presence():
            return True
        # if config.debugging:
        #     #permet de ne passe que 2 fois dans la boucle, pour eviter de remplir la console
        #     sleep(0.3)
    return False
def RFID_waitRetireCarte():
    if config.debugging:
        print("## RFID_waitRetireCarte ##")
    _counter=1
    while RFID_carteCheck():
        MENU_clear() #Nettoie l'écran
        _counter=_counter%4+1
        hint("RETIRER LA CARTE",_counter)
def RFID_waitPresenterCarte():
    if config.debugging:
        print("## RFID_waitPresenterCarte ##")
    _counter=2
    _time0=time()
    hint("PRESENTER LA CARTE",4)
    while (time()-_time0<5):
        _time=time()
        while (time()-_time<0.5):
            if RFID_presence():
                return True
        if _counter==2:
            hint("",4)
            _counter=1
        if _counter==1:
            hint("PRESENTER LA CARTE",4)
            _counter=2
    return False

def RFID_readblock(block,uidstring):
    if config.debugging:
        print("## RFID_readblock ##")
    if len(uidstring)==8:
        if config.debugging:
            print("auth secteur "+str(block))
        #authentification pour les cartes MIFARE Classic
        key=[255,255,255,255,255,255]
        uid=STRING_List(uidstring)[0:4]
        status=MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A,block,key,uid)
        if status !=0:
            hint("! PROBLEME AUTH !",4)
            sleep(1)
            hint("",4)
    """permet de lire un block, et gère l'authentification si nécessaire (pour les cartes classic)"""
    return(MIFAREReader.MFRC522_Read(block)[0:4])

def RFID_readCarteOLD():
    while True:
        try:
            if RFID_presence():
                (status,uid)=MIFAREReader.MFRC522_SelectTagSN()
                if status==MIFAREReader.MI_OK:
                    return (int(STRING_Tag(uid)),int(STRING_Tag(MIFAREReader.MFRC522_Read(config.blockArgent)[0:8])),int(STRING_Tag(MIFAREReader.MFRC522_Read(config.blockHashCodeGuinche)[0:8])),int(STRING_Tag(MIFAREReader.MFRC522_Read(config.blockHashUID)[0:8])),int(STRING_Tag(MIFAREReader.MFRC522_Read(config.blockHashArgent)[0:8])))
        except:
            hint("! PROBLEME LECTURE !",4)
            sleep(1)
            hint("",4)
        sleep(0.01)



def RFID_readCarte():
    if config.debugging:
        print("## RFID_readCarteTEST ##")
    while True:
        try:
            if RFID_presence():
                (status,uid)=MIFAREReader.MFRC522_SelectTagSN()
                uidstring=STRING_Tag(uid,len(uid))
                if config.debugging:
                    print("uid:"+uidstring)
                if status==MIFAREReader.MI_OK:
                    argentListe      = RFID_readblock(config.blockArgent,uidstring)
                    hashGuincheListe = RFID_readblock(config.blockHashCodeGuinche,uidstring)
                    hashUIDListe     = RFID_readblock(config.blockHashUID,uidstring)
                    hashArgentListe  = RFID_readblock(config.blockHashArgent,uidstring)
                    return (uidstring,int(STRING_Tag(argentListe),16),STRING_Tag(hashGuincheListe),STRING_Tag(hashUIDListe),STRING_Tag(hashArgentListe))
            elif config.debugging:
                print("absence de carte")
        except:
            hint("! PROBLEME LECTURE !",4)
            sleep(1)
            hint("",4)
        if config.debugging:
            #permet d'essayer une seule fois par seconde de lire une carte en mode debug, pour ne pas remplir la console
            sleep(1)
        sleep(0.05)


def RFID_write(block,TAG,uidstring):
    if config.debugging:
        print("## RFID_write ##")
    tag=STRING_List(TAG)
    while True:
        try:
            if RFID_presence():
                (status,uidNew) = MIFAREReader.MFRC522_SelectTagSN()
                print("## SelectTagSN Fini ##")
                if status == MIFAREReader.MI_OK:
                    if config.debugging:
                        print("## SelectTagSN OK ##")
                    RFID_readblock(block,uidstring)
                    if config.debugging:
                        print("## MFRC522_Write ##")
                    MIFAREReader.MFRC522_Write(block,tag)
                    TAG_read=STRING_Tag(RFID_readblock(block,uidstring))
                    if TAG_read==TAG:
                        return
                    else:
                        if config.debugging:
                            print(str(TAG_read)+" / "+str(TAG))
                        hint("! ERREUR ECRITURE  !",4)
                        sleep(0.4)
                        hint("",4)
                else:
                    hint("PB ECRITURE-STATUS",4)
                    sleep(0.4)
                    hint("",4)
        except:
            hint("!PROBLEME ECRITURE!",4)
            sleep(0.4)
            hint("",4)
        if config.debugging:
            sleep(1)

def RFID_setArgent(montant,uidstring):
    #on prend le plus grand entre montant et 0, on le convertie en hexa et enlève le 0x devant.
    #puis on fait en sorte que la chaine de caractère soit de 8 caractères
    if config.debugging:
        print("## RFID_setArgent ##")
    montantHexa=( "0"*8+hex(max(0,montant))[2:] )[-8:]
    RFID_write(config.blockArgent,montantHexa,uidstring)
    RFID_write(config.blockHashArgent,CRYPT_hashage(int(montant)),uidstring)
def RFID_setHashCodeType(codeType,uidstring):
    RFID_write(config.blockHashCodeGuinche,CRYPT_hashage(codeType),uidstring)
def RFID_setHashUID(uidstring):
    RFID_write(config.blockHashUID,CRYPT_hashage(RFID_getUID()),uidstring)

def RFID_getUID():
    if config.debugging:
        print("## RFID_getUID ##")
    while True:
        try:
            if RFID_presence():
                (status,uid)=MIFAREReader.MFRC522_SelectTagSN()
                if status==MIFAREReader.MI_OK:
                    uidstring=STRING_Tag(uid,len(uid))
                    return uidstring
        except:
            hint("PROBLEME LECTURE UID",4)
            sleep(0.4)
            hint("",4)
def RFID_resetCarte(uidstring):
    if config.debugging:
        print("## RFID_resetCarte ##")
    RFID_setArgent(0,uidstring)
    RFID_setHashCodeType(config.codeGuinche,uidstring)
    RFID_setHashUID(uidstring)
