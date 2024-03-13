projet_path="/".join(__file__.split("/")[:-2])+"/"

print("Demarrage 'launch.py'")
exec(open(projet_path+'PICONFLEX2000-CLIENT/setting.py').read())
exec(open(projet_path+'PICONFLEX2000-CLIENT/config.py').read())
exec(open(projet_path+'PICONFLEX2000-CLIENT/importation.py').read())
exec(open(projet_path+'PICONFLEX2000-CLIENT/setup.py').read())