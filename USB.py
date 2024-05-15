print("Demarrage 'USB.py'")
from DATA import *

def get_device_id(device_name):
    if device_name == 'keyboard':
        device_name="Barcode Reader"
    else:
        device_name="BF SCAN SCAN KEYBOARD"
    try:
        result = subprocess.run(['xinput', 'list'], capture_output=True, text=True, check=True)
        lines = result.stdout.split('\n')
        for line in lines:
            if device_name in line:
                parts = line.split('id=')
                if len(parts) > 1:
                    id_part = parts[1]
                    device_id = id_part.split()[0]
                    print(device_id)
                    return device_id
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None


def command_usb(usb,type):
    id=get_device_id(usb)
    if id==None:
        return False
    command = f'xinput {type} {id}'
    os.system(command)
    return True