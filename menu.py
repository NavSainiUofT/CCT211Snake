from tkinter import *
import snake
import multiplayer
import time
import os
import pickle
import pygame
import timetrial
import tkinter.messagebox

class Menu:
    
    def __init__(self, master):
        self.master =master
        self.players = "single"
        self.difficulty = "easy"
        self.location = "heaven"
        self.master.config(bg = "#4eee94")
        self.frames = [PhotoImage(file='imaSnake.gif', format = 'gif -index %i' %(i)) for i in range(2)]      
        self.label = Label(master)
        self.label.grid(row=0, column=2)

        self.label_P = Label(master, text = "Choose Player")
        self.label_P.config(font=(15), bg = "#4eee94")
        self.label_P.grid(row=1, column=2)
        #self.label_P.place(x=300,y=200,height=50,width=200)
                             
        
        self.button_SP = Button(master, text="Singleplayer", command = lambda  arg="single": self.choosePlayer(arg))
        self.button_SP.config(bg="aqua")
        self.button_SP.grid(row=2, column=1)
        self.button_MP = Button(master, text="Multiplayer", command = lambda arg="multi": self.choosePlayer(arg))
        self.button_MP.grid(row=2, column=2)
        self.button_TT = Button(master, text="Time Trial", command = lambda arg="time": self.choosePlayer(arg))
        self.button_TT.grid(row=2, column=3)
      
        self.label_L = Label(master, text = "Choose Location")
        self.label_L.config(font=(15), bg = "#4eee94")
        self.label_L.grid(row=3, column=2)
        
        self.button_WM = Button(master, text="Heaven", command = lambda arg="heaven": self.chooseLocation(arg))
        self.button_WM.config(bg="aqua")
        self.button_WM.grid(row=4, column=1)

        self.button_DM = Button(master, text="Darkness", command = lambda arg="dark": self.chooseLocation(arg))
        self.button_DM.grid(row=4, column=2)

        self.button_MM = Button(master, text="Hotline Miami", command = lambda arg="miami": self.chooseLocation(arg))
        self.button_MM.grid(row=4, column=3)

        self.label_L = Label(master, text = "Choose Difficulty")
        self.label_L.config(font=(15), bg = "#4eee94")
        self.label_L.grid(row=5, column=2)


        self.frame = Frame(master)
        self.frame.grid(row=6, columnspan=4)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=2)
        self.frame.columnconfigure(3, weight=2)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        
        
        self.button_easy = Button(self.frame, text="Easy", command = lambda  arg="easy": self.chooseDifficulty(arg))
        self.button_easy.config(bg="aqua")
        self.button_easy.grid(row=0, column=1)

        self.button_medium = Button(self.frame, text="Medium",command = lambda  arg="medium": self.chooseDifficulty(arg), width=15)
        self.button_medium.grid(row=0, column=2)

        self.button_hard = Button(self.frame, text="Hard", command = lambda  arg="hard": self.chooseDifficulty(arg))
        self.button_hard.grid(row=0, column=3)

        self.button_die = Button(self.frame, text="Nightmare", command = lambda  arg="nightmare": self.chooseDifficulty(arg))
        self.button_die.grid(row=0, column=4)

        self.button_play = Button(master, text="PLAY", font=20, command = self.play)
        self.button_play.grid(row=8, column=2)
        
        self.button_leaderboard = Button(master, text="Leaderboard", command = self.show_highscores)
        self.button_leaderboard.grid(row=0, column=1)

        
    def choosePlayer(self, player):
        
        self.players = player
        if player == "single":
            
            self.button_SP.config(bg="aqua")
            self.button_MP.config(bg="white")
            self.button_TT.config(bg="white")
        elif player== "multi":
            self.button_SP.config(bg="white")
            self.button_MP.config(bg="aqua")
            self.button_TT.config(bg="white")
        else:
            self.button_SP.config(bg="white")
            self.button_MP.config(bg="white")
            self.button_TT.config(bg="aqua")
        print(self.players)
        return

    def chooseDifficulty(self, diff):
        self.difficulty = diff
        if diff == "easy":
            self.button_easy.config(bg="aqua")
            self.button_medium.config(bg="white")
            self.button_hard.config(bg="white")
            self.button_die.config(bg="white")
        if diff =="medium":
            self.button_easy.config(bg="white")
            self.button_medium.config(bg="aqua")
            self.button_hard.config(bg="white")
            self.button_die.config(bg="white")
        if diff == "hard":
            self.button_easy.config(bg="white")
            self.button_medium.config(bg="white")
            self.button_hard.config(bg="aqua")
            self.button_die.config(bg="white")
        if diff == "nightmare":
            self.button_easy.config(bg="white")
            self.button_medium.config(bg="white")
            self.button_hard.config(bg="white")
            self.button_die.config(bg="aqua")
        print(diff)
        return
    
    def chooseLocation(self, loc):
        self.location = loc
        if loc == "heaven":
            self.button_WM.config(bg="aqua")
            self.button_DM.config(bg="white")
            self.button_MM.config(bg="white")
            
            snake.BACKGROUND = (255,255,255)
            snake.SNAKE1 = (0, 155, 0)
            snake.APPLE = (255, 0, 0)

            multiplayer.BACKGROUND = (255,255,255)
            multiplayer.SNAKE1 = (0, 155, 0)
            multiplayer.APPLE = (255, 0, 0)

            timetrial.BACKGROUND = (255,255,255)
            timetrial.SNAKE1 = (0, 155, 0)
            timetrial.APPLE = (255, 0, 0)
        if loc == "dark":
            self.button_WM.config(bg="white")
            self.button_DM.config(bg="aqua")
            self.button_MM.config(bg="white")

            snake.BACKGROUND = (0,0,0)
            snake.SNAKE1 = (0, 155, 0)
            snake.APPLE = (255, 0, 0)
            
            multiplayer.BACKGROUND = (0,0,0)
            multiplayer.SNAKE1 = (0, 155, 0)
            multiplayer.APPLE = (255, 0, 0)

            timetrial.BACKGROUND = (0,0,0)
            timetrial.SNAKE1 = (0, 155, 0)
            timetrial.APPLE = (255, 0, 0)
            
        if loc == "miami":
            self.button_WM.config(bg="white")
            self.button_DM.config(bg="white")
            self.button_MM.config(bg="aqua")

            snake.BACKGROUND = (0,0,0)
            snake.SNAKE1 = (39,253,245)
            snake.APPLE = (247,101,184)

            timetrial.BACKGROUND = (0,0,0)
            timetrial.SNAKE1 = (39,253,245)
            timetrial.APPLE = (247,101,184)
            
            multiplayer.BACKGROUND = (0,0,0)
            multiplayer.SNAKE1 = (39,253,245)
            multiplayer.APPLE = (247,101,184)
            
    


    def play(self):
        if self.players == "single":
            snake.singleplayer(self.difficulty)
            
        elif self.players == "multi":
            pygame.init()
            gameDisplay = pygame.display.set_mode((800,600))
            pygame.display.set_caption("Snake")
            multiplayer.gameLoop(False, gameDisplay)

        else:
            timetrial.singleplayer(self.difficulty, 5)
            
            
        
    def update(self, ind):

        self.frame = self.frames[ind]
        if ind == 0:
            ind += 1
        else:
            ind = 0
        self.label.configure(image=self.frame)
        root.after(200, self.update, ind)

    def show_highscores(self):
        if os.path.isfile('score.p'):
            # Load high_scores with existing dict
            with open("score.p", "rb") as f:
                high_scores = pickle.load(f)  
        # Score.p doesn't exist
        else:
            # Default with empty dict
            with open("score.p","wb") as out:
                pickle.dump({"EASY":[0,0,0], "MEDIUM": [0,0,0], "HARD": [0,0,0], "NIGHTMARE":[0,0,0]}, out)

        with open("score.p", "rb") as f:
            high_scores = pickle.load(f)
            string = "EASY: " + str(high_scores["EASY"]) + "\n" + "MEDIUM: " + str(high_scores["MEDIUM"]) + "\n" + "HARD: " + str(high_scores["HARD"]) + "\n" + "NIGHTMARE: " + str(high_scores["NIGHTMARE"])
            tkinter.messagebox.Message(title="Leaderboards", message=string)    
        

root = Tk()
root.geometry("800x600")
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)

gui = Menu(root)
root.after(100, gui.update, 0)
root.mainloop()
