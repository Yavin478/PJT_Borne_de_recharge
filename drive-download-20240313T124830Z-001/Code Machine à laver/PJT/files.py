import os

def write_m(mode):
	#file = Path(mode + ".txt")
	#if file.exists():
	if os.path.isfile("normal.txt"):
		file = open(mode + ".txt","r")
		content = file.read()
		file.close()
		lines = content.split("\n")
		file = open(mode + ".txt","w")
		file.write(str(int(lines[0])+1))
		file.close()
	else:
		file = open(mode + ".txt","w")
		file.write("1")
		file.close()

def write_normal_m():
	#file = Path("/home/pi/prog/normal.txt")
	#if file.exists():
	if os.path.isfile("normal.txt"):
		file = open("normal.txt","r")
		content = file.read()
		file.close()
		lines = content.split("\n")
		file = open("normal.txt","w")
		file.write(str(int(lines[0])+1))
		file.close()
	else:
		file = open("normal.txt","w")
		file.write("1")
		file.close()
