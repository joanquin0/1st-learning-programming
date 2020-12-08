"""

Group 3 - Text

Ang, Matthew
Tan, Andre
Buquia, Arnulfo
Marcellones, Jasper
Simborio, Darwin

Program:
    1 - input anything in the 1st textbox
    2 - press button
    3 - copies the input from the 1st textbox

"""



from tkinter import *


tktk = Tk()
tktk.geometry('300x400')
tktk.title('Textbox Widget - Group 3')


def get_input():
    inpVal = textBox.get('1.0', 'end-1c')
    textBox2.insert(INSERT, inpVal)


textBox = Text(tktk, height=5, width=30, font=('Times New Roman', 12))
textBox.pack()


buttonPress = Button(tktk, height=1, width=10, text='Press me',
                     command=get_input, font=('Verdana', 12))
buttonPress.pack()


textBox2 = Text(tktk, height=5, width=30, font=('Verdana', 12))
textBox2.pack()


mainloop()
