
import pygame
from pygame.locals import *
import spaceship, background, camera
import sys
import eventd

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size, HWSURFACE|DOUBLEBUF|RESIZABLE)

camera = camera.Camera()

eventd.create_event_type("screen size")
spaceship1 = spaceship.Spaceship("/simple")
spaceship2 = spaceship.Spaceship("/simple", (100,100))

front_fps = pygame.font.SysFont('Comic Sans MS', 30)

background = background.Background()

clock = pygame.time.Clock()
pygame.display.flip()

pygame.key.set_repeat(30,10)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==QUIT: pygame.display.quit()

        if event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            eventd.send_event("screen size")

        if event.type==KEYDOWN:
            if event.key==K_s:
                spaceship1.moveBy(0, 1)
            if event.key==K_z:
                spaceship1.moveBy(0, -1)
            if event.key==K_d:
                spaceship1.moveBy(1, 0)
            if event.key==K_q:
                spaceship1.moveBy(-1, 0)
            if event.key==K_c:
                if camera.mode == None:
                    camera.follow(spaceship1)
                else:
                    camera.mode = None
        if event.type==MOUSEBUTTONDOWN:
            if event.button==4:
                camera.zoom()

            elif event.button==5:
                camera.zoom(False)

    camera.update()
    background.animation(screen, round(clock.get_fps()))
    spaceship1.animation(screen, round(clock.get_fps()))
    spaceship2.animation(screen, round(clock.get_fps()))

    render_fps = front_fps.render("FPS:" + str(round(clock.get_fps())), False, (255, 255, 255))
    screen.blit(render_fps,(0,0))

    pygame.display.update()

    #spaceship.moveBy(1, 0)
