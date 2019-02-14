import pygame
from pygame.locals import *
import spaceship
import sys
import eventd

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size, HWSURFACE|DOUBLEBUF|RESIZABLE)

eventd.create_event_type("screen size")
spaceship = spaceship.Spaceship("/simple")
front_fps = pygame.font.SysFont('Comic Sans MS', 30)
background = pygame.image.load(sys.path[0]+"/pictures/background.png")
screen.blit(pygame.transform.scale(background, size), (0,0))
clock = pygame.time.Clock()
pygame.display.flip()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==QUIT: pygame.display.quit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            size = event.dict['size']
            eventd.send_event("screen size")

    render_fps = front_fps.render("FPS:" + str(round(clock.get_fps())), False, (255, 255, 255))

    screen.blit(pygame.transform.scale(background,size), (0,0))
    screen.blit(render_fps,(0,0))
    counter = spaceship.animation(screen, round(clock.get_fps()))

    pygame.display.update()