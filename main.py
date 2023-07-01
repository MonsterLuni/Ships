import pygame as p
import menu as m
import map
import ui as u

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
colors = [[(255,0,0,255),0, "Red"],[(0,255,0,255),0, "Green"],[(0,0,255,255),0, "Blue"],[(255,255,0,255),0, "Yellow"],[(255,0,255,255),0, "Pink"],[(255,255,255,255),0, "White"]]

def game(running):
    global rightclickactive, collide, number, map_generated, dt, colors, surface, screen
    while running:
        dt = clock.tick(20) / 1000
        for event in p.event.get():
            mouse = p.mouse.get_pressed(3)
            if event.type == p.QUIT:
                running = False
            keys = p.key.get_pressed()
            if event.type == p.KEYDOWN:
                if keys[p.K_ESCAPE]:
                    running = False
                if keys[p.K_DELETE]:
                    map.deleteAll()
                if keys[p.K_F11]:
                    screen = u.togglefullscreen(screen)
            if event.type == p.MOUSEBUTTONDOWN:
                if  mouse[2]:
                    print("RIGHT")
                    rightclickactive = True
                    mouse_pos = p.mouse.get_pos()
                    collide, number = m.rightClickMenu(screen, mouse_pos, 6, True)
            if event.type == p.KEYDOWN or any(mouse):
                screen.fill((0,0,0,255))
                if  mouse[0]:
                    if not collide:
                        print("LEFT")
                        rightclickactive = False
                        mouse_pos = p.mouse.get_pos()
                        tile_pos = map.clickedtile(mouse_pos)
                        print(tile_pos)
                        map.placeTile(tile_pos, number)
                    else:
                        rightclickactive, collide = m.rightClickMenuAction(number)
                if  mouse[1]:
                        print("MIDDLE")
                        rightclickactive = False
                        mouse_pos = p.mouse.get_pos()
                        tile_pos_del = map.clickedtile(mouse_pos)
                        print(tile_pos_del)
                        map.deleteTile(tile_pos_del)
                map.rendermap(screen)
                tiles = map.rendertiles(screen)
                u.renderfont(screen, tiles,colors)
                print("Screen Updated")
        if not map_generated:
            map_generated = map.gamefield(9)
            map.rendermap(screen)
            tiles = map.rendertiles(screen)
            u.renderfont(screen, tiles, colors)
        if rightclickactive:
            collide, number = m.rightClickMenu(screen, mouse_pos, 6, False)
        p.display.flip()

game(True)