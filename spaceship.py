import pygame
from lxml import etree
import os, sys

class Spaceship:
	def __init__(self, directory, pos=(0, 0)):
		self.name = etree.parse(sys.path[0]+"/spaceships"+directory+"/model.xml").xpath("/spaceship/name")[0].text
		self.pos = (0, 0)
		self.life = eval(etree.parse(sys.path[0]+"/spaceships"+directory+"/model.xml").xpath("/spaceship/life")[0].text)
		self.speed = eval(etree.parse(sys.path[0]+"/spaceships"+directory+"/model.xml").xpath("/spaceship/speed")[0].text)
		self.animation_time = eval(etree.parse(sys.path[0]+"/spaceships"+directory+"/model.xml").xpath("/spaceship/animationTime")[0].text)
		self.list_pictures = self._load_pictures(directory)


	def _load_pictures(self, directory):
		"""
		Entree:	Dossier du vaisseau
		Sortie: Liste des surfaces des images dans une liste
		"""
		list_pictures = list()
		for file in os.listdir("./spaceships{}/animation".format(directory)):
			list_pictures.append(pygame.image.load("./spaceships{}/animation/{}".format(directory, file)).convert_alpha())
		return list_pictures


	def move(self, x, y):
		"""
		Bouge le joueur

		Entree: x, y bool
		Sortie: True si peux bouger sinon False
		"""
		display = pygame.display.get_surface().get_rect()

		self.pos = (self.pos[0]+speed*x, self.pos[1]+speed*y)
		if not display.colliderect(self.list_pictures[0].get_rect()):#Verification que le joueur reste sur l'ecran
			self.pos = (self.pos[0]-speed*x, self.pos[1]-speed*y)
			return False

		else:
			return True


	def animation(self, screen, counter, fps):
		"""
		Affiche le vaisseau sur l'ecran en fonction de l'animation

		Entree: Ecran, compteur de boucle, fps, duree de l'animation
		Sortie: Compteur de boucle
		"""
		fps = fps if fps != 0 else 0.1
		if counter/fps >= self.animation_time:
			screen.blit(self.list_pictures[-1], self.pos)
			counter = 0

		else:
			for i in range(1, len(self.list_pictures)+1):
				t = self.animation_time/len(self.list_pictures)
				if t*(i-1) <= counter/fps and counter/fps < t*i:
					screen.blit(self.list_pictures[i-1], self.pos)

		return counter


if __name__ == "__main__":
	spaceship = Spaceship("/simple")
	print(spaceship.name)
	print(spaceship.life)
	print(spaceship.speed)
	print(spaceship.list_pictures)
