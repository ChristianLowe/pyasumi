'''
David Dalisay
scene.py

Object representing a Scene in the TRPG.
'''
import pyglet
from pyglet.gl import *
from pyglet.window import key

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

	def key_pressed(self, symbol):
		if symbol == key.UP:
			self.grid.move_selected_tile_up()

		if symbol == key.DOWN:
			self.grid.move_selected_tile_down()

		if symbol == key.LEFT:
			self.grid.move_selected_tile_left()

		if symbol == key.RIGHT:
			self.grid.move_selected_tile_right()

	def print_selected_tile(self):
		self.grid.get_selected_tile()

	def draw_huds(self, x, y):
		for hud in self.huds:
			hud.update(x, y)
			hud.draw()
		#self.huds[0].draw(x, y)#self.hud_image_batch.draw()
