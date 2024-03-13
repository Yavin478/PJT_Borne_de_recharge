print("Demarrage 'STRING.py'")
def STRING_montant(montant):
    STRING=str(abs(int(montant)))
    if (len(STRING)==0):
        return ("0,00e")
    elif (len(STRING)==1):
        return ("0,0"+STRING+"e")
    elif (len(STRING)==2):
        return ("0,"+STRING+"e")
    elif (len(STRING)==3):
        return (STRING[0]+","+STRING[1]+STRING[2]+"e")
    else:
        return (STRING[0:-2]+","+STRING[-2]+STRING[-1]+"e")

def STRING_List(tag):
    """recupère un tag en hexadecimal de 8 caractères max, stocké dans un string, et le transforme en une liste de 4 byte chacun sctocké dans une case
    la liste est ensuite répétée 4 fois pour correspondre à la façon dont les données sont écrites.
    (Pour les cartes Ultralight, même si un bloc ne contient que 4 bytes, les autres cartes ont des blocs de 16 bytes; plus de détails sur la doc du module MFRC522 et des cartes MIFARE)"""
    tag=(8*"0"+str(tag))[-8:]
    LIST=[]
    for i in range(4):
        LIST.append(int(tag[2*i:2*i+2],16))
    return LIST*4

def STRING_Tag(list,longueur=4):
    """renvoie un string de 8 caractères hexa correspondant aux données dans les l<ongueur> premières cases de liste.
    list provient de la lecture d'une carte RFID, et contient des données sous forme d'entier. Une case de la liste devrait contenir un octet de la carte"""
    tag=""
    for i in range(longueur):
        #on s'assure de bien mettre 2  caractère par octets en rajoutant des 0 au début
        tag+=(2*"0"+hex(list[i])[2:])[-2:]
    return str(((longueur*2)*"0"+str(tag))[-longueur*2:])

def STRING_getPath(chemin):
    List=chemin.split("/")
    chemin=""
    for i in range(len(List)-1):
        chemin=chemin+List[i]+"/"
    chemin=chemin[:-1]
    return chemin

def STRING_uidStrToInt(UID):
    if isinstance(UID,str):
        UID=int(UID,16)
    if not(isinstance(UID,int)):
        return("")
    return UID