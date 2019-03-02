
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
eventd.create_event_type("fps")
spaceship1 = spaceship.Spaceship("/simple")
spaceship2 = spaceship.Spaceship("/simple", (100,100))

front_fps = pygame.font.SysFont('Comic Sans MS', 30)

background = background.Background()

clock = pygame.time.Clock()
pygame.display.flip()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==QUIT: pygame.display.quit()

        if event.type==VIDEORESIZE:
            screen_size = pygame.display.get_surface().get_size()
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            eventd.send_event("screen size", screen_size)
        if event.type==MOUSEBUTTONDOWN:
            if event.button==4:
                camera.zoom()

            elif event.button==5:
                camera.zoom(False)

    keys=pygame.key.get_pressed()

    if keys[K_s]:
        spaceship1.moveBy(0, 1)
    if keys[K_z]:
        spaceship1.moveBy(0, -1)
    if keys[K_d]:
        spaceship1.moveBy(1, 0)
    if keys[K_q]:
        spaceship1.moveBy(-1, 0)
    if keys[K_c]:
        if camera.mode == None:
            camera.follow(spaceship1)
        else:
            camera.mode = None

    eventd.send_event("fps",  round(clock.get_fps()))
    camera.update()
    background.animation(screen)
    spaceship1.animation(screen)
    spaceship2.animation(screen)

    render_fps = front_fps.render("FPS:" + str(round(clock.get_fps())), False, (255, 255, 255))
    screen.blit(render_fps,(0,0))

    pygame.display.update()

    #spaceship.moveBy(1, 0)
