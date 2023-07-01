import pygame as p
import numpy as np

id = 0
linesx = []
linesy = []
tiles = []
idplace = 0
colors = [[(255,0,0,255),0, "Red"],[(0,255,0,255),0, "Green"],[(0,0,255,255),0, "Blue"],[(255,255,0,255),0, "Yellow"],[(255,0,255,255),0, "Pink"],[(255,255,255,255),0, "White"]]

def gamefield(amount, screen):
    global id, lines, linesx, linesy
    id = 0
    linesx = []
    linesy = []
    lines = amount
    while id < amount:
        start = p.Vector2((screen.get_width() - 400) / 2,50 + (id * 50))
        end = p.Vector2((screen.get_width() - (screen.get_width() - 400) / 2),50 + (id * 50))
        linesx.append([
            id,
            start,
            end
        ])
        start = p.Vector2(((screen.get_width() - 400) / 2) + (id * 50),50)
        end = p.Vector2(((screen.get_width() - 400) / 2) + (id * 50),450)
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

def clickedtile(mouse_pos, screen):
    global lines, lst
    id = 0
    reseter = 1
    mouse_pos_better = tuple([(mouse_pos[0] - ((screen.get_width() - 400) / 2)),mouse_pos[1]])
    print(mouse_pos_better)
    pos = p.Vector2((mouse_pos_better[0])/50,(mouse_pos_better[1]-50)/50)
    #print(str(pos.x) + " : " + str(pos.y))
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
    return p.Vector2(x,y)

def placeTile(tile_pos, number):
    global tiles, idplace, colors
    rect = p.Rect((tile_pos[0] * 50) +25, (tile_pos[1] * 50) +25,50,50)
    match number:
        case 1:
            color = colors[0][0]
        case 2:
            color = colors[1][0]
        case 3:
            color = colors[2][0]
        case 4:
            color = colors[3][0]
        case 5:
            color = colors[4][0]
        case 6:
            color = colors[5][0]
    for tile in tiles:
        if rect == tile[0]:
            return
    if number < 1 or tile_pos.x > 8 or tile_pos.y > 8:
        return
    tiles.append([rect, color, idplace])
    idplace += 1
    return colors

def deleteTile(tile_pos):
    global tiles
    idtile = 0
    position = p.Rect((tile_pos[0] * 50) +25, (tile_pos[1] * 50) +25,50,50)
    for tile in tiles:
        if tile[0] == position:
            del tiles[idtile]
        idtile += 1

def deleteAll():
    global tiles
    tiles.clear()

def rendertiles(screen):
    global tiles
    for tile in tiles:
        rect = p.Rect(((screen.get_width() - 400) / 2) + tile[0][0] - 50,tile[0][1],50,50)
        p.draw.rect(screen,tile[1],rect)
    return tiles