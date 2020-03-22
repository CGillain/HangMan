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

        self.letters_word = "_ " * len(self.guess_word)
        #print(type(self.letters_word))
        self.word= Label(window, text="Guess the word: " + self.letters_word, font=("Calibri", 20), fg="black").grid(row=3, column=2)

        # Start Guessing
        self.letter_label= Label(window, text="Enter a letter: ", font=("Calibri", 20), fg="black").grid(row=3, column=3)

        self.letter_input = Entry(window)
        self.letter_input.grid(row=4, column=3)
        # self.letter_input = str(self.letter_input)
        self.letter_input = self.letter_input.get()
        #print(type(self.letter_input))


        # Check if letter in word

        self.letter_input = Entry(window)
        self.letter_input.grid(row=4, column=3)
        # self.letter_input = str(self.letter_input)
        self.letter_input = self.letter_input.get()

        if self.letter_input in self.guess_word:
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"
            self.alphabet.replace(self.letter_input, "")
            self.letters_word_1= self.letters_word.replace(self.alphabet, "_ ")
            self.word_1 = Label(window, text="Guess the word: " + self.letters_word_1, font=("Calibri", 20),
                              fg="black").grid(row=3, column=2)

        else:
            self.photo_2= Image.open("2.png")
            self.photo_2 = self.photo_2.resize((500, 500), Image.ANTIALIAS)
            self.photo_2 = ImageTk.PhotoImage(self.photo_2)
            self.label_2= Label(window, image= self.photo_2).grid(row=2, column=2)



hangman = hangman(window)


window.mainloop()

