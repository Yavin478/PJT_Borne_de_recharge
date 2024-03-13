import string

from evdev import InputDevice
from select import select

keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
dev = InputDevice('/dev/input/by-id/usb-©Symbol_Technologies__Inc__2006_Symbol_Bar_Code_Scanner_S_N:9A72F449E108A047B4770C9EBF8E0A00_Rev:CBRPVASA3-event-kbd')

while True:
   r,w,x = select([dev], [], [])
   for event in dev.read():
        if event.type==1 and event.value==1:
                print( keys[ event.code ] )