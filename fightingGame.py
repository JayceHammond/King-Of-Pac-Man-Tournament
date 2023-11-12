import pygame as p
import sys
from player1 import Player


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


# Initialize Pygame
p.init()

# Constants
WIDTH, HEIGHT = 1200, 600
FPS = 60
WHITE = (255, 255, 255)

bgImgArr = [
    "FightingGameAssets/BG_Assets/bg1.png",
    "FightingGameAssets/BG_Assets/bg2.png",
    "FightingGameAssets/BG_Assets/bg3.png",
    "FightingGameAssets/BG_Assets/bg4.png",
    "FightingGameAssets/BG_Assets/bg5.png",
    "FightingGameAssets/BG_Assets/bg6.png",
    "FightingGameAssets/BG_Assets/bg7.png",
    "FightingGameAssets/BG_Assets/bg8.png"
]


# Create the screen
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Fighting Game")

# Load images
bg_frames = [p.image.load(img_path).convert() for img_path in bgImgArr]
current_frame = 0

# Create players using the Player class
player1 = Player(50, 550, 50, 50, RED)
player2 = Player(700, 550, 50, 50, BLUE)

# Set up clock
clock = p.time.Clock()

def draw_background():
    global lastframe
    if current_frame % 7 == 0:
        screen.blit(bg_frames[current_frame % len(bg_frames)], (0, 0))
        lastframe = bg_frames[current_frame % len(bg_frames)]
    else:
        screen.blit(lastframe, (0,0))

# Game loop
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()

    # Handle player input using the Player class methods
    keys = p.key.get_pressed()
    player1.sideInput(keys)
    player1.jumpInput(keys)
    #player2.handle_input(keys)

    # Update game logic here (e.g., collision detection, health, etc.)

    draw_background()

    # Draw everything using the Player class methods
    player1.draw(screen)
    player2.draw(screen)

    # Update the display
    p.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
    current_frame += 1