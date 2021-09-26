from tkinter import *
from tkinter import ttk  #needed for combo box and scrollbar

bg_root = "blue"
bg_frame_space = "white"
bg_frame_cavas = "grey"
bg_cavas = "green"
bg_option_frame = "cyan"
bg_contens_frame = "red"

root = Tk()
# root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.wm_title("NPIC")
root.geometry("800x700")
root.config(background=bg_root)

def fake_command():
    pass

def test():
    print("Version: " + version_selection.get() + " Cume option: " + str(cume_option.get()))

def clear():
    for widgets in contents_frame.winfo_children():
        widgets.destroy()
    contents_frame.forget()

    root.update_idletasks()
    canvas.configure(scrollregion = canvas.bbox('all'))

    pass
def addStuff():
    clear()
    my_entries = []
    for x in range(20):
        my_entry = Entry(contents_frame)
        my_entry.insert(END, x)
        my_entry.grid(row=x, column=1, pady=5, padx=5)
        my_entries.append(my_entry)
    pass

####
#  root.update_idletasks() then my_canvas.configure(scrollregion = self.my_canvas.bbox('all'))
####


frame_space = Frame(root, bg=bg_frame_space, height=50, width=700)
frame_space.grid(row=0, column=0, columnspan=3)


#Where to design with scroolbar

canvas_frame = Frame(root, bg=bg_frame_cavas, height=500, width=700)
canvas_frame.grid(row=2, column=0, columnspan=3, sticky=W)

canvas = Canvas(canvas_frame, bg=bg_cavas, width=700, bd=2)
canvas.pack(side=LEFT, fill=BOTH, expand=1, padx=2, pady=2)

scrollbar = ttk.Scrollbar(canvas_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

contents_frame = Frame(canvas, bg=bg_contens_frame, width=700)

canvas.create_window((0,0), window=contents_frame, anchor=NW)



#End design with scrollbar

#Testing ################################################

my_entries = []
for x in range(20):
    my_entry = Entry(contents_frame)
    my_entry.grid(row=x, column=1, pady=5, padx=5)
    my_entries.append(my_entry)

#########################################################

options_frame = Frame(root, bg=bg_option_frame, height=100)
options_frame.grid(row=3, column=0, columnspan=3, sticky=W, ipadx=5)

intro_label = Label(frame_space, text="Netserver PTF Infromation Center")
intro_label.configure(font=("halvetica", 24, "bold", "roman", "underline"))
intro_label.grid(row=0, column=2)

decoration_options_frame = LabelFrame(options_frame, text="Options Selection", labelanchor=N, bd=3, relief="sunken")
decoration_options_frame.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5)

version_selection_options = ["V7R4", "V7R3", "V7R2"]
version_selection = ttk.Combobox(decoration_options_frame, values=version_selection_options, width=14)
version_selection.current(0)
version_selection.grid(row=0, column=1, columnspan=3, sticky=W, pady=5, ipady=4)

version_selection_button = Button(decoration_options_frame, text="Select", command=test, relief="raised")
version_selection_button.grid(row=0, column=0, columnspan=3,sticky=W, padx=5, pady=5)

cume_option = StringVar()
cume_option_checkbox = Checkbutton(decoration_options_frame, text="Deselect for not on cume",variable=cume_option, onvalue=1, offvalue=0, relief="groove")
cume_option_checkbox.select()
cume_option_checkbox.grid(row=1, column=0, sticky=NW, columnspan=3, padx=5, pady=5)

#Define Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Menu items
file_menu = Menu(my_menu, tearoff="off")
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=addStuff)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff="off")
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=fake_command)  #Normally it would be differernt commands, this is just for demo
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_separator()
edit_menu.add_command(label="Past", command=fake_command)

help_menu = Menu(my_menu, tearoff="off")
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help Text", command=fake_command) #Normally it would be differernt commands, this is just for demo
help_menu.add_separator()
help_menu.add_command(label="Contact", command=fake_command)
help_menu.add_separator()
help_menu.add_command(label="About", command=fake_command)



root.mainloop()