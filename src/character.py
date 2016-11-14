'''
David Dalisay
character.py

Represents the characters in the TRPG.
'''
import pyglet
from pyglet.gl import *

class Character:
	def __init__(self, name, image_loc, x, y, image_type="image"):
		self.name = name
		self.image_loc = image_loc
		self.x = x
		self.y = y
		self.image_type = image_type

	def set_image(self, batch_,image_type=None, image_loc=None):
		if not image_type:
			i_type = self.image_type
		else:
			i_type = image_type

		if i_type == "image":
			if image_loc:
				self.image= pyglet.image.load(image_loc)
			else:
				self.image = pyglet.image.load(self.image_loc)
		elif i_type == "animation":
			if image_loc:
				animation = pyglet.image.load_animation(image_loc)
			else:
				animation = pyglet.image.load_animation(self.image_loc)	
				self.image = animation

		self.image = pyglet.sprite.Sprite(self.image, batch=batch_)

	def scale(self, scale_factor):
		self.image.scale = scale_factor
