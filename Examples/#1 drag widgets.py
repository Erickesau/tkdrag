
from tkinter import *
from tkdrag import Drag
root = Tk()

label = Label(width=30, height=10, bg="#225588", borderwidth=10, relief="ridge")
label.pack()	
# let configure dragging to the label
Drag(label)

root.geometry("400x400+50+50")
root.mainloop()
