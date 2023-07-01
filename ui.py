import pygame as p
import map as m

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
        if 25 + (id * 100) > screen.get_width():
            screen.blit(score, (25 + (id * 100) % 500, 468))
        else:
            screen.blit(score, (25 + (id * 100),18))
        id += 1

def togglefullscreen(screen, amount):
    if p.display.is_fullscreen():
        p.display.toggle_fullscreen()
        screen = p.display.set_mode((500,500))
    else:
        screens = p.display.get_desktop_sizes()
        screen = p.display.set_mode(screens[0])
        p.display.toggle_fullscreen()
    m.gamefield(amount, screen)
    return screen