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
		self.tiles = []
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
					val = bitmap[row][col]
					if val == 1:
						asset = self.atlas.get_asset(bm_key, self.batches[bm_key])
						self.tiles.append(Tile(x_loc, y_loc, asset["image"]))
				y_loc += y_tile_gap
			x_loc += x_tile_gap

	def draw(self):
		assets_by_layer = self.atlas.get_assets_by_layer()
		for asset in assets_by_layer:
			asset_name = asset[0]
			self.batches[asset_name].draw()

				


