from tkinter import *

class recup(Tk):


    def __init__(self):
        Tk.__init__(self)
        self.attributes('-fullscreen', True)
        self.setup_bind()

    def setup_bind(self):
        self.bind('<KeyPress>', self.keypress)
        self.bind('<Escape>', self.terminate)

    def keypress(self, event):
        self.text += str(event.char)

    def terminate(self):
        print(self.text)
        self.destroy()

if __name__ == '__main__':
    screen=recup()
    screen.mainloop()
