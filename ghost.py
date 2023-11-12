import pygame as p
import random as r
from random import choice
from mapGenerator import mapMain, getDoneBool, getGridCells, getPelletStack

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
    def __init__(self, posX, posY, spriteSheet, speed):
        self.posX = posX
        self.posY = posY
        self.spriteSheet = spriteSheet
        self.speed = speed
        self.dirX = 0
        self.dirY = 0

    def move(self, gridCells):
        # Attempt to move in the current direction
        newPosX = self.posX + self.speed * self.dirX
        newPosY = self.posY + self.speed * self.dirY

        # Check collision with walls
        for cell in gridCells:
            cellX = cell.x * 48
            cellY = cell.y * 48
            if cell.walls['left'] and newPosX < cellX + 48 and self.posY + 48 > cellY and newPosY < cellY + 48:
                self.changeDirection()
            if cell.walls['right'] and newPosX + 48 > cellX and self.posY + 48 > cellY and newPosY < cellY + 48:
                self.changeDirection()
            if cell.walls['top'] and newPosY < cellY + 48 and self.posX + 48 > cellX and newPosX < cellX + 48:
                self.changeDirection()
            if cell.walls['bottom'] and newPosY + 48 > cellY and self.posX + 48 > cellX and newPosX < cellX + 48:
                self.changeDirection()

        # Update ghost position after collision check
        self.posX += self.speed * self.dirX
        self.posY += self.speed * self.dirY

    def changeDirection(self):
        # Change direction randomly
        self.dirX = r.choice([-1, 0, 1])
        self.dirY = r.choice([-1, 0, 1])

    def getImage(self, sheet, frame, width, height, scale, color):
        image = p.Surface((width, height))
        image.blit(sheet, (0,0), ((frame * width), 0, width, height))
        image = p.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image.convert_alpha()

    def draw(self, screen):
        screen.blit(self.getImage(self.spriteSheet, 0, 48, 48, 1, (0, 0, 0)), (self.posX, self.posY))
