import pygame as p
import numpy
import random as r
from random import choice
from mapGenerator import mapMain
from mapGenerator import getDoneBool
from mapGenerator import getPelletStack
from ghost import Ghost

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GREY = (128, 128, 128)
FROYALBLUE = (79, 132, 166)
BLUE = (65, 105, 225)

p.init()
res = width, height = 1200, 600
sc = p.display.set_mode(res)
clock =p.time.Clock()

pacmanSheetR = p.image.load("Pac-Man Assets\Pac-Man Sprites\pacManR.png")
pacmanSheetL = p.image.load("Pac-Man Assets\Pac-Man Sprites\pacManL.png")
pacmanSheetU = p.image.load("Pac-Man Assets\Pac-Man Sprites\pacManU.png")
pacmanSheetD = p.image.load("Pac-Man Assets\Pac-Man Sprites\pacManD.png")


global ghostDirX
global ghostDirY
ghostDirY = 1
ghostDirX = 1
wanderChoice = [ghostDirX, ghostDirY]
redGhostPosX = r.randint(0, 1200)
redGhostPosY = r.randint(0, 600)
redGhostSpeed = 3

global frameNum
global frameCount
global pacManPosX
global pacManPosY
global pacManSpeed
pacManPosX = 5
pacManPosY = 5
pacManPos = (pacManPosX, pacManPosY)
pacManSpeed = 3

pelletStack = getPelletStack()

frameNum = 0
frameCount = 0


def getImage(sheet, frame, width, height, scale, color):
    image = p.Surface((width, height))
    image.blit(sheet, (0,0), ((frame * width), 0, width, height))
    image = p.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image.convert_alpha()

def animator(sheet, spriteWidth, spriteHeight, scalar, color, pos):
    global frameNum
    global frameCount
    #show frame img
    sc.blit(getImage(sheet, frameNum, spriteWidth, spriteHeight, scalar, color), pos)
    if frameCount == 0:
        frameNum += 1
    if frameNum > 2:
        frameNum = 0

    frameCount += 1
    if frameCount == 12:
        frameCount = 0

def pacManController(xDir, yDir, currDirAnim):
    global pacManSpeed
    if getDoneBool() == True:
        if event.type == p.KEYDOWN:
            #CONTROLS
            if event.key == p.K_w:
                xDir = 0
                yDir = -1
                pacManSpeed = 3
            if event.key == p.K_s:
                xDir = 0
                yDir = 1
                pacManSpeed = 3
            if event.key == p.K_d:
                yDir = 0
                xDir = 1
                pacManSpeed = 3
            if event.key == p.K_a:
                yDir = 0
                xDir = -1
                pacManSpeed = 3

    return xDir, yDir, currDirAnim

def checkCollision(posX, posY):
    global pacManPosX
    global pacManPosY
    if posX < 0:
        pacManPosX = 1
    if posX + 48 > width:
        pacManPosX = width - 48
    if posY < 0:
        pacManPosY = 1
    if posY + 48 > height:
        pacManPosY = height - 48

def spawnGhost(posX, posY, type):
    sc.blit(getImage(ghostSpriteSheet, type, 48, 48, 1, BLACK), (posX, posY))

def moveGhost(ghostPosX, ghostPosY, ghostSpeed):
    global ghostDirX
    global ghostDirY

    if getDoneBool() == True:
        choice = 0
        lock = True
        if choice == 0:
            if ghostDirX == 1:
                ghostPosX += ghostSpeed * ghostDirX
                spawnGhost(ghostPosX, ghostPosY, 0)
            if ghostDirX == -1:
                ghostPosX += ghostSpeed * ghostDirX
                spawnGhost(ghostPosX, ghostPosY, 3)

    #    if choice == 1:
    #        if ghostDirY == 1:
    #            ghostPosY += ghostSpeed * ghostDirY
    #            spawnGhost(redGhostPosX, redGhostPosY, 1)
    #        if ghostDirY == -1:
    #            ghostPosY += ghostSpeed * ghostDirY
    #            spawnGhost(redGhostPosX, redGhostPosY, 1)

        if ghostPosX < 0:
            ghostPosX = 1
            ghostDirX *= -1
        if ghostPosX + 48 > width:
            ghostPosX = width - 48
            ghostDirX *= -1
    #    if ghostPosY < 0:
    #        ghostPosY = 1
    #        ghostDirY *= -1
    #    if ghostPosY + 48 > height:
    #        ghostPosY = height - 48
    #        ghostDirY *= -1

    return ghostPosX


currDirAnim = pacmanSheetU
xDir = 0
yDir = 0
#ghost = Ghost(48, 48)
ghostSpriteSheet = p.image.load("Pac-Man Assets\Ghosts\GhostSpriteSheet.png")

while True:
    sc.fill(p.Color(BLUE))

    for event in p.event.get():
        if event.type == p.QUIT:
            exit()
        xDir, yDir, currDirAnim = pacManController(xDir, yDir, currDirAnim)


    if xDir == 1:
        pacManPosX += pacManSpeed
        currDirAnim = pacmanSheetR
    if yDir == -1:
        pacManPosY -= pacManSpeed 
        currDirAnim = pacmanSheetU
    if xDir == -1:
        pacManPosX -= pacManSpeed 
        currDirAnim = pacmanSheetL
    if yDir == 1:
        pacManPosY += pacManSpeed 
        currDirAnim = pacmanSheetD

    wallStack = mapMain(sc, pacManPos)
    pacmanCol = p.draw.rect(sc, BLACK, (pacManPosX + 5, pacManPosY, 45, 45), 1)
    redGhostCol = p.draw.rect(sc, BLACK, (redGhostPosX + 5, redGhostPosY, 45, 45), 1)
    if wallStack != None:
        for wall in wallStack:
            if pacmanCol.colliderect(wall):
                if xDir == 1:
                    pacManSpeed = 0
                    pacManPosX -= 3
                elif xDir == -1:
                    pacManSpeed = 0
                    pacManPosX += 3
                elif yDir == 1:
                    pacManSpeed = 0
                    pacManPosY -= 3
                elif yDir == -1:
                    pacManSpeed = 0
                    pacManPosY += 3

            if redGhostCol.colliderect(wall):
                if xDir == 1:
                    redGhostSpeed = 0
                    redGhostPosX -= 3
                elif xDir == -1:
                    redGhostSpeed = 0
                    redGhostPosX += 3
                elif yDir == 1:
                    redGhostSpeed = 0
                    redGhostPosY -= 3
                elif yDir == -1:
                    redGhostSpeed = 0
                    redGhostPosY += 3

        for pellet in pelletStack:
            if pacmanCol.collidepoint(pellet):
                pelletStack.remove(pellet)
                print(len(pelletStack))

    

    checkCollision(pacManPosX, pacManPosY)
    redGhostPosX = moveGhost(redGhostPosX, redGhostPosY, redGhostSpeed)
    pacManPos = (pacManPosX, pacManPosY)
    animator(currDirAnim, 48, 48, 1, BLACK, pacManPos)
    


    

    p.display.flip()
    clock.tick(60)
    print(clock.get_fps())