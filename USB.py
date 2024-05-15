print("Demarrage 'USB.py'")
from DATA import *

def get_id_usb(usb):
    try:
        if usb=="keyboard":
            command_get_id = f'xinput list --id-only "{config.ID_keyboard}"'
        else:
            command_get_id = f'xinput list --id-only "{config.ID_scan}"'
        device_id = subprocess.check_output(command_get_id, shell=True).decode().strip()
        return device_id
    except:
        print("print_erreur device")
        return False

def command_usb(usb,type):
    id=get_id_usb(usb)
    if id==False:
        return False
    command = f'xinput {type} {id}'
    os.system(command)
    return True