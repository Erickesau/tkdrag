from tkinter import Button, Label, Tk, Toplevel
from tkdrag import Drag
root = Tk()
root.geometry("400x400+50+50")
root["bg"] = "yellow"
top = Toplevel()
top["bg"] = "red"
top.geometry("400x400+400+150")

Drag(top, root)# make top draggable and sticky root to draw togueter
Drag(root, top)# make root draggable and sticky top to draw togueter

root.mainloop()
