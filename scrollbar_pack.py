from tkinter import *
from tkinter import ttk  #needed for combo box and scrollbar
from tkinter import messagebox

root = Tk()
root.title("Testing")
root.configure(background="black")
root.geometry("800x600")

root.grid_columnconfigure(1, weight=1)

def press_me():
    messagebox.showinfo("Hello", "You Pressed me")

#Changing this size seems to have no effect
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
#Changes the size for the display area in put_stuff_here
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)
#Setting up the scrollbar
scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
#This is the frame to add things to.
put_stuff_here = Frame(canvas)
canvas.create_window((0,0), window=put_stuff_here, anchor="nw")

#just to test scrollbar
my_entries = []
for x in range(20):
    my_entry = Entry(put_stuff_here)
    my_entry.grid(row=x, column=1, pady=5, padx=5)
    my_entries.append(my_entry)

#Few buttons to test outside the scolled area in root
my_buton = Button(root, text="Press Me", command=press_me)
my_buton.pack(padx=10, pady=10)

my_buton = Button(root, text="Press Me", command=press_me)
my_buton.pack(padx=10, pady=10)

root.mainloop()