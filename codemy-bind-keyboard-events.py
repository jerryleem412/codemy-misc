from tkinter import *

root = Tk()
root.title("Test Program")
root.geometry("400x400")

def clicker(event):
    myLabel = Label(root, text="You clicked me" + str(event.x) + " " + str(event.y))  #event. gives differernt info
    myLabel.pack()


#Using events and bind
myButton = Button(root, text="Click Me")
myButton.bind("<Button-3>", clicker)  #Button-1 is left, Button-3 is right, Button-2 is Middle other options: <leave> <FocusIn> <FocusOut> <Enter> <Return> <Key>
myButton.pack(pady=20)


root.mainloop()