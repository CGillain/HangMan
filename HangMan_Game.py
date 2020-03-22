### Stuff to import ###

import Word_List

import random
from tkinter import *
from PIL import ImageTk, Image
from string import ascii_lowercase
from tkinter import messagebox

### Game ###

window = Tk()

#####------------------------------------------------------------------
### Loading all pics ###
# Starting picture
photo= Image.open("1.png")
photo = photo.resize((500, 500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)


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

# 10 wrong guesses pic - WINNER
photo_10= Image.open("11.png")
photo_10 = photo_10.resize((500, 500), Image.ANTIALIAS)
photo_10 = ImageTk.PhotoImage(photo_10)
#label_10= Label(window, image= photo_10).grid(row=2, column=2)

photos = [photo, photo_1, photo_2, photo_3,photo_4, photo_5, photo_6, photo_7, photo_8, photo_9]

#####------------------------------------------------------------------




# Intial window
window.title("Hangman")
Welcome = Label(master=window, text="Welcome to HangMan", font=("Calibri", 20), fg="blue")
Welcome.grid(row= 1, column= 1)

# Word list
word_list= Word_List.new_word_list

def NewGame():
    global TheWordWithDashes
    global NumberOfGuesses

    NumberOfGuesses= 0
    photo_label.config(image=photos[0])

    # Word to guess
    the_word = random.choice(word_list)
    the_word = str(the_word)
    print(the_word)
    TheWordWithDashes=" ".join(the_word)
    DashedWord.set(" ".join("_"*len(the_word)))

def letterguess(letter):
    global NumberOfGuesses
    if NumberOfGuesses < 9:
        txt= list(TheWordWithDashes)
        guessed= list(DashedWord.get())
        if TheWordWithDashes.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c]= letter
                DashedWord.set("".join(guessed))
                if DashedWord.get() == TheWordWithDashes:
                    messagebox.showinfo("Hangman", "Congratulations! You WONNNNNNN")

        else:
            NumberOfGuesses += 1
            photo_label.config(image=photos[NumberOfGuesses])
            if NumberOfGuesses >= 9:
                messagebox.showwarning("Hangman", "GAME OVER!!!")



photo_label= Label(window)
photo_label.grid(row=2, column=0, columnspan=3, padx=10, pady=40)
photo_label.config(image= photos[0])


DashedWord= StringVar()
Label(window, textvariable=DashedWord, font=("Consolas 24 bold")).grid(row=2, column=3, columnspan= 6, padx=10)


# Creating keyboard for input
n= 0
for c in ascii_lowercase:
    Button(window, text=c, command=lambda c=c: letterguess(c), font=("Calibri", 18), width= 4).grid(
        row=3+n//9, column=3+n%9
    )
    n += 1


Button(window, text= "New\nGame", command= lambda:NewGame(), font=("Calibri 18 bold")).grid(row=5, column=11, sticky="NSWE")

NewGame()



window.mainloop()

