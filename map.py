import pygame as p

id = 0
linesx = []
linesy = []

def gamefield(screen, amount):
    global id
    while id < amount:
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