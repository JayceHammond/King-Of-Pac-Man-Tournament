import pygame as p
from pygame import mixer
import math
import numpy
import random as r

class Collider:
    def __init__(self, posx, posy, width, height):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
    
    def checkCollision(self, objArray):
        #Calculate the distance between the collider and the center of the obj
        collided = False
        for obj in objArray:
            distance = math.sqrt((self.posx - obj.posx) ** 2 + (self.posy - obj.posy) ** 2)

            #Check if a collision has occurred
            if distance < (self.width / 2) + (obj.width / 2):
                collided = True
                return collided