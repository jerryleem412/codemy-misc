#Imports
from tkinter import *

#Create base windows called root (name can be anything obviously)
root = Tk() #Creates tkinter object
root.title("Hello World") #Windows Title
root.geometry("700x500") #in pixcels
root.iconbitmap(r"C:\Users\JerryMckee\Pictures\splash.ico") #Creates icon to use for windows, must use the r ()

my_entries = []

def something():
    entry_list = ''

    for entries in my_entries:
        entry_list = entry_list = str(entries.get()) + '\n'
        my_label.config(text=entry_list)
        print(str(entries.get()))
        print(entry_list)

for x in range(5):
    my_entry = Entry(root)
    my_entry.grid(row=0, column=x, pady=5, padx=5)
    my_entries.append(my_entry)

my_button = Button(root, text="Click Me", command=something)
my_button.grid(row=1, column=0, pady=20)

my_label = Label(root, text='')
my_label.grid(row=2, column=0, pady=20)

#Loop
root.mainloop()