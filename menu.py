import pygame as p

collide = []
number = 0
id = 0
points = []

def rightClickMenu(screen, mouse_pos, amount, new):
    global collide, number, id, points
    if new:
        points = []
        id = 0
    while id < amount:
        menurect = p.Rect(mouse_pos[0], mouse_pos[1] + (id * 25), 50, 25)
        points.append([
            id,
            menurect
        ])
        id += 1
    for point in points:
        colliderect = point[1].collidepoint(p.mouse.get_pos())
        colorrect = (255, 0, 0) if colliderect else (255,215,0)
        p.draw.rect(screen, colorrect, point[1])
        if colliderect:
            number = point[0] + 1
            collide.append(True)
        else:
            collide.append(False)
    if any(collide):
        hover = True
    else:
        hover = False
    collide = []
    return hover, number

def rightClickMenuAction(number):
    print("AUF NUMMER: " + str(number) + " Gedrückt")
    return False
    