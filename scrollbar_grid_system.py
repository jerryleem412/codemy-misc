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
main_frame = Frame(root, bg='yellow', width=700, height=500)
main_frame.grid(row=0, column=0, sticky=NSEW, columnspan=3)
#Changes the size for the display area in put_stuff_here
canvas = Canvas(main_frame, bg='blue', width=700, height=500)
canvas.pack(side=LEFT, fill=BOTH, expand=1)
#Setting up the scrollbar
scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
#This is the frame to add things to.
put_stuff_here = Frame(canvas, bg="green")
canvas.create_window((0,0), window=put_stuff_here, anchor="nw")

#just to test scrollbar
my_entries = []
for x in range(20):
    my_entry = Entry(put_stuff_here)
    my_entry.grid(row=x, column=1, pady=5, padx=5)
    my_entries.append(my_entry)

#Few buttons to test outside the scolled area in root
my_buton = Button(root, text="Press Me", command=press_me)
my_buton.grid(row=1, column=0, padx=10, pady=10)

my_buton = Button(root, text="Press Me", command=press_me)
my_buton.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()