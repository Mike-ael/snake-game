# using tkinter to simulate a snake game
#import the tkinter library
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from random import randint
class Snake:
    def __init__(self):
        self.window = Tk()
        self.window.title("Snake game")
        self.window.resizable(False, False)
        self.menubar = Menu(self.window)
        self.window.config(menu = self.menubar) #display the menu bar
        #create a pull down menu and add it to the menubar
        self.levelMenu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "choose level", menu = self.levelMenu)
        self.levelMenu.add_command(label = "Easy", command = self.setEasy)
        self.levelMenu.add_command(label = "Medium", command = self.setMedium)
        self.levelMenu.add_command(label = "Hard", command = self.setHard)
        self.sleepTime = 100
        #create popup menu
        self.optionMenu = Menu(self.window, tearoff = 0)
        self.optionMenu.add_command(label = "Resume", command = self.resumeGame)
        self.optionMenu.add_command(label = "Quit", command = self.quitGame)
        self.snakeMoving = True
        #place canvas in the window
        self.canvas = Canvas(self.window, width = 1000, height = 600, bg = "white")
        self.canvas.pack()
        self.currentKeycode = 39
        self.ball_x1_position, self.ball_y1_position, self.ball_x2_position, self.ball_y2_position = 0, 0, 0, 0
        self.create_ball()
        self.setFirstSnakePart()
        #bind popup menu to the canvas
        self.canvas.bind("<Return>", self.processPopup)
        self.canvas.bind("<Key>", self.processDirectionKeys)
        self.canvas.focus_set()
        self.notFailed = True
        self.moveSnake()
        self.window.mainloop()
    #This function creates the first part of the snake
    #it is called when the game starts or when a player fails and wishes to continue
    def setFirstSnakePart(self):
        self.snake_parts = []
        self.numberOfParts = 1
        self.snake_parts_head_x_position = []
        self.snake_parts_head_x_position.append(40)
        self.snake_parts_head_y_position = []
        self.snake_parts_head_y_position.append(40)
        self.snake_parts_tail_x_position = []
        self.snake_parts_tail_x_position.append(self.snake_parts_head_x_position[0] - 20)
        self.snake_parts_tail_y_position = []
        self.snake_parts_tail_y_position.append(self.snake_parts_head_y_position[0] - 20)
    #This function creates the ball at a random position
    #it is called as soon as the snake head touches the current ball position
    def create_ball(self):
        self.ball_x1_position, self.ball_y1_position = randint(0, 980), randint(0, 580)
        self.ball_x2_position, self.ball_y2_position = self.ball_x1_position + 20, self.ball_y1_position + 20
        self.canvas.create_oval(self.ball_x1_position, self.ball_y1_position, self.ball_x2_position,\
                                self.ball_y2_position, fill = "purple", tags = "ball")
    #This function is responsible for moving the snake
    #the snake is a list of rectangles(or squares), it passes the position of the first rectangle to the
    #second and that of the second to the third and so on. It then moves the position of the head by constant
    def moveSnake(self):
        while self.snakeMoving and self.notFailed:
            for i in range(self.numberOfParts):
                self.snake_parts.append(self.canvas.create_rectangle(self.snake_parts_tail_x_position[i], self.snake_parts_tail_y_position[i], \
                                            self.snake_parts_head_x_position[i], self.snake_parts_head_y_position[i], \
                                             fill="green", tags="snake"))
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            #To check if the snake head has touched the ball position
            if (self.snake_parts_head_x_position[0] - 30 <= self.ball_x1_position <= self.snake_parts_head_x_position[0] + 25 or \
                    self.snake_parts_tail_x_position[0] - 30 <= self.ball_x1_position <= self.snake_parts_tail_x_position[0] + 25) and \
                    (self.snake_parts_head_y_position[0] - 30 <= self.ball_y1_position <= self.snake_parts_head_y_position[0] + 25 or \
                    self.snake_parts_tail_y_position[0] - 30 <= self.ball_y1_position <=  self.snake_parts_tail_y_position[0] + 25) and \
                    (self.snake_parts_head_x_position[0] - 30 <= self.ball_x2_position <= self.snake_parts_head_x_position[0] + 25 or
                    self.snake_parts_tail_x_position[0] - 30 <= self.ball_x2_position <= self.snake_parts_tail_x_position[0] + 25) and \
                    (self.snake_parts_head_y_position[0] - 30 <= self.ball_y2_position <= self.snake_parts_head_y_position[0] + 25 or \
                    self.snake_parts_tail_y_position[0] - 30 <= self.ball_y2_position <= self.snake_parts_tail_y_position[0] + 25):
                self.canvas.after(0)
                self.canvas.update()
                self.canvas.delete("ball")
                self.create_ball()
                self.numberOfParts += 1
                self.snake_parts_head_x_position.append(0)
                self.snake_parts_head_y_position.append(0)
                self.snake_parts_tail_x_position.append(0)
                self.snake_parts_tail_y_position.append(0)
            if self.currentKeycode == 37:#left arrow key
                i = self.numberOfParts - 1
                while i > 0:
                    self.snake_parts_tail_x_position[i] = self.snake_parts_tail_x_position[i - 1]
                    self.snake_parts_head_x_position[i] = self.snake_parts_head_x_position[i - 1]
                    self.snake_parts_head_y_position[i] = self.snake_parts_head_y_position[i - 1]
                    self.snake_parts_tail_y_position[i] = self.snake_parts_tail_y_position[i - 1]
                    i -= 1
                self.snake_parts_head_x_position[0] -= 20
                self.snake_parts_tail_x_position[0] -= 20
            elif self.currentKeycode == 38:#up arrow key
                i = self.numberOfParts - 1
                while i > 0:
                    self.snake_parts_tail_x_position[i] = self.snake_parts_tail_x_position[i - 1]
                    self.snake_parts_head_x_position[i] = self.snake_parts_head_x_position[i - 1]
                    self.snake_parts_tail_y_position[i] = self.snake_parts_tail_y_position[i - 1]
                    self.snake_parts_head_y_position[i] = self.snake_parts_head_y_position[i - 1]
                    i -= 1
                self.snake_parts_head_y_position[0] -= 20
                self.snake_parts_tail_y_position[0] -= 20
            elif self.currentKeycode == 39:#right arrow key
                i = self.numberOfParts - 1
                while i > 0:
                    self.snake_parts_tail_x_position[i] = self.snake_parts_tail_x_position[i - 1]
                    self.snake_parts_head_x_position[i] = self.snake_parts_head_x_position[i - 1]
                    self.snake_parts_head_y_position[i] = self.snake_parts_head_y_position[i - 1]
                    self.snake_parts_tail_y_position[i] = self.snake_parts_tail_y_position[i - 1]
                    i -= 1
                self.snake_parts_head_x_position[0] += 20
                self.snake_parts_tail_x_position[0] += 20
            else:#down arrow key
                i = self.numberOfParts - 1
                while i > 0:
                    self.snake_parts_tail_y_position[i] = self.snake_parts_tail_y_position[i - 1]
                    self.snake_parts_head_y_position[i] = self.snake_parts_head_y_position[i - 1]
                    self.snake_parts_tail_x_position[i] = self.snake_parts_tail_x_position[i - 1]
                    self.snake_parts_head_x_position[i] = self.snake_parts_head_x_position[i - 1]
                    i -= 1
                self.snake_parts_head_y_position[0] += 20
                self.snake_parts_tail_y_position[0] += 20
            #call function to check if snake head is at the boundary
            self.checkBoundary()
            if self.checkHeadBodyConnectionFail():
                self.notFailed = tkinter.messagebox.askyesno("askyesno", "failed!!!\nplay again?")
                if self.notFailed == True:
                    self.snake_parts_head_x_position.pop()
                    self.snake_parts_head_y_position.pop()
                    self.snake_parts_tail_x_position.pop()
                    self.snake_parts_tail_y_position.pop()
                    self.snake_parts.pop()
                    self.currentKeycode = 39
                    self.numberOfParts = 0
                    self.setFirstSnakePart()
                    continue
                else:
                    self.window.destroy()

            self.canvas.delete("snake")
            for counter in range(len(self.snake_parts)):
                self.snake_parts.pop()
    def processDirectionKeys(self, event):
        if event.keycode == 37:
            if self.currentKeycode != 39:
                self.snake_parts_head_x_position[0], self.snake_parts_tail_x_position[0] = self.snake_parts_tail_x_position[0],\
                                                                                           self.snake_parts_head_x_position[0]
                self.currentKeycode = 37
        elif event.keycode == 38:
            if self.currentKeycode != 40:
                self.snake_parts_head_y_position[0], self.snake_parts_tail_y_position[0] = self.snake_parts_tail_y_position[0], \
                                                                                           self.snake_parts_head_y_position[0]
                self.currentKeycode = 38
        elif event.keycode == 39:
            if self.currentKeycode != 37:
                self.snake_parts_head_y_position[0], self.snake_parts_tail_y_position[0] = self.snake_parts_tail_y_position[0], \
                                                                                           self.snake_parts_head_y_position[0]
                self.currentKeycode = 39
        elif event.keycode == 40:
            if self.currentKeycode != 38:
                self.snake_parts_head_x_position[0], self.snake_parts_tail_x_position[0] = self.snake_parts_tail_x_position[0], \
                                                                                               self.snake_parts_head_x_position[0]
                self.currentKeycode = 40
    def checkBoundary(self):
        if self.snake_parts_head_x_position[0] < 0:
            self.snake_parts_head_x_position[0] = 980
            self.snake_parts_tail_x_position[0] = 1000

        if self.snake_parts_head_y_position[0] < 0:
            self.snake_parts_head_y_position[0] = 580
            self.snake_parts_tail_y_position[0] = 600

        if self.snake_parts_head_x_position[0] > 1000:
            self.snake_parts_head_x_position[0] = 20
            self.snake_parts_tail_x_position[0] = 0

        if self.snake_parts_head_y_position[0] > 600:
            self.snake_parts_head_y_position[0] = 20
            self.snake_parts_tail_y_position[0] = 0

    def checkHeadBodyConnectionFail(self):
        if (self.numberOfParts < 4):
            return False
        if self.currentKeycode == 40 or self.currentKeycode == 39:
            for i in range(4, self.numberOfParts):
                if self.snake_parts_head_x_position[0] == self.snake_parts_head_x_position[i] and \
                        self.snake_parts_head_y_position[0] == self.snake_parts_head_y_position[i]:
                    print(self.snake_parts_head_x_position[0], self.snake_parts_head_x_position[i])
                    return True
        if self.currentKeycode == 38 or self.currentKeycode == 37:
            for i in range(4, self.numberOfParts):
                if self.snake_parts_head_x_position[0] == self.snake_parts_head_x_position[i] and\
                        self.snake_parts_head_y_position[0] == self.snake_parts_head_y_position[i]:
                    print(self.snake_parts_head_x_position[0], self.snake_parts_tail_x_position[i])
                    return True
        return False

    def setEasy(self):
        self.sleepTime = 40

    def setMedium(self):
        self.sleepTime = 20

    def setHard(self):
        self.sleepTime = 0

    def processPopup(self, event):
        self.snakeMoving = False
        self.optionMenu.post(event.x, event.y)

    def resumeGame(self):
        self.snakeMoving = True
        self.moveSnake()

    def quitGame(self):
        self.window.destroy()

Snake()