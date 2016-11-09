'''
David Dalisay
tile.py

Object representing each tile (square) on the grid.

Note: There can be multiple tiles on the same spot on the grid. This allows for layering.
i.e. If you want to draw objects like a flower, on dirt, on grass - You must use 3 tiles on the same spot.
'''
import pyglet
from pyglet.gl import *
import math

class Tile:
	def __init__(self, x, y, image=None, image_loc=None):
		self.image = image
		self.image.x = x
		self.image.y = y

	def set_image(self, image_loc=None):
		self.image = pyglet.image.load(self.image_loc)
		self.image = pyglet.sprite.Sprite(self.image)

	def get_image(self):
		return self.image

	def draw(self):
		self.image.draw()