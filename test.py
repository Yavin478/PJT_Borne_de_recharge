from tkinter import*

root=Tk()

root.withdraw()

root.bind('<KeyPress>',lambda event:print(event.keysym))
root.bind('<Return>',lambda event:root.destroy())

root.mainloop()