import pygame
from pygame.locals import *
import spaceship, background
import sys
import eventd

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size, HWSURFACE|DOUBLEBUF|RESIZABLE)

eventd.create_event_type("screen size")
spaceship = spaceship.Spaceship("/simple")
front_fps = pygame.font.SysFont('Comic Sans MS', 30)

background = background.Background()

clock = pygame.time.Clock()
pygame.display.flip()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==QUIT: pygame.display.quit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            eventd.send_event("screen size")


    background.animation(screen, round(clock.get_fps()))
    spaceship.animation(screen, round(clock.get_fps()))

    render_fps = front_fps.render("FPS:" + str(round(clock.get_fps())), False, (255, 255, 255))
    screen.blit(render_fps,(0,0))

    pygame.display.update()
