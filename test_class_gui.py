from tkinter import *

bg_root = "blue"
bg_frame_space = "white"
bg_frame_cavas = "red"
bg_cavas = "green"
bg_option_frame = "cyan"

root = Tk()
# root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.wm_title("Title")
root.geometry("600x400")
root.config(background=bg_root)

def fake_command():
    pass

frame_space = Frame(root, bg=bg_frame_space, height=50, width=600)
frame_space.grid(row=0, column=0, columnspan=3, sticky=W)

canvas_frame = Frame(root, bg=bg_frame_cavas, height=300, width=600)
canvas_frame.grid(row=2, column=0, columnspan=3, sticky=W)

options_frame = Frame(root, bg=bg_option_frame)
options_frame.grid(row=3, column=0, columnspan=3, sticky=W, ipadx=5)


my_label = Label(options_frame, text="Version Select")
my_label.grid(row=0, column=0, sticky=NW)

my_label = Label(options_frame, text="on/off")
my_label.grid(row=0, column=1, sticky=NW)

my_label = Label(options_frame, text="select button")
my_label.grid(row=0, column=2, sticky=NW)

#Define Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Menu items
file_menu = Menu(my_menu, tearoff="off")
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=fake_command)
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