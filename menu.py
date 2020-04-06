from tkinter import *
import snake
import time
import os

class Menu:
    def __init__(self, master):
        self.master =master
        
        
        self.frames = [PhotoImage(file='imaSnake.gif', format = 'gif -index %i' %(i)) for i in range(2)]      
        self.label = Label(master)
        self.label.pack()

        self.label_P = Label(master, text = "Play")
        self.label_P.place(x=350,y=250,height=50,width=100)
                             
        
        self.button_SP = Button(master, text="Single Player", command = self.singlePlayer)
        self.button_SP.place(x=250,y=300,height=50,width=100)
        self.button_MP = Button(master, text="Multi Player")
        self.button_MP.place(x=450,y=300,height=50,width=100)
      
        
        self.button_WM = Button(master, text="Heaven")
        self.button_WM.place(x=150,y=400,height=50,width=75)

        self.button_DM = Button(master, text="Darkness")
        self.button_DM.place(x=250,y=400,height=50,width=75)

        self.button_MM = Button(master, text="Hotline Miami")
        self.button_MM.place(x=350,y=400,height=50,width=120)


        self.button_easy = Button(master, text="Easy")
        self.button_easy.place(x=150,y=500,height=50,width=75)

        self.button_medium = Button(master, text="Medium")
        self.button_medium.place(x=250,y=500,height=50,width=75)

        self.button_hard = Button(master, text="Hard")
        self.button_hard.place(x=350,y=500,height=50,width=75)

        self.button_die = Button(master, text="You aint gonna survive")
        self.button_die.place(x=450,y=500,height=50,width=200)

        
    def singlePlayer(self):
        
        snake.singleplayer("easy")
        
    def update(self, ind):

        self.frame = self.frames[ind]
        if ind == 0:
            ind += 1
        else:
            ind = 0
        self.label.configure(image=self.frame)
        root.after(300, self.update, ind)
   
            
            
            
        

root = Tk()
root.geometry("800x600")
gui = Menu(root)
root.after(100, gui.update, 0)
root.mainloop()
