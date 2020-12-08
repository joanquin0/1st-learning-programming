"""

Group 4 - Listbox

Golosinda, Kenneth
Alabastro, Chryse
Galope, Reznee

Program:
    1 - type in the input box
    2 - insert the input (using the insert button)
    3 - the input will be added to the list
    (you can delete items and delete the entire list)

"""


#imports all classes
from tkinter import *


# creates the window where the widgets will be displayed
root = Tk()
root.title('Listbox Widget - Group 4')
root.geometry('200x300')


# function for 'insert item' button
def insert_item():
    listbox.insert(END, content.get())
        # means to insert the input value in 'content' to the end of the list
    content.set("")
# function for 'delete list' button
def delete_list():
    listbox.delete(0, END)
        # (0, END) means from the beginning to the end of the list
# function for 'delete selected item' button
def delete_item_selected():
    listbox.delete(ANCHOR)
        # ANCHOR means


# creates label for 'insert the items below'
label = Label(root, text='Insert the items below:')
label.pack()


# creates button for 'insert item'
button = Button(root, text='Insert Item', command=insert_item)
button.pack()


# creates button for 'delete list'
button_delete = Button(root, text='Delete List', command=delete_list)
button_delete.pack()


# creates button for 'delete selected item'
button_delete_selected = Button(root, text='Delete Selected Item',
                                command=delete_item_selected)
button_delete_selected.pack()


# creates entry for any input (where the user types)
content = StringVar()
entry = Entry(root, textvar=content)
entry.pack()


#creates the listbox
listbox = Listbox(root)
listbox.pack()



mainloop()
