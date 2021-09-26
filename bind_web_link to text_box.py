######################################
#                                    #
# Just using this to test things out #
#                                    #
######################################  

from tkinter import *
from tkinter import ttk  #needed for combo box and scrollbar
from PIL import Image, ImageTk

import webbrowser

#Create root Window
root = Tk()
root.title("NetServer Tools")
root.configure(background="black") #makes background black. Can be hex value.
ico = Image.open('splash.png')    ##this and next two lines convert photo to icon and then assigns the icon for Tkinter window.
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.geometry("1300x650")
################################

def callback(url):
    webbrowser.open_new_tab(url)

link2 = Text(root, height=1, width=20, fg="blue", cursor="hand2")
link2.pack()
link2.insert(1.0, "Link")
link2.bind("<Button-1>", lambda e: callback("http://www.tutorialspoint.com"))


# link = Label(root, text="link",font=('Helveticabold', 15), fg="blue", cursor="hand2")
# link.pack()
# link.bind("<Button-1>", lambda e: callback("http://www.tutorialspoint.com"))

root.mainloop()