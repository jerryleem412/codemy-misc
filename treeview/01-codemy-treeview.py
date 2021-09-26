from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test tree view")
root.geometry("500x600")

my_tree = ttk.Treeview(root)

#Define Columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

#Formate Columns
# my_tree.column("#0", width=120, minwidth=25) #0 is the place holder column...  an set width to 0 if your not having a parent child item

my_tree.column("#0", width=0, stretch=NO) #To remove the label column 

my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favorite Pizza", anchor=W, width=120)

#Create headings
# my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("#0", text="", anchor=W) #renoved text to remove the label column

my_tree.heading("Name", text="Customer name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

data = [
    ["John", 1, "Pepperoni"],
    ["Mary", 2, "Cheese"],
    ["Tim", 3, "Mushroom"],
    ["Eric", 4, "Ham"],
    ["Bob", 5, "Onion"]
]

count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]))
    count+=1


#Add Data
# my_tree.insert(parent='', index='end', iid=0, text="Parrent", values=("John", 1, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=1, text="Parrent", values=("Mary", "2", "Peperonni")) #Just to show you can use a string.
# my_tree.insert(parent='', index='end', iid=2, text="Parrent", values=("Tina", 3, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=3, text="Parrent", values=("Bob", 4, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=4, text="Parrent", values=("Erin", 5, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=5, text="Parrent", values=("Wes", 6, "Peperonni"))

#Getting rid of Parrent
# my_tree.insert(parent='', index='end', iid=0, text="", values=("John", 1, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", "2", "Peperonni")) #Just to show you can use a string.
# my_tree.insert(parent='', index='end', iid=2, text="", values=("Tina", 3, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=3, text="", values=("Bob", 4, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=4, text="", values=("Erin", 5, "Peperonni"))
# my_tree.insert(parent='', index='end', iid=5, text="", values=("Wes", 6, "Peperonni"))

# #Add Child
# my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
# my_tree.move('6', '0', '0') #item, parrent, index

my_tree.pack(pady=20)


root.mainloop()