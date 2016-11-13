'''
David Dalisay
grid.py

Object representing a Grid of a Scene in the TRPG.
'''
import pyglet
from pyglet.gl import *
import random
from tile import Tile
from atlas import Atlas

class Grid:
	def __init__(self, x, y, x_tile_gap, y_tile_gap, atlas_file):
		self.set_atlas(atlas_file, atlas_file)
		self.set_tiles(x, y, x_tile_gap, y_tile_gap)

	def set_atlas(self, atlas_name, atlas_file_loc):
		self.atlas = Atlas(atlas_name, atlas_file_loc)

	# The integer value at each bitmap position will represent an asset id assigned to an asset
	# in the atlas json.
	def set_tiles(self, x, y, x_tile_gap, y_tile_gap):
		self.tiles = [[Tile(i,j) for i in range(x)] for j in range(y)]
		self.selected_x = 0
		self.selected_y = 0

		self.batches = {}

		bitmaps = self.atlas.get_bitmaps()

		x_loc = 0
		for row in range(x):
			y_loc = 0
			for col in range(y):
				for bm_key in bitmaps:
					if bm_key not in self.batches:
						self.batches[bm_key] = pyglet.graphics.Batch()
					bitmap = bitmaps[bm_key]
					do_draw = bitmap[row][col]
					if do_draw == 1:
						asset = self.atlas.get_asset(bm_key, self.batches[bm_key])
						self.tiles[row][col].set_xy(x_loc, y_loc)
						self.tiles[row][col].add_image(asset["image"],asset["name"],asset["layer"])
				y_loc += y_tile_gap
			x_loc += x_tile_gap

	def get_selected_tile(self):
		print("selected tile: ({},{},{})".format(self.selected_x, self.selected_y, self.tiles[self.selected_x][self.selected_y].get_image_descriptions()))

	def move_selected_tile_up(self):
		self.selected_y += 1

	def move_selected_tile_left(self):
		self.selected_x -= 1

	def move_selected_tile_right(self):
		self.selected_x += 1

	def move_selected_tile_down(self):
		self.selected_y -= 1

	# Grid's draw method doesn't call tile's draw method.
	# For optimization purposes, it uses batches that hold the tile's images.
	# @TODO: Create 2 draw methods that can do either one of those options.
	def draw(self):
		assets_by_layer = self.atlas.get_assets_by_layer()
		for asset in assets_by_layer:
			asset_name = asset[0]
			self.batches[asset_name].draw()
