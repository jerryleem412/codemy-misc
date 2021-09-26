import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

colHeadings = ['car', 'repair']
itemList = [('Hyundai', 'brakes'),('Honda', 'light'), 
            ('Lexus', 'battery'), ('Benz', 'wiper'), 
            ('Ford', 'tire'), ('Chevy', 'air'), 
            ('Chrysler', 'piston'), ('Toyota', 'brake pedal'), 
            ('BMW', 'seat')]

def buildtree(thetree, colHeadings, itemList):
    thetree['columns'] = colHeadings
    print(thetree)
    for each in colHeadings:
        thetree.column(each, width=tkFont.Font().measure(each.title()))
        thetree.heading(each, text=each.title())
    for item in itemList:
        thetree.insert('', 'end', values=item)
        for i, each in enumerate(item):
            colwidth = int(1.3*tkFont.Font().measure(each))
            if thetree.column(colHeadings[i], width=None) < colwidth:
                thetree.column(colHeadings[i], width=colwidth)

class AppBT(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = ttk.Frame(self)
        frame = StatsTree(container)

        container.pack(side="top", fill="both", expand=1)
        frame.pack(side="top", fill="y",expand=1)

class StatsTree(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        tframe = ttk.Frame(self)
        yscrollbar = ttk.Scrollbar(tframe, orient="vertical")
        tree = ttk.Treeview(tframe)

        yscrollbar.config(command=tree.yview)
        tree.config(yscrollcommand=yscrollbar.set)

        buildtree(tree, colHeadings, itemList)

        tree.pack(side="left", fill="y")
        yscrollbar.pack(side="right", fill="y")
        tframe.pack(side="top", fill="y", expand=1, padx=10, pady=10)

app = AppBT()
app.geometry("800x600")
app.mainloop()