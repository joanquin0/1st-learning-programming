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


from tkinter import *


root = Tk()
root.title('Listbox Widget - Group 4')
root.geometry('200x300')


def insert_item():
    listbox.insert(END, content.get())
def delete_list():
    listbox.delete(0, END)
def delete_items_selected():
    listbox.delete(ANCHOR)


label = Label(root, text = 'Insert the items below:')
label.pack()


button = Button(root, text='Insert Item', command=insert_item)
button.pack()


button_delete = Button(root, text='Delete List', command=delete_list)
button_delete.pack()


button_delete_selected = Button(root, text='Delete Selected Item',
                                command=delete_items_selected)
button_delete_selected.pack()


content = StringVar()
entry = Entry(root, textvar=content)
entry.pack()

listbox = Listbox(root)
listbox.pack()




mainloop()
