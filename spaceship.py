import pygame
from lxml import etree
import os, sys
import eventd

class Spaceship:
	def __init__(self, directory, pos=(0,0)):
		self.directory = "{}/spaceships{}".format(sys.path[0], directory)
		self.name = etree.parse(self.directory+"/model.xml").xpath("/spaceship/name")[0].text

		self.pos = pos
		self.pos_pictures = pos

		self.life = eval(etree.parse(self.directory+"/model.xml").xpath("/spaceship/life")[0].text)
		self.speed = eval(etree.parse(self.directory+"/model.xml").xpath("/spaceship/speed")[0].text)

		self.animation_time = eval(etree.parse(self.directory+"/model.xml").xpath("/spaceship/animationTime")[0].text)
		self.animation_counter = 0
		self.proportion_on_screen = 1/eval(etree.parse(self.directory+"/model.xml").xpath("/spaceship/proportionOnScreen")[0].text)
		self.list_original_pictures = self.load_pictures()
		self.list_pictures = self.resize_pictures()

		self.fps = 0

		self.bullet = Bullet(self)

		self._events_registers()


	def _events_registers(self):
		eventd.register("screen size", self._screen_resize)
		eventd.register("camera move", self._camera_move)
		eventd.register("zoom", self._camera_zoom)
		eventd.register("fps", self._save_fps)

	def _save_fps(self, fps):
		self.fps = fps


	def load_pictures(self):
		"""
		Charge les images

		Sortie: Liste des surfaces des images dans une liste
		"""
		list_pictures = list()
		for file in os.listdir(self.directory+"/animation"):
			picture = pygame.image.load("{}/animation/{}".format(self.directory, file)).convert_alpha()
			list_pictures.append(picture)
		self.list_original_pictures = list_pictures
		return list_pictures


	def resize_pictures(self):
		list_pictures = list()
		for picture in self.list_original_pictures:
			size = (int(pygame.display.get_surface().get_size()[0]*self.proportion_on_screen), int(pygame.display.get_surface().get_size()[1]*self.proportion_on_screen))
			picture = pygame.transform.scale(picture, size)
			list_pictures.append(picture)
		self.list_pictures = list_pictures
		return list_pictures


	def moveBy(self, horizontal, vertical):
		"""
		Bouge le joueur sans savoir si la position est valable

		Entree: vertical(-1, 0 ou 1), horizontal(-1, 0 ou -1)
		"""
		self.pos = (self.pos[0]+self.speed*horizontal*60/self.fps, self.pos[1]+self.speed*vertical*60/self.fps)
		self.pos_pictures = (self.pos_pictures[0]+self.speed*horizontal*60/self.fps, self.pos_pictures[1]+self.speed*vertical*60/self.fps)


	def animation(self, screen):
		"""
		Affiche le vaisseau sur l'ecran en fonction de l'animation

		Entree: Ecran, fps
		"""
		self.animation_counter+=1
		self.fps = self.fps if self.fps != 0 else 0.1
		if self.animation_counter/self.fps >= self.animation_time:
			screen.blit(self.list_pictures[-1], self.pos_pictures)
			self.animation_counter = 0

		else:
			for i in range(1, len(self.list_pictures)+1):
				t = self.animation_time/len(self.list_pictures)
				if t*(i-1) <= self.animation_counter/self.fps and self.animation_counter/self.fps < t*i:
					screen.blit(self.list_pictures[i-1], self.pos_pictures)


	def _camera_move(self, pos):
		self.pos_pictures = (self.pos_pictures[0]-pos[0], self.pos_pictures[1]-pos[1])


	def _camera_zoom(self, zoom):
		mousex, mousey = pygame.mouse.get_pos()
		self.pos_pictures = (round((self.pos_pictures[0]-mousex)*zoom)+mousex, round((self.pos_pictures[1]-mousey)*zoom)+mousey)
		self.speed*=zoom
		self.proportion_on_screen*=zoom
		self.resize_pictures()

	def _screen_resize(self, old_sreen_size):
		self.resize_pictures()
		self.pos_pictures = (self.pos_pictures[0]*pygame.display.get_surface().get_size()[0]/old_sreen_size[0],
							 self.pos_pictures[1]*pygame.display.get_surface().get_size()[1]/old_sreen_size[1])
		self.speed*=pygame.display.get_surface().get_size()[0]/old_sreen_size[0]



class Bullet:
	def __init__(self, spaceship):
		self.directory = spaceship.directory

		self.type = etree.parse(self.directory+"/model.xml").xpath("/spaceship/bullet/type")[0].text
		self.damage = eval(etree.parse(self.directory+"/model.xml").xpath("/spaceship/bullet/damage")[0].text)

	def shoot(self):
		if self.type == "default":
			pass
