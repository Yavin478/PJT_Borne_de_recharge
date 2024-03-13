projet_path="/".join(__file__.split("/")[:-2])+"/"

print(projet_path)

print("Démarrage 'boot.py'")
exec(open(projet_path+'PICONFLEX2000-CLIENT/launch.py').read())  # Permet de se servir directement de toutes les fonctionnalités de la box quand il est lancé (Très utile pour DEV)

if config.debugging :
    print("Attente de 3s")
    sleep(3)

try:
    exec(open(projet_path+'PICONFLEX2000-CLIENT/init.py').read())  # Effectue les premières communications avec le serveur
except:
    exec(open(projet_path+'PICONFLEX2000-CLIENT/error.py').read())  # Script de gestion et affichage des erreurs
while True:  # Boucle infinie du script
    try:
        if setting.nomBox == "Secss":
            exec(open(projet_path+'PICONFLEX2000-CLIENT/loop_secss.py').read())  # Execution du script en mode secss, se répétant jusqu'à l'arrêt du système
        else:
            exec(open(projet_path+'PICONFLEX2000-CLIENT/loop.py').read())  # Execution du script se répétant jusqu'à l'arrêt du système
    except:
        exec(open(projet_path+'PICONFLEX2000-CLIENT/error.py').read())  # Script de gestion et affichage des erreurs
