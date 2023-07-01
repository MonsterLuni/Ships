import pygame as p

p.font.init()
font = p.font.SysFont(None, 50)

def renderfont():
    global font
    score = font.render("Hellou",True,"red")