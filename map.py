import pygame as p
import numpy as np

id = 0
linesx = []
linesy = []
tiles = []

def gamefield(amount):
    global id, lines
    lines = amount
    while id <= amount:
        start = p.Vector2(50,50 + (id * 50))
        end = p.Vector2(450,50 + (id * 50))
        linesx.append([
            id,
            start,
            end
        ])
        start = p.Vector2(50 + (id * 50),50)
        end = p.Vector2(50 + (id * 50),450)
        linesy.append([
            id,
            start,
            end
        ])
        id += 1
    return True

def rendermap(screen):
    global linesx, linesy
    for linex in linesx:
        p.draw.line(screen,"red",linex[1],linex[2],2)
    for liney in linesy:
        p.draw.line(screen,"blue",liney[1],liney[2],2)

import numpy as np
def closest(lst, K):
     
     lst = np.asarray(lst)
     idx = (np.abs(lst - K)).argmin()
     return lst[idx]

def clickedtile(mouse_pos):
    global lines, lst
    id = 0
    reseter = 1
    pos = p.Vector2((mouse_pos[0]-50)/50,(mouse_pos[1]-50)/50)
    lst = []
    while id <= lines:
        lst.append([id])
        if reseter == 1:
            lst.pop(len(lst)-1)
            reseter = 0
        else:
            reseter += 1
        id += 0.5
    x = closest(lst,pos.x)
    y = closest(lst,pos.y)
    #print("X: " + str(x) + " Y: " + str(y))
    return p.Vector2(x,y)

def placeTile(tile_pos):
    global tiles
    rect = p.Rect((tile_pos[0] * 50) +25, (tile_pos[1] * 50) +25,50,50)
    tiles.append([rect])
    print("Tile Placed")

def rendertiles(screen):
    global tiles
    for tile in tiles:
        p.draw.rect(screen, "green", tile[0])

