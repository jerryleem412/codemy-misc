from tkinter import *
import time
from random import randint
import threading

root = Tk()
root.title("Threading")
root.geometry("500x400")



my_label = Label(root, text="Hello there")
my_label.pack(pady=20)

def five_seconds():
    random_label.config(text="calclating")
    time.sleep(5)
    my_label.config(text="5 seconds is up" +f'Random Number:  {randint(1, 100)}')
    random_label.config(text="done")
    pass

def rando():
    random_label.config(text=f'Random Number:  {randint(1, 100)}')
    pass

def start():
    t1 = threading.Thread(target=five_seconds)
    t1.start()


my_button = Button(root, text="5 seconnds", command=start)
my_button.pack(pady=20)

my_button2 = Button(root, text="pick random nunmber", command=rando)
my_button2.pack(pady=20)

random_label = Label(root, text="")
random_label.pack(pady=20)






root.mainloop()