import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None): #Master=None says I'm the Parrent Class
        super().__init__(master)  #super() allows inheritence from the parrent class.
        self.master = master  #In this case master is called root, set in the app veriable outside
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.say_hi()
app.create_widgets()
app.mainloop()