import Word_List
import random

print(Word_List.word_list)

guess_word = random.choice(Word_List.word_list)
#print(guess_word)

from tkinter import *
from PIL import ImageTk, Image
import os



window = Tk()

class hangman:
    def __init__(self, window):
        self.window = window
        self.idx = 0
        window.title("Hangman")
        window.geometry("500x500")

        self.lb = Label(master=window, text="Welcome to HangMan", font=("Calibri", 20), fg="red")
        self.lb.grid(row=0, pady=20, columnspan=2)

        self.bt = Button(master=window, text="Exit", font=("Helvetica", 15), command=sys.exit)
        self.bt.grid(row=7, columnspan= 3)

        self.width = 50
        self.height = 50
        #self.photo = Image.open("1.png")
        #self.photo = self.photo.resiz(self.width, self.height)
        self.photo = ImageTk.PhotoImage(Image.open("1.png"))
        self.label= Label(window, image= self.photo).grid(row=1, column=1)





hangman = hangman(window)
window.mainloop()

