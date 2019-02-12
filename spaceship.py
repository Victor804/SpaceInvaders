import pygame
from lxml import etree
import sys, os

class Spaceship:
	def __init__(self, directory):
		self.name = etree.parse(sys.path[0]+"/spaceships"+directory+"/model.xml").xpath("/spaceship/name")[0].text
		self.life = eval(etree.parse(sys.path[0]+"/spaceships"+directory+"/model.xml").xpath("/spaceship/life")[0].text)
		self.speed = eval(etree.parse(sys.path[0]+"/spaceships"+directory+"/model.xml").xpath("/spaceship/speed")[0].text)
		self.list_pictures = self._load_pictures(directory)


	def _load_pictures(self, directory):
		"""
		Entree:	Dossier du vaisseau
		Sortie: Liste des surfaces des images dans une liste
		"""
		list_pictures = list()
		for file in os.listdir(sys.path[0]+"/spaceships{}/animation".format(directory)):
			list_pictures.append(pygame.image.load(sys.path[0]+"/spaceships{}/animation/{}".format(directory, file)).convert_alpha())
		return list_pictures


	def animation(self, screen, counter, fps):
		"""
		Affiche le vaisseau sur l'ecran en fonction de l'animation

		Entree: Ecran, compteur de boucle, fps
		Sortie: Compteur de boucle
		"""
		fps = fps if fps != 0 else 0.1
		if counter/fps >= 1:
			screen.blit(self.list_pictures[-1], (0,0))
			counter = 0

		else:
			for i in range(1, len(self.list_pictures)+1):
				t = 1/len(self.list_pictures)
				if t*(i-1) <= counter/fps and counter/fps < t*i:
					screen.blit(self.list_pictures[i-1], (0,0))

		return counter

if __name__ == "__main__":
	spaceship = Spaceship("/simple")
	print(spaceship.name)
	print(spaceship.life)
	print(spaceship.speed)
	print(spaceship.list_pictures)
