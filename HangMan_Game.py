### Stuff to import ###

import Word_List
import random

from tkinter import *
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import filedialog
import os

### Game ###

window = Tk()

class hangman:

    def __init__(self, window):
        self.window = window
        self.window.resizable(width=True, height=True)
        self.window.title("Hangman")

        # Title
        self.lb = Label(master=window, text="Welcome to HangMan", font=("Calibri", 20), fg="blue")
        self.lb.grid(row= 1, column= 2)

        # Starting picture
        self.photo= Image.open("1.png")
        self.photo = self.photo.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)
        self.label= Label(window, image= self.photo).grid(row=2, column=2)


        # Word to guess
        self.guess_word = random.choice(Word_List.word_list)
        self.guess_word= str(self.guess_word)
        print(self.guess_word)

        # Secret word showing with _
        self.letters_word = "_ " * len(self.guess_word)
        self.word= Label(window, text="Guess the word: " + self.letters_word, font=("Calibri", 20), fg="black").grid(row=3, column=2)


        # Start Guessing
        self.letter_label= Label(window, text="Enter a letter: ", font=("Calibri", 20), fg="black").grid(row=3, column=3)
        self.letter_input = Entry(window)
        self.letter_input.grid(row=4, column=3)
        self.letter_input = self.letter_input.get()



hangman = hangman(window)


window.mainloop()

