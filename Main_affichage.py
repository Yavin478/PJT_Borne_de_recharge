from Template_page import Page, Size, path_img_bg, path_img_fg, ratio_square
from Recup_Qr import QR_seeker
from tkinter import *


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

    def Qr_waiter(self):
        Page(self)
        QR_seeker(self)


if __name__ == "__main__":
    root=MainApp()
    root.Qr_waiter()
    root.mainloop()