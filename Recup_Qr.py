from tkinter import *

class QR_seeker(Toplevel):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.text=""
        self.setup_bind()
        self.withdraw()

    def setup_bind(self):
        self.bind('<KeyPress>', self.keypress)
        self.bind('<Return>', self.terminate)
        self.bind('<Escape>', lambda e: self.quit_app())

    def keypress(self, event):
        self.text += str(event.char)

    def terminate(self,e):
        print(self.text)
        self.quit_app()

    def quit_app(self):
        self.master.destroy()


if __name__ == '__main__':
    root = Tk()
    app = QR_seeker(root)
    root.withdraw()
    root.mainloop()

