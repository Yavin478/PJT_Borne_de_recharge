print("Demarrage 'CRYPT.py'")
def CRYPT_hashage(data):
    seed(str(data)+str(config.codeHash))
    seed(random())
    return hex(int(str(random()).replace("0.",""))).replace("0x","")[:8]
    #on prend le nombre décimal en 0 et 1 renvoyé par random, on retire le "0."
    #convertie l'entier qui en découle en héxadécimale (revoyé par hex(), sous forme d'une strig commançant par '0x')
    #et on enlève le "0x" au début et ne garde que les 8 premiers caractère (pour faire 4 octets)

def CRYPT_HashDossier(path,noList):
    digest = hashlib.sha1()

    for root, dirs, files in os.walk(path):
        for names in files:
            file_path = os.path.join(root, names)

            bool_Continue=False
            for No in noList:
                if No in file_path:
                    bool_Continue=True
            if bool_Continue:
                continue

            print(file_path)
            digest.update(hashlib.sha1(file_path[len(path):].encode()).digest())

            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f_obj:
                    while True:
                        buf = f_obj.read(1024 * 1024)
                        if not buf:
                            break
                        digest.update(buf)

    return digest.hexdigest()