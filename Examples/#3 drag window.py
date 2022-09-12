from tkinter import Button, Tk
from tkdrag import Drag
root = Tk()
dr = Drag(root)

# we can use the stop or start method to enable
# or disable dragging in windows or widgets.
Button(text="Stop dragging window",command=dr.stop, bg="#ff99dd").grid()
Button(text="Start dragging window",command=dr.start, bg="#ff99dd").grid()

root.geometry("400x400+50+50")
root.mainloop()
