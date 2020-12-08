"""

Group 2 - Checkbutton

Nanual, Audrey
Flores, Ray
Morales, Rey
Launio, Princess
Padilla, Mc-Twins

Program:
   - displays the text 'chosen' once the corresponding checkbutton is clicked


"""



# imports all classes under the tkinter method
from tkinter import *   



# a function that updates the text in label 1 once the corresponding checbutton is clicked
def updatelabel_1():    
    if var1.get() == 1: # .get retrieves the text or value stored in var1
        labeltext_1.set("Chosen")   # changes text in label 1 to 'chosen'
    else:
        labeltext_1.set("")        # changes text in label 1 to ""
        
def updatelabel_2():
    if var2.get() == 1:
        labeltext_2.set("Chosen")
    else:
        labeltext_2.set("")

def updatelabel_3():
    if var3.get() == 1:
        labeltext_3.set("Chosen")
    else:
        labeltext_3.set("")

def updatelabel_4():
    if var4.get() == 1:
        labeltext_4.set("Chosen")
    else:
        labeltext_4.set("")



# Tk class is used to create a root window, whose frame is a container for other widgets
window = Tk()   
window.geometry('270x300')
window.configure(bg='powder blue')
window.title('Group 2: Checkbutton Widget')



#creates label for 'choose the animals you like' heading
L = Label(window, text='Choose the animals you like!',
           bg='powder blue', width=25, height=1,
           font=('times new roman', '13', 'bold'))
L.grid(columnspan=2)



# checkbutton for 'cat'
var1 = IntVar() # sets the variable to value, converting booleans to integers
C1 = Checkbutton(window,  text="Cat", variable=var1, onvalue=1, offvalue=0, command=updatelabel_1,
                 bg='powder blue', activebackground='light gray',
                 width=10, height=1, font=('times new roman', '12', 'italic'),
                 cursor='dot')
C1.grid(row=2, column=0)
# label
labeltext_1 = StringVar()
L1 = Label(window, textvariable=labeltext_1, bg='powder blue',
           width=10, height=1, font=('times new roman', '12'), cursor='dot')
L1.grid(row=2, column=1)
labeltext_1.set("")


# checkbutton for 'dog'
var2 = IntVar()
C2 = Checkbutton(window,  text="Dog", variable=var2, onvalue=1, offvalue=0, command=updatelabel_2,
                 bg='powder blue', activebackground='light gray',
                 width=10, height=1, font=('times new roman', '12', 'italic'),
                 cursor='dot')
C2.grid(row=3, column=0)
# label for 'chosen' or ''
labeltext_2 = StringVar()
L2 = Label(window, textvariable=labeltext_2, bg='powder blue',
           width=10, height=1, font=('times new roman', '12'), cursor='dot')
L2.grid(row=3, column=1)
labeltext_2.set("")


# checkbutton for 'panda'
var3 = IntVar()
C3 = Checkbutton(window,  text="Panda", variable=var3, onvalue=1, offvalue=0, command=updatelabel_3,
                 bg='powder blue', activebackground='light gray',
                 width=10, height=1, font=('times new roman', '12', 'italic'),
                 cursor='dot')
C3.grid(row=4, column=0)
# label for 'chosen' or ''
labeltext_3 = StringVar()
L3 = Label(window, textvariable=labeltext_3, bg='powder blue',
           width=10, height=1, font=('times new roman', '12'), cursor='dot')
L3.grid(row=4, column=1)
labeltext_3.set("")


# checkbutton for 'Tarantula'
var4 = IntVar()
C4 = Checkbutton(window,  text="Tarantula", variable=var4, onvalue=1, offvalue=0, command=updatelabel_4,
                 bg='powder blue', activebackground='light gray',
                 width=10, height=1, font=('times new roman', '12', 'italic'),
                 cursor='dot')
C4.grid(row=5, column=0)
# label for 'chosen' or ''
labeltext_4 = StringVar()
L4 = Label(window, textvariable=labeltext_4, bg='powder blue',
           width=10, height=1, font=('times new roman', '12'), cursor='dot')
L4.grid(row=5, column=1)
labeltext_4.set("")



mainloop()  # an infinite loop used to run the application


