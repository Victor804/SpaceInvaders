import pygame
from lxml import etree
import os, sys
import eventd

class Background:
    def __init__(self, directory="/default", pos=(0,0)):
        self.directory = "{}/pictures/background{}".format(sys.path[0], directory)

        self.name = etree.parse(self.directory+"/model.xml").xpath("/background/name")[0].text
        self.pos = pos

        self.animation_time = eval(etree.parse(self.directory+"/model.xml").xpath("/background/animationTime")[0].text)
        self.animation_counter = 0

        self.list_pictures = self.load_pictures()
        self._events_registers()


    def _events_registers(self):
        eventd.register("screen size", self.load_pictures)


    def load_pictures(self):
        """
        Charge les images

        Sortie: Liste des surfaces des images dans une liste
        """
        list_pictures = list()
        for file in os.listdir("{}/animation".format(self.directory)):
            picture = pygame.image.load("{}/animation/{}".format(self.directory, file)).convert()
            size = (int(pygame.display.get_surface().get_size()[0]), int(pygame.display.get_surface().get_size()[1]))
            picture = pygame.transform.scale(picture, size)
            list_pictures.append(picture)
        self.list_pictures = list_pictures
        return list_pictures


    def animation(self, screen, fps):
        """
        Affiche le fond d'ecran en fonction de l'animation

        Entree: Ecran, fps
        """
        self.animation_counter+=1
        fps = fps if fps != 0 else 0.1
        if self.animation_counter/fps >= self.animation_time:
            screen.blit(self.list_pictures[-1], self.pos)
            self.animation_counter = 0

        else:
            for i in range(1, len(self.list_pictures)+1):
                t = self.animation_time/len(self.list_pictures)
                if t*(i-1) <= self.animation_counter/fps and self.animation_counter/fps < t*i:
                    screen.blit(self.list_pictures[i-1], self.pos)
