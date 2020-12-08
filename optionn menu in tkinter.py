from tkinter import*
root = Tk()
root.title("Option menu")
root.geometry('400x450')
def print_answers():
    print("Q:{} A:{}".format(tkvarq.get(),answer_entry.get))
    return None
questions = ["what is your name",
             "why mcm?",
             "m cm is the best school of you?",
             "mcm is?"]

tkvarq = StringVar(root)
tkvarq.set(questions[0])
question_menu = OptionMenu(root, tkvarq, *questions)
question_menu.pack()
answer_entry = Entry(root, width=20)
answer_entry.pack()
submit_button = Button(root, text='Submit', command=print_answers)
submit_button.pack()
root.mainloop()