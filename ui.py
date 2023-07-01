import pygame as p

p.font.init()
font = p.font.SysFont(None, 25)

def renderfont(screen, tiles):
    global font
    score = font.render("Blocks: " + str(len(tiles)),True,"red")
    screen.blit(score, (25,18))