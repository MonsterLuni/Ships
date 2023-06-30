import pygame as p
import numpy as np

id = 0
linesx = []
linesy = []
tiles = []
idplace = 0

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
    while id < lines - 1:
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

def placeTile(tile_pos, number):
    global tiles, idplace
    rect = p.Rect((tile_pos[0] * 50) +25, (tile_pos[1] * 50) +25,50,50)
    color = (255,255,255,255)
    match number:
        case 1:
            color = (255,0,0,255)
        case 2:
            color = (0,255,0,255)
        case 3:
            color = (0,0,255,255)
        case 4:
            color = (255,255,0,255)
        case 5:
            color = (255,0,255,255)
    for tile in tiles:
        if rect == tile[0]:
            return
    if number < 1:
        return
    tiles.append([rect, color, idplace])
    idplace += 1
    print("Tile Placed")

def deleteTile(tile_pos):
    global tiles
    idtile = 0
    position = p.Rect((tile_pos[0] * 50) +25, (tile_pos[1] * 50) +25,50,50)
    for tile in tiles:
        if tile[0] == position:
            del tiles[idtile]
            print("Tile erfolgreich gelöscht")
        idtile += 1

def rendertiles(screen):
    global tiles
    for tile in tiles:
        p.draw.rect(screen, tile[1], tile[0])