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
import operator

class TileImage:
	def __init__(self, x, y, image=None, image_desc=None, layer=None):
		self.actual_image = image
		self.image = image
		self.set_image(self.image)
		self.image_desc = image_desc
		self.set_xy(x, y)
		self.layer = layer

	def set_selected_image(self, image):
		self.selected_image = image
		self.image = image

	def set_image(self, image=None):
		if not image:
			self.image = pyglet.sprite.Sprite(self.image)
		else:
			self.image = image

	def set_xy(self, x, y):
		self.x = x
		self.y = y

		self.image.x = x
		self.image.y = y

	def get_image(self):
		return self.image

class Tile:
	def __init__(self, x_index, y_index, width, height):
		self.tile_images = []

		self.selected = False

		self.width = width
		self.height = height

		# Indices used for grid locations.
		# These are NOT the tile's image x,y locations.
		self.x_index = x_index
		self.y_index = y_index

	def add_image(self, image, image_desc=None, layer=None):
		tile_image = TileImage(self.x, self.y, image, image_desc, layer)
		self.tile_images.append(tile_image)

	def set_xy(self, x, y):
		self.x = x
		self.y = y

	def get_xy(self):
		return (self.x, self.y)

	def get_image_descriptions(self):
		return [tile_image.image_desc for tile_image in self.tile_images]

	def deselect(self):
		self.selected = False

	def select(self):
		self.selected = True
