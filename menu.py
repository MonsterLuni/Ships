import pygame as p

collide = []
number = 0
id = 0
points = []
colors = [[(255,0,0,255),0, "Red"],[(0,255,0,255),0, "Green"],[(0,0,255,255),0, "Blue"],[(255,255,0,255),0, "Yellow"],[(255,0,255,255),0, "Pink"],[(255,255,255,255),0, "White"]]

def rightClickMenu(screen, mouse_pos, amount, new):
    global collide, number, id, points
    if new:
        points = []
        id = 1
    while id <= amount:
        menurect = p.Rect(mouse_pos[0], mouse_pos[1] + (id * 25), 50, 25)
        match id:
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
        points.append([
            id - 1,
            menurect,
            color
        ])
        id += 1
    for point in points:
        colliderect = point[1].collidepoint(p.mouse.get_pos())
        colorrect = (80, 80, 80, 20) if colliderect else point[2]
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
    return False, False
    