projet_path="/".join(__file__.split("/")[:-2])+"/"

print("Demarrage 'error.py'")
error=traceback.format_exc()
print(error)
errorList=error.replace(" ","").replace("File","").replace("line","").replace("in","").split("\n")
errortype=errorList[-2]
hint(errortype,1)
hint("",2)
hint("",3)
hint("",4)
DATA_add(projet_path+"PICONFLEX2000-LOGS/LOG_ERROR.txt",error)
sleep(5)
if errortype in ["SystemExit","KeyboardInterrupt"]:
    hint("Systeme Interrompu",2)
    hint("a distance",3)
    hint("ne pas reboot!",4)
    REZAL_exit()
for i in range(len(errorList)):
    if i<=2:
        hint(errorList[i],i+2)
    else:
        CLAVIER_get()
        hint(errorList[i-2],2)
        hint(errorList[i-1],3)
        hint(errorList[i],4)
CLAVIER_get()
REZAL_restart()
