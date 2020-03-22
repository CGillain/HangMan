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

window.resizable(width=True, height=True)
window.title("Hangman")

# Title
lb = Label(master=window, text="Welcome to HangMan", font=("Calibri", 20), fg="blue")
lb.grid(row= 1, column= 2)

### Loading all pics ###
# Starting picture
photo= Image.open("1.png")
photo = photo.resize((500, 500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)
label= Label(window, image= photo).grid(row=2, column=2)

# 1 wrong guess pic
photo_1= Image.open("2.png")
photo_1 = photo_1.resize((500, 500), Image.ANTIALIAS)
photo_1 = ImageTk.PhotoImage(photo_1)
#label_1= Label(window, image= photo_1).grid(row=2, column=2)

# 2 wrong guesses pic
photo_2= Image.open("3.png")
photo_2 = photo_2.resize((500, 500), Image.ANTIALIAS)
photo_2 = ImageTk.PhotoImage(photo_2)
#label_2= Label(window, image= photo_2).grid(row=2, column=2)

# 3 wrong guesses pic
photo_3= Image.open("4.png")
photo_3 = photo_3.resize((500, 500), Image.ANTIALIAS)
photo_3 = ImageTk.PhotoImage(photo_3)
#label_3= Label(window, image= photo_3).grid(row=2, column=2)

# 4 wrong guesses pic
photo_4= Image.open("5.png")
photo_4 = photo_4.resize((500, 500), Image.ANTIALIAS)
photo_4 = ImageTk.PhotoImage(photo_4)
#label_4= Label(window, image= photo_4).grid(row=2, column=2)

# 5 wrong guesses pic
photo_5= Image.open("6.png")
photo_5 = photo_5.resize((500, 500), Image.ANTIALIAS)
photo_5 = ImageTk.PhotoImage(photo_5)
#label_5= Label(window, image= photo_5).grid(row=2, column=2)

# 6 wrong guesses pic
photo_6= Image.open("7.png")
photo_6 = photo_6.resize((500, 500), Image.ANTIALIAS)
photo_6 = ImageTk.PhotoImage(photo_6)
#label_6= Label(window, image= photo_6).grid(row=2, column=2)

# 7 wrong guesses pic
photo_7= Image.open("8.png")
photo_7 = photo_7.resize((500, 500), Image.ANTIALIAS)
photo_7 = ImageTk.PhotoImage(photo_7)
#label_7= Label(window, image= photo_7).grid(row=2, column=2)

# 8 wrong guesses pic
photo_8= Image.open("9.png")
photo_8 = photo_8.resize((500, 500), Image.ANTIALIAS)
photo_8 = ImageTk.PhotoImage(photo_8)
#label_8= Label(window, image= photo_8).grid(row=2, column=2)

# 9 wrong guesses pic - Game over
photo_9= Image.open("10.png")
photo_9 = photo_9.resize((500, 500), Image.ANTIALIAS)
photo_9 = ImageTk.PhotoImage(photo_9)
#label_9= Label(window, image= photo_9).grid(row=2, column=2)

# 9 wrong guesses pic - WINNER
photo_10= Image.open("11.png")
photo_10 = photo_10.resize((500, 500), Image.ANTIALIAS)
photo_10 = ImageTk.PhotoImage(photo_10)
#label_10= Label(window, image= photo_10).grid(row=2, column=2)



# Word to guess
guess_word = random.choice(Word_List.new_word_list)
guess_word= str(guess_word)
print(guess_word)


# Start Guessing
letters_word = "_ " * len(guess_word)
word = Label(window, text="Guess the word: " + letters_word, font=("Calibri", 20), fg="black")
word.grid(row=3, column=2)

def retrieve_input(arg=None):

    result = letter.get()
    new = []
    guess_wrong_count = 0

    if result in guess_word:
        list_guess_word = list(guess_word)
        for i in list_guess_word:
            if i != result:
                i = "_ "
            new.append(i)
        letters_word= "".join(new)
        #print(letters_word)
        word.configure(text="Guess the word: " + letters_word)

    else:
        guess_wrong_count += 1
        if guess_wrong_count == 1:
            label_1= Label(window, image= photo_1).grid(row=2, column=2)

        if guess_wrong_count == 2:
            label_2 = Label(window, image=photo_2).grid(row=2, column=2)

        if guess_wrong_count == 3:
            label_3 = Label(window, image=photo_3).grid(row=2, column=2)




letter_label= Label(window, text="Guess, enter a letter: ", font=("Calibri", 20), fg="black").grid(row=3, column=3)

letter = StringVar()
letter_input = Entry(window, textvariable=letter)
letter_input.grid(row=4, column=3)
#letter_input.delete(0, 'end')

btn1= Button(window, text='Show', command=retrieve_input)
btn1.grid(row=6,column=6)

btn2=Button(window,text='Quit',
          command=window.quit).grid(row=7,column=6)

window.mainloop()




