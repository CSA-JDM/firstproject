import time, math, random as rand
from tkinter import *
root = Tk()
ct = "[" + time.asctime() + "]"
name = ""
def spaceshipgamerun():
    root.title("Spaceship Game")
    wleocme = Label(root, text = "Welcome to 'The Spaceship Game!'\nThe point of the game is to escape the planet you're on by determining how fast you believe you need to go.")
    wleocme.grid(row = 0, columnspan = 2), print(ct)
    username = Label(root, text = "Name:")
    username_input = Entry(root)
    quitchoice = Button(root, text = "Quit")
    quitchoice["command"] = root.destroy
    quitchoice.grid(row = 2, column = 2)
    def namedeleteandprint():
        global name
        name = username_input.get()
        username.destroy()
        username_input.destroy()
        afternameandintro()
    def afternameandintro():
        startgame = Label()
        planetcode = Label()
    username_input.bind('<Return>', lambda username_input = username_input : namedeleteandprint())
    username.grid(row = 1, column = 0, sticky = E)
    username_input.grid(row = 1, column = 1, sticky = W)
        
spaceshipgamerun()
