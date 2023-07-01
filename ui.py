import pygame as p

p.font.init()
font = p.font.SysFont(None, 25)
# FARBNAME, AMOUNT

def renderfont(screen, tiles, colors):
    id = 0
    for color in colors:
        color[1] = 0
        for tile in tiles:
            if tile[1] == color[0]:
                color[1] += 1
        score = font.render(color[2] + ": " + str(color[1]),True,color[0])
        if 25 + (id * 100) > 500:
            screen.blit(score, (25 + (id * 100) % 500, 468))
        else:
            screen.blit(score, (25 + (id * 100),18))
        id += 1

def togglefullscreen():
    print("FULLSCREEN TOGGLED")