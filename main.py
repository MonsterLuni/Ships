import pygame as p
import menu as m
import map

p.init()
p.display.set_caption('Ships')
screen = p.display.set_mode((500,500))
clock = p.time.Clock()
dt = 0
surface = p.display.get_surface()
rightclickactive = False
collide = False
number = 0
map_generated = False

def game(running):
    global rightclickactive, collide, number, map_generated, dt
    while running:
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0,255))
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            keys = p.key.get_pressed()
            if event.type == p.KEYDOWN:
                if keys[p.K_ESCAPE]:
                    running = False
            mouse = p.mouse.get_pressed(5)
            if event.type == p.MOUSEBUTTONDOWN:
                if  mouse[0]:
                    if not collide:
                        print("LEFT")
                        rightclickactive = False
                        mouse_pos = p.mouse.get_pos()
                        tile_pos = map.clickedtile(mouse_pos)
                        print(tile_pos)
                        map.placeTile(tile_pos)
                    else:
                        rightclickactive, collide = m.rightClickMenuAction(number)
                if  mouse[1]:
                    print("MIDDLE")
                    rightclickactive = False
                if  mouse[2]:
                    print("RIGHT")
                    rightclickactive = True
                    mouse_pos = p.mouse.get_pos()
                    collide, number = m.rightClickMenu(screen, mouse_pos, 5, True)
        if not map_generated:
            map_generated = map.gamefield(9)
        map.rendermap(screen)
        map.rendertiles(screen)
        if rightclickactive:
            collide, number = m.rightClickMenu(screen, mouse_pos, 5, False)
        p.display.flip()

game(True)