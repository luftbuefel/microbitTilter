from microbit import *
#import random
from random import *
import math

EMPTY_ROW = "00000"
PLAYER_BRIGHTNESS = "9"
GOAL_BRIGHTNESS = "5"

MIN_X_TILT = -550
MAX_X_TILT = 550
MIN_Y_TILT = -350
MAX_Y_TILT = 650
#this is the amount of x tilt required to move one space
X_TILT_MOVE_AMOUNT =275#220 
#this is the amount of y tilt required to move one space
Y_TILT_MOVE_AMOUNT = 250#200

#The player starts off in the center of the grid
playerX = 2
playerY = 2
#The grid is off the board by default
goalX = -1
goalY = -1
#keep track of the player score
score = 0

def moveGoal():
    global goalX
    global goalY
    goalX = randint(0,4)
    goalY = randint(0,4)
    return

def updatePlayerPosition():
    global playerX
    global playerY
    #get the tilt to use to control the player
    xValue = accelerometer.get_x()
    yValue = accelerometer.get_y()
    #set a limit on the x value
    if(xValue<MIN_X_TILT):
        xValue = MIN_X_TILT
    elif(xValue > MAX_X_TILT):
        xValue = MAX_X_TILT
    #add an offset to make the min tilt  = 0
    xValue = math.floor((xValue+abs(MIN_X_TILT))/X_TILT_MOVE_AMOUNT)
    #set a limit to the y value
    if(yValue<MIN_Y_TILT):
        yValue = MIN_Y_TILT
    elif(yValue > MAX_Y_TILT):
        yValue = MAX_Y_TILT   
    #add an offset to make the min tilt  = 0
    yValue = math.floor((yValue+abs(MIN_Y_TILT))/Y_TILT_MOVE_AMOUNT)
    #update the position of the player
    playerX = xValue
    playerY = yValue
    #display.show(str(playerX))
    return

def draw():
    global score
    screenContents = ""
    #check if the player is on the goalX
    if(playerX==goalX and playerY==goalY):
        score+=1
        moveGoal()
    #draw each row
    for i in range(0, 5):
        nextRow = EMPTY_ROW
        if(playerY == i):
            nextRow = nextRow[:playerX]+PLAYER_BRIGHTNESS+nextRow[playerX:]
        if(goalY == i):            
            nextRow = nextRow[:goalX]+GOAL_BRIGHTNESS+nextRow[goalX:]    
        if(i!=4):
            nextRow+=":"
        screenContents += nextRow
    display.show(Image(screenContents))
    return

moveGoal()
while True:
    updatePlayerPosition()    
    draw()
