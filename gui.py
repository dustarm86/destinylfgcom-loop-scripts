import Tkinter
import tkMessageBox

window = Tkinter.Tk()
window.title("The Slightly Annoying Prog (Beta)")
window.geometry("350x250")

def scripts():
    import loop_scripts

button = Tkinter.Button(window, text = "Click here to start", command = scripts)

button.pack()
window.mainloop()



"""
from Tkinter import *
import tkMessageBox

# creates window
window = Tk()

# modify window
window.title("Test title")
window.geometry("1000x500")

button1 = Tkinter.Button(top, text="Button1", command = "loop_scripts.py")
button1.pack()

# event loop
window.mainloop()
"""
