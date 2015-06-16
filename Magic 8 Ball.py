# Magic 8 Ball
# The user enters a question and the 8 ball randomly generates a response

from tkinter import *
from random import *

class Eight_Ball(Frame):
    """GUI that can reveal the answer to an question you can think of."""

    def __init__(self, master): # initialise the window
        super(Eight_Ball, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self): # used to create labels, buttons and test field
        # create a introduction label
        self.inst_lbl = Label(self, text = "Magic 8 Ball. What would you like to do?")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create the three buttons 'Ask', 'Clear', and 'Quit'
        self.ask_bttn = Button(self, text = "Ask", command = self.ask)
        self.ask_bttn.grid(row = 1, column = 0, sticky = W)

        self.clear_bttn = Button(self, text = "Clear", command = self.clear)
        self.clear_bttn.grid(row = 1, column = 1, sticky = W)

        self.quit_bttn = Button(self, text = "Quit", command = self.quit)
        self.quit_bttn.grid(row = 1, column = 2, sticky = W)

        # create an entry block to ask the question
        self.question_ent = Entry(self)
        self.question_ent.grid(row = 2, column = 1, sticky = W)

        # label for entry block
        self.inst_lbl = Label(self, text = "What is your question?")
        self.inst_lbl.grid(row = 2, column = 0, columnspan = 1, sticky = W)

        # create a text display for the answer
        self.answer_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.answer_txt.grid(row = 3, column = 0, columnspan = 4, sticky = W)

    # define the ask, clear, and quit methods
    def ask(self):
        answers = ["It is certain", "It is decidedly so", "Without a doubt",
                   "Yes definitely", "You may rely on it", "As I see it, yes",
                   "Most likely", "Outlook good", "Yes", "Signs point to yes",
                   "Reply hazy try again", "Ask again later", "Better not tell you now",
                   "Cannot predict now", "Concentrate and ask again", "Don't count on it",
                   "My reply is no", "My sources say no", "Outlook not so good",
                   "Very doubtful"]

        rand_answer = answers[randint(1, 20)]
        question = self.question_ent.get() # brings back contents of question field

        if question: 
            response = rand_answer
        else:
            response = "Please ask me a valid question."

        self.answer_txt.delete(0.0, END)
        self.answer_txt.insert(0.0, response)

    def clear(self):
        # clear the entry and response fields
        self.answer_txt.delete(0.0, END)
        self.question_ent.delete(0, END)

    def quit(self):
        root.destroy()

# main part of the program

root = Tk()
root.title("Magic 8 Ball")
root.geometry("300x150")

app = Eight_Ball(root)

root.mainloop()
