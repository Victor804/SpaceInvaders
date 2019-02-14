import pygame
import spaceship
import sys
import eventd

pygame.init()

screen = pygame.display.set_mode((640, 480))
eventd.create_event_type("screen size")

spaceship = spaceship.Spaceship("/simple")

front_fps = pygame.font.SysFont('Comic Sans MS', 30)
background = pygame.image.load(sys.path[0]+"/pictures/background.png").convert()
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    render_fps = front_fps.render("FPS:" + str(round(clock.get_fps())), False, (255, 255, 255))

    screen.blit(background, (0,0))
    screen.blit(render_fps,(0,0))
    counter = spaceship.animation(screen, round(clock.get_fps()))

    pygame.display.update()
