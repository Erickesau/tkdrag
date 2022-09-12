from tkinter import Button, Label, Tk, Toplevel
from tkdrag import Drag
root = Tk()
root.geometry("400x400+50+50")
root["bg"] = "yellow"
top = Toplevel()
top["bg"] = "red"
top.geometry("400x400+400+150")
top.wm_attributes("-alpha",0.7)

lb = Label(top, text="drag this window",bg="yellow")
lb.place(x=150, y=150)
lb2 = Label(top, text="we move togueter", bg="cyan")
lb2.place(x=150, y=200)
bt = Button(text="dragme")
bt.place(x=150, y=150)

Drag(top, root)# make top draggable and sticky root to draw togueter
Drag(bt, lb, lb2)# make button draggable and sticky labels to draw togueter

root.mainloop()
