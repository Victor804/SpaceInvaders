import pygame
import eventd

class Camera:
    def __init__(self, pos=(0,0)):
        self.pos = pos
        self.zoom = 1
        self.speed = 10

        eventd.create_event_type("camera move")

    def moveTo(self, horizontal, vertical):
        """
        Teleporte la camera sur une position
        Entree: horizontal(int), vertical(int)
        """
        diff_pos = (horizontal-self.pos[0], vertical-self.pos[1])
        self.pos = (horizontal, vertical)
        eventd.send_event("camera move", diff_pos)


    def moveBy(self, horizontal, vertical):
        """
        Bouge la camera dans une certaine direction
        Entree: horizontal(1, 0, -1), vertical(1, 0, -1)
        """
        self.pos = (self.pos[0]+horizontal*self.speed, self.pos[-1]+vertical*self.speed)
        eventd.send_event("camera move", (horizontal*self.speed, self.speed*vertical))

    def zoom(self):
        pass
