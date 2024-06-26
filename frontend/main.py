import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



root = ttk.Window(themename='solar')
root.title('DataBase')
root.minsize(200,100)
frame = ttk.LabelFrame(root);
frame.pack()

def buttonClicked(event):
    label = ttk.Label(frame, text='Hello, World !!')
    label.pack()

button = ttk.Button(frame, text='Click Me')
button.pack()
button.bind('<Enter>',buttonClicked)

button = ttk.Button(frame, text='Click Me', bootstyle = LIGHT)
button.pack()


root.mainloop()