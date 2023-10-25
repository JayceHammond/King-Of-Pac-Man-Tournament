import pygame as p
import numpy

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)


tileSheet = "Pac-Man Assets\Tiles\MazeParts.png"

def get_pixels_at(x, y, width, height, map):
    rect = p.Rect(x, y, width, height)
    pixels = p.Surface((width, height))
    pixels.blit(map, (0,0), rect)
    return pixels

p.init()
clock = p.time.Clock()
screen_width = 720
screen_height = 720
screen = p.display.set_mode([screen_width, screen_height])
get_pixels_at(0,0, 48, 48, tileSheet)
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        