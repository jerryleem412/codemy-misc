from tkinter import *

root = Tk()
root.title('GUI test')
root.geometry("400x400")

class whatEver:
    def __init__(self, jerry):  #Master could be root or what ever  __init__ gets alled automatically.
        myFrame = Frame(jerry)
        myFrame.pack()

        self.myButton = Button(jerry, text="Click me", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Look what I did")

w = whatEver(root)




root.mainloop()