import pygame as p
import numpy
from random import choice
from mapGenerator import mapMain

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

global frameNum
global frameCount
frameNum = 0
frameCount = 0


def getImage(sheet, frame, width, height, scale, color):
    image = p.Surface((width, height))
    image.blit(sheet, (0,0), ((frame * width), 0, width, height))
    image = p.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image.convert_alpha()

def animator(sheet, spriteWidth, spriteHeight, scalar, color):
    global frameNum
    global frameCount
    #show frame img
    sc.blit(getImage(sheet, frameNum, spriteWidth, spriteHeight, scalar, color), (0,0))
    if frameCount == 0:
        frameNum += 1
    if frameNum > 2:
        frameNum = 0

    frameCount += 1
    if frameCount == 12:
        frameCount = 0



while True:
    sc.fill(p.Color(BLUE))

    for event in p.event.get():
        if event.type == p.QUIT:
            exit()
    mapMain(sc)
    animator(pacmanSheetD, 48, 48, 1, BLACK)

    p.display.flip()
    clock.tick(60)