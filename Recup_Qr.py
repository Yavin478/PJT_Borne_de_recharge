from tkinter import *

class QR_seeker(Toplevel):

    def __init__(self, callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.text=""
        self.setup_bind()
        self.withdraw()

    def setup_bind(self):
        self.bind('<KeyPress>', self.keypress)

    def keypress(self, event):
        print(event.keysym)
        if event.keysym=="Return":
            self.callback(self.text)
        else:
            self.text += str(event.char)



if __name__ == '__main__':
    def callback(text):
        print(text)
        app.destroy()
        root.destroy()

    root = Tk()
    app = QR_seeker(callback)
    root.withdraw()
    root.mainloop()


