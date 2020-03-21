import Word_List
import random

print(Word_List.word_list)

guess_word = random.choice(Word_List.word_list)
#print(guess_word)

from tkinter import *

class Hello:
    def __init__(self, window):
        self.window = window
        self.idx = 0
        window.title("Hangman")
        window.geometry("500x500")

        self.lb = Label(master=window, text="Welcome to HangMan", font=("Calibri", 20), fg="red")
        self.lb.grid(row=0, pady=20, columnspan=2)

        self.bt = Button(master=window, text="Exit", font=("Helvetica", 15), command=sys.exit)
        self.bt.grid(row=1)

        self.bt2 = Button(master=window, text="Count", font=("Helvetica", 15), command=self.count)
        self.bt2.grid(row=1, column=1)

    def count(self):
        self.idx += 1
        self.lb.config(text="Hello World" + str(self.idx))
        return


window = Tk()
hello = Hello(window)
window.mainloop()

