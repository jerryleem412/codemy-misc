from os import add_dll_directory
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test tree view")
root.geometry("500x600")

#Add style
style = ttk.Style()

#Pick a theme
style.theme_use("default") #clam, default, alt


#Configure treeview colors
style.configure("Treeview",
	background="white",
	foreground="black",
	rowheight=25,
	fieldbackground="white")

style.map('Treeview',
	background=[('selected', 'blue')])

#Create treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

#create treeview scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

#Create treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
my_tree.pack()

#Configure scrollbar
tree_scroll.config(command=my_tree.yview)


#Define Columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favorite Pizza", anchor=W, width=140)


#Create headings
my_tree.heading("#0", text="", anchor=W)

my_tree.heading("Name", text="Customer name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

data = [
    ["John", 1, "Pepperoni"],
    ["Mary", 2, "Cheese"],
    ["Tim", 3, "Mushroom"],
    ["Eric", 4, "Ham"],
    ["Bob", 5, "Onion"],
    ["Steve", 6, "Peppers"],
    ["Tina", 7, "Cheese"],
    ["Mark", 8, "Supreme"],
    ["Eric", 9, "Ham"],
    ["Bob", 10, "Onion"],
    ["Steve", 11, "Peppers"],
    ["Tina", 12, "Cheese"],
    ["Mark", 13, "Supreme"],
    ["Ruth", 14, "Vegan"]
]

#Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


global count
count=0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))    
    count+=1


add_frame = Frame(root)
add_frame.pack(pady=20)

#Labels
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

#Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

def add_record():
    global count
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")
    
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="Parrent", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="Parrent", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('oddrow',))
    count+=1
    #Clear boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)
#Remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

def remove_many():
    x = my_tree.selection()

    for record in x:
        my_tree.delete(record)

    pass


#Buttons
add_record = Button(root, text="Add Record", command=add_record)
add_record.pack(pady=20)

#Remove all
remove_all = Button(root, text="Remove All Records", command=remove_all)
remove_all.pack(pady=10)

#Remove 1
remove_one = Button(root, text="Remove One Selected", command=remove_one)
remove_one.pack(pady=10)

#Remove many selected
remove_many = Button(root, text="Remove many selected", command=remove_many)
remove_many.pack(pady=10)

root.mainloop()