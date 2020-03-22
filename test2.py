import tkinter as tk



window = tk.Tk()

window.title("Guessing Game")



lblInst = tk.Label(window, text = "Guess a number from 0 to 9")

lblLine0 = tk.Label(window, text = "*********************************************************************")

lblNoGuess = tk.Label(window, text = "No of Guesses: 0")

lblMaxGuess = tk.Label(window, text = "Max Guess: 3")

lblLine1 = tk.Label(window, text = "*********************************************************************")

lblLogs = tk.Label(window, text="Game Logs")

lblLine2 = tk.Label(window, text = "*********************************************************************")



# create the buttons

buttons = []

for index in range(0, 10):

    button = tk.Button(window, text=index, state=tk.DISABLED)

    buttons.append(button)





btnStartGameList = []

for index in range(0, 1):

    btnStartGame = tk.Button(window, text="Start Game")

    btnStartGameList.append(btnStartGame)



# append elements to grid

lblInst.grid(row=0, column=0, columnspan=5)

lblLine0.grid(row=1, column=0, columnspan=5)

lblNoGuess.grid(row=2, column=0, columnspan=3)

lblMaxGuess.grid(row=2, column=3, columnspan=2)

lblLine1.grid(row=3, column=0, columnspan=5)

lblLogs.grid(row=4, column=0, columnspan=5)  # row 4 - 8 is reserved for showing logs



lblLine2.grid(row=9, column=0, columnspan=5)





for row in range(0, 2):

    for col in range(0, 5):

        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns

        buttons[i].grid(row=row+10, column=col)



btnStartGameList[0].grid(row=13, column=0, columnspan=5)



window.mainloop()