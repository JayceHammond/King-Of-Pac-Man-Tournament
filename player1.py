import pygame as p
import sys

class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = p.Rect(x, y, width, height)
        self.color = color
        self.isJumping = False
        self.jumpCount = 10

    def sideInput(self, keys):
        if keys[p.K_LEFT]:
            self.rect.x -= 5
        if keys[p.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x <= 0:
            self.rect.x = 1
        if self.rect.x >= 1200:
            self.rect.x = 1199
        if self.rect.y >= 550:
            self.rect.y = 549

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

    #def crouchInput(self, keys):
        #if keys[p.K_DOWN]:
         #   self.rect.y += 5

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)