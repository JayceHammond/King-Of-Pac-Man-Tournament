import pygame as p
import sys


pacmanSpriteSheet = p.image.load("Pac-Man Assets/Pac-Man Sprites/PacFightSprites/pacMoveSet.png")


global frameNum
global frameCount
frameNum = 0
frameCount = 0

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

#states
moveLeft = False
moveRight = False
jump = False
isIdle = False
isBlocking = False


class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = p.Rect(x, y, width, height)
        self.color = color
        self.isJumping = False
        self.jumpCount = 10

    def sideInput(self, event, keys):
        global moveLeft, moveRight, isIdle
        if keys[p.K_LEFT]:
            self.rect.x -= 5
            isIdle = False
            moveRight = False
            moveLeft = True
        elif keys[p.K_RIGHT]:
            self.rect.x += 5
            isIdle = False
            moveRight = True
        else:
            isIdle = True

        if event.type == p.KEYUP:
            if keys[p.K_LEFT]:
                moveLeft = False
                isIdle = True
            if keys[p.K_RIGHT]:
                moveRight = False
                isIdle = True

        if self.rect.x <= 0:
            self.rect.x = 1
        if self.rect.x >= 1200:
            self.rect.x = 1199
        if self.rect.y >= 470:
            self.rect.y = 469

    def jumpInput(self, keys):
        if not self.isJumping:
            if keys[p.K_UP]:
                self.isJumping = True
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.rect.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJumping = False
                self.jumpCount = 10

    def getImage(self, sheet, frame, width, height, scale, color):
        image = p.Surface((width, height))
        image.blit(sheet, (0,0), ((frame * width), 0, width, height))
        image = p.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image.convert_alpha()


    def animator(self, sheet, spriteWidth, spriteHeight, scalar, color, pos, sc, frameStart, frameEnd, rate):
        global frameNum
        global frameCount
        #show frame img
        sc.blit(self.getImage(sheet, frameNum, spriteWidth, spriteHeight, scalar, color), pos)
        if frameCount == frameStart:
            frameNum += 1
        if frameNum > frameEnd:
            frameNum = frameStart

        frameCount += 1
        if frameCount == rate:
            frameCount = frameStart

    #def crouchInput(self, keys):
        #if keys[p.K_DOWN]:
         #   self.rect.y += 5

    def drawPac(self, screen):
        global frameNum
        #p.draw.rect(screen, self.color, self.rect)
        if moveRight:
            self.animator(pacmanSpriteSheet, 27, 40, 3.7, BLACK, (self.rect.x, self.rect.y), screen, 2, 7, 18)
        if isIdle:
            self.animator(pacmanSpriteSheet, 27, 40, 3.7, BLACK, (self.rect.x, self.rect.y), screen, 0, 1, 24)

    def drawGhost(self, screen):
        p.draw.rect(screen, self.color, self.rect)