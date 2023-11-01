import pygame as p
import numpy
from random import choice
from collider import Collider

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



class Ghost:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def getImage(sheet, frame, width, height, scale, color):
        image = p.Surface((width, height))
        image.blit(sheet, (0,0), ((frame * width), 0, width, height))
        image = p.transform.scale(image, (width *scale, height * scale))
        image.set_colorkey(color)

        return image.convert_alpha()
    
    def animator(self, frameNum, sheet, spriteWidth, spriteHeight, scalar, color , pos, frameCount, screen):
        
        screen.blit(self.getImage(sheet, frameNum, spriteWidth, spriteHeight, scalar), pos)
        if frameCount == 0:
            frameNum += 1
        if frameNum > 16:
            frameNum = 0

        frameCount += 1
        if frameCount == 12:
            frameCount = 0