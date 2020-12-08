"""

Radiobutton Widget
from Anton's group

"""

# imports the tkinter module so we can use all tkinter commands
from tkinter import *
# this statement will refer to Tkinter as tk throughout the code
import tkinter as tk


# creates the window where all objects will be put
window = Tk()
# sets the size of the window
window.geometry('300x300')
# most buttons in tkinter is the usage of multiple buttons to get an option
# on all of them, that is why there is tk.intvar
# the functionality of this is you pass in a variable var is equal to tk.intvar
# into each of these buttons
# and then when each of these buttons are selected, that variable get its
# associated value
var = tk.IntVar()
# we have this variable now as an integer variable of the tkinter class


rb1 = Radiobutton(window, variable=var, value=0, text='There is a Class!',
                  command=lambda: print(var.get()))
rb2 = Radiobutton(window, variable=var, value=1, text='There is no Class!',
                  command=lambda: print(var.get()))

# lambda is a shorthand expression you can use instead of calling the function


rb1.pack()
rb2.pack()

mainloop()
