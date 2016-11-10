'''
David Dalisay
scene.py

Object representing a Scene in the TRPG.
'''
import pyglet
from pyglet.gl import *

class Scene:
	def __init__(self, grid, huds):
		self.grid = grid
		self.huds = huds

		# Bundle all huds into one draw batch.
		self.hud_image_batch = pyglet.graphics.Batch()
		self.batch_hud_images()

	def batch_hud_images(self):
		for hud in self.huds:
			hud.image.batch = self.hud_image_batch

	def draw_grid(self):
		self.grid.draw()
		

	def draw_huds(self, x, y):
		for hud in self.huds:
			hud.update(x, y)
			hud.draw()
		#self.huds[0].draw(x, y)#self.hud_image_batch.draw()
			