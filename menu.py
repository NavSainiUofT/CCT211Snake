from tkinter import *
import snake
import multiplayer
import time
import os
import pygame
import timetrial

class Menu:
    
    def __init__(self, master):
        self.master =master
        self.players = "single"
        self.difficulty = "easy"
        self.location = "heaven"
        self.master.config(bg = "#4eee94")
        self.frames = [PhotoImage(file='imaSnake.gif', format = 'gif -index %i' %(i)) for i in range(2)]      
        self.label = Label(master)
        self.label.pack()

        self.label_P = Label(master, text = "Choose Player")
        self.label_P.config(font=(15), bg = "#4eee94")
        self.label_P.place(x=300,y=200,height=50,width=200)
                             
        
        self.button_SP = Button(master, text="Single Player", command = lambda  arg="single": self.choosePlayer(arg))
        self.button_SP.config(bg="aqua")
        self.button_SP.place(x=200,y=250,height=35,width=100)
        self.button_MP = Button(master, text="Multi Player", command = lambda arg="multi": self.choosePlayer(arg))
        self.button_MP.place(x=400,y=250,height=35,width=100)
        self.button_TT = Button(master, text="Time Trial", command = lambda arg="time": self.choosePlayer(arg))
        self.button_TT.place(x=600,y=250,height=35,width=100)
      
        self.label_L = Label(master, text = "Choose Location")
        self.label_L.config(font=(15), bg = "#4eee94")
        self.label_L.place(x=300,y=300,height=50,width=200)
        
        self.button_WM = Button(master, text="Heaven", command = lambda arg="heaven": self.chooseLocation(arg))
        self.button_WM.config(bg="aqua")
        self.button_WM.place(x=200,y=350,height=35,width=75)

        self.button_DM = Button(master, text="Darkness", command = lambda arg="dark": self.chooseLocation(arg))
        self.button_DM.place(x=350,y=350,height=35,width=75)

        self.button_MM = Button(master, text="Hotline Miami", command = lambda arg="miami": self.chooseLocation(arg))
        self.button_MM.place(x=500,y=350,height=35,width=120)

        self.label_L = Label(master, text = "Choose Difficulty")
        self.label_L.config(font=(15), bg = "#4eee94")
        self.label_L.place(x=300,y=400,height=50,width=200)
        
        self.button_easy = Button(master, text="Easy", command = lambda  arg="easy": self.chooseDifficulty(arg))
        self.button_easy.config(bg="aqua")
        self.button_easy.place(x=150,y=450,height=35,width=75)

        self.button_medium = Button(master, text="Medium",command = lambda  arg="medium": self.chooseDifficulty(arg))
        self.button_medium.place(x=275,y=450,height=35,width=75)

        self.button_hard = Button(master, text="Hard", command = lambda  arg="hard": self.chooseDifficulty(arg))
        self.button_hard.place(x=400,y=450,height=35,width=75)

        self.button_die = Button(master, text="You aint gonna survive", command = lambda  arg="die": self.chooseDifficulty(arg))
        self.button_die.place(x=525,y=450,height=35,width=200)

        self.button_play = Button(master, text="play", font=20, command = self.play)
        self.button_play.place(x=350,y=500,height=50,width=100)

        
    def choosePlayer(self, player):
        
        self.players = player
        if player == "single":
            
            self.button_SP.config(bg="aqua")
            self.button_MP.config(bg="white")
        else:
            self.button_SP.config(bg="white")
            self.button_MP.config(bg="aqua")
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
        if diff == "die":
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
        
            
            
            
        

root = Tk()
root.geometry("800x600")
gui = Menu(root)
root.after(100, gui.update, 0)
root.mainloop()
