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


res = width, height = 1200, 600
tile = 60
cols, rows = width // tile, height // tile
pellet = p.image.load("Pac-Man Assets\Tiles\Pellet.png")
pelletStack = []
global updatePellets
updatePellets = True
global doneBool
doneBool = False

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True, 'pellet': True}
        self.visited = False
        self.open = False

    def draw(self, sc):
        global updatePellets
        x, y = self.x * tile, self.y * tile
        
        if self.visited:
            p.draw.rect(sc, BLACK, (x,y, tile, tile))
            self.open = True
        if self.walls['top']:
            p.draw.line(sc, BLUE, (x,y), (x + tile, y), 5)
        if self.walls['right']:
            p.draw.line(sc, BLUE, (x + tile, y), (x + tile, y + tile), 5)
        if self.walls['bottom']:
            p.draw.line(sc, BLUE, (x + tile, y + tile), (x, y + tile), 5)
        if self.walls['left']:
            p.draw.line(sc, BLUE, (x, y + tile), (x, y), 5)
        if self.walls['pellet']:
            if updatePellets:
                pelletStack.append((x + (tile // 2), y + (tile // 2)))
                if len(pelletStack) == 200:
                    updatePellets = False
            p.draw.circle(sc, YELLOW, (x + (tile // 2), (y + (tile // 2))), 5)

        

    def drawCurrentCell(self,sc):
        x = self.x * tile
        y = self.y * tile
        p.draw.rect(sc, FROYALBLUE, (x + 2, y + 2, tile - 2, tile - 2))

    def checkCell(self, x, y):
        findIndex = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return gridCells[findIndex(x,y)]
    
    def checkNeighbors(self):
        neighbors = []
        top = self.checkCell(self.x, self.y - 1)
        right = self.checkCell(self.x + 1, self.y)
        left = self.checkCell(self.x - 1, self.y)
        bottom = self.checkCell(self.x, self.y + 1)

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if left and not left.visited:
            neighbors.append(left)
        if bottom and not bottom.visited:
            neighbors.append(bottom)

        return choice(neighbors) if neighbors else False
    



gridCells = [Cell(col, row) for row in range(rows) for col in range(cols)]
currCell = gridCells[0]
stack = []
wallStack = []
        

tileSheet = "Pac-Man Assets\Tiles\MazeParts.png"

def removeWalls(curr, next):
    dx = curr.x - next.x
    dy = curr.y - next.y
    if dx == 1:
        curr.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        curr.walls['right'] = False
        next.walls['left'] = False

    if dy == 1:
        curr.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        curr.walls['bottom'] = False
        next.walls['top'] = False


def backtrack():
    if stack:
        cell_to_backtrack = stack[-1]
        unvisited_neighbors = cell_to_backtrack.checkNeighbors()



        if isinstance(unvisited_neighbors, Cell):
                # If there's a single unvisited neighbor, choose it
                next_cell = unvisited_neighbors
                removeWalls(cell_to_backtrack, next_cell)
                next_cell.visited = True
                stack.append(next_cell)
                return cell_to_backtrack if stack else None
        else:
            stack.pop()
            return cell_to_backtrack if stack else None


def getDoneBool():
    return doneBool

def getPelletStack():
    return pelletStack
        


runnable = True
def mapMain(screen, pacMan):
    global currCell
    global nextCell
    global doneBool
    doneBool = False
    [cell.draw(screen) for cell in gridCells]
    if currCell != None:
        currCell.visited = True
        currCell.drawCurrentCell(screen)

        nextCell = currCell.checkNeighbors()
    if nextCell:
        nextCell.visited = True
        stack.append(currCell)
        removeWalls(currCell, nextCell)
        currCell = nextCell
    elif stack:
        currCell = backtrack()
    else:
        doneBool = True

    if doneBool == True:
        collision = False
        global updatePellets
        if len(wallStack) <= 200:
            for cell in gridCells:      
                if cell.walls["left"] == True:
                    leftWall = p.draw.rect(screen, GREEN, (cell.x * tile, cell.y * tile, 5, 60))
                    wallStack.append(leftWall)
                if cell.walls["top"] == True:
                    topWall = p.draw.rect(screen, GREEN, (cell.x * tile, cell.y * tile, 60, 5))
                    wallStack.append(topWall)
            doneBool = False
        return wallStack

