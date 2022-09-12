# lets make a small programm to try	
from tkinter import *
from tkdrag import Drag
root = Tk()

label = Label(width=30, height=10, bg="#225588", borderwidth=10, relief="ridge")
label.grid()

# you can make an objet and later use stop or start method to stop or start dragging.
dl = Drag(label)

# we can call the stop or start method to enable or disable dragging
button = Button(text="stop drag label",command=dl.stop, bg="#ff99dd")
button.grid()
button2 = Button(text="start drag label",command=dl.start, bg="#ff99dd")
button2.grid()

# configure drag is easy, make both buttons draggable too.
Drag(button)
Drag(button2)

root.geometry("400x400+50+50")
root.mainloop()
