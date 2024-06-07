from tkinter import *
from PIL import ImageTk



class A:
    def _init_(self,root1):
        self.root = root1
        self.root.title("Transparent label")
        self.root.geometry('1000x626+100+30')

        self.bg = ImageTk.PhotoImage(file="bgImage.png")

        canvas = Canvas(self.root)
        canvas.create_image(0, 0, image=self.bg, anchor=NW)
        canvas.pack(fill="both", expand=True)


root = Tk()
obj = A(root)
root.mainloop()


A > _init_()