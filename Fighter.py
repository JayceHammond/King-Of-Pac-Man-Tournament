import pygame as p
import sys
from healthbar import HealthBar


pacmanSpriteSheet = p.image.load("Pac-Man Assets/Pac-Man Sprites/PacFightSprites/pacMoveSet.png")
brolyTransformation = p.image.load("FightingGameAssets/broly transformation.png")
brolyIdle = p.image.load("FightingGameAssets/Broly Idle.png")


global flip, inputTimer
global i, j, done
done = False
i, j = 0, 0
#frameNum, frameCount,
inputTimer = 0
flip = False
press = False
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
    def __init__(self, x, y, width, height, color, health):
        self.rect = p.Rect(x, y, width, height)
        self.color = color
        self.isJumping = False
        self.jumpCount = 10
        self.state = "Idle"
        self.healthNum = health
        self.healthBar = HealthBar(0, 0, 200)
        self.name = "player"
        self.frameNum = 0
        self.frameCount = 0
        self.flip = False

    def sideInput(self, event, keys):
        global flip, inputTimer, press
        if keys[p.K_LEFT]:
            inputTimer = (p.time.get_ticks() / 1000)
            print(inputTimer)
            self.rect.x -= 5
            self.state = "LeftW"
            self.flip = True
        elif keys[p.K_RIGHT]:
            self.rect.x += 5
            self.state = "RightW"
            self.flip = False
        else:
            self.state = "idle"

        if event.type == p.KEYUP:
            if keys[p.K_LEFT]:
                self.state = "idle"
            if keys[p.K_RIGHT]:
                self.state = "idle"

        if self.rect.x <= 0:
            self.rect.x = 1
        if self.rect.x >= 1200:
            self.rect.x = 1199
        if self.rect.y >= 470:
            self.rect.y = 469

    def attackInput(self, event, keys):
        if keys[p.K_z]:
            self.state = "light"

    def jumpInput(self, keys):
        if not self.isJumping:
            if keys[p.K_UP]:
                self.isJumping = True
                #self.state = "jump"
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

    def getImage(self, sheet, frame, width, height, scale, color, row):
        image = p.Surface((width, height))
        image.blit(sheet, (0,0), ((frame * width), (row * height), width, height))
        image = p.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image.convert_alpha()


    def animator(self, sheet, spriteWidth, spriteHeight, scalar, color, pos, sc, frameStart, frameEnd, rate, row):
        #global frameNum
        #global frameCount
        #frameInc = 0
        #show frame img
        frame = self.getImage(sheet, self.frameNum, spriteWidth, spriteHeight, scalar, color, row)
        
        if self.flip == True and self.name == "player":
            flipFrame = p.transform.flip(frame, 1, 0)
            sc.blit(flipFrame, pos)
        if self.flip == False :
            sc.blit(frame, pos)
        self.frameCount += 1
        if self.frameCount == frameEnd:
            self.frameNum += 1
            #print("HELP")
        if self.frameNum > frameEnd:
            self.frameNum = frameStart

        if self.frameCount > rate:
            self.frameCount = frameStart
        #print(self.state)
        #print(frameCount)
        #print("FrameNum: " + str(frameNum))
        #print("FrameEnd: " + str(frameEnd))

    #def crouchInput(self, keys):
        #if keys[p.K_DOWN]:
         #   self.rect.y += 5

    def drawPac(self, screen):
        #global frameNum
        #p.draw.rect(screen, self.color, self.rect)
        if self.state == "RightW":
            #frameNum = 2
            self.animator(pacmanSpriteSheet, 27, 40, 3.7, BLACK, (self.rect.x, self.rect.y), screen, 2, 7, 9, 0)
        if self.state == "LeftW":
            #frameNum = 2
            self.animator(pacmanSpriteSheet, 27, 40, 3.7, BLACK, (self.rect.x, self.rect.y), screen, 2, 7, 9, 0)
        if self.state == "jump":
            self.animator(pacmanSpriteSheet, 27, 40, 3.7, BLACK, (self.rect.x, self.rect.y), screen, 0, 2, 9, 1)
        if self.state == "light":
            self.animator(pacmanSpriteSheet, 54, 40, 3.7, BLACK, (self.rect.x, self.rect.y), screen, 0, 1, 18, 5)
        if self.state == "idle":
            #frameNum = 0
            self.animator(pacmanSpriteSheet, 27, 40, 3.7, BLACK, (self.rect.x, self.rect.y), screen, 0, 1, 24, 0)

    def drawGhost(self, screen):
        global i, j, done 
        #p.draw.rect(screen, self.color, self.rect)
        
        if not done:
            if self.frameNum != 4:
                self.animator(p.transform.flip(brolyTransformation, 1, 0), 143, 204, 1, BLACK, (self.rect.x, self.rect.y), screen, 0, 4, 9, i)
            if self.frameNum == 4:
                self.frameNum = 0
                i += 1
            if self.frameNum == 1 and i == 3:
                done = True
        else:
            self.animator(p.transform.flip(brolyIdle, 1, 0), 143, 204, 1, BLACK, (self.rect.x, self.rect.y), screen, 0, 4, 9, j)
            if j == 1:
                j = 0
            if self.frameNum == 4:
                j += 1