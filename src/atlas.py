'''
David Dalisay
atlas.py

Represents the atlas that navigates any appropriately formatted assets json i.e. terrain_atlas.json.
This module accesses the data in those assets jsons and returns any asset to the grid module.
'''
import pyglet
from pyglet.gl import *
import json
import operator

class Atlas:
	def __init__(self, name, file_loc):
		self.name = name
		self.file_loc = file_loc

		atlas_file = open(file_loc)
		self.assets = json.load(atlas_file)
		atlas_file.close()

	def get_asset(self,asset_name,batch_):
		asset_img = pyglet.image.load(self.assets["file_location"])
		asset_x = self.assets[asset_name]["x"]
		asset_y = self.assets[asset_name]["y"]
		asset_width = self.assets[asset_name]["width"]
		asset_height = self.assets[asset_name]["height"]
		asset_scale = self.assets[asset_name]["scale"]
		asset_layer = self.assets[asset_name]["layer"]
		if batch_:
			asset_sprite = pyglet.sprite.Sprite(asset_img.get_region(x=asset_x, y=asset_y, width=asset_width, height=asset_height),batch=batch_)
		else:
			asset_sprite = pyglet.sprite.Sprite(asset_img.get_region(x=asset_x, y=asset_y, width=asset_width, height=asset_height))

		asset_sprite.scale = asset_scale

		asset = {
			"image": asset_sprite,
			"name": asset_name,
			"x": asset_x,
			"y": asset_y,
			"width": asset_sprite.width,
			"height": asset_sprite.height,
			"scale": asset_sprite.scale,
			"layer": asset_layer
		}
		return asset

	def get_bitmaps(self):
		bitmaps = {asset_name:self.assets[asset_name]["bitmap"] for asset_name in self.assets if asset_name != "file_location"}
		return bitmaps

	def get_asset_names(self):
		return self.assets.keys()

	def get_assets_by_layer(self):
		assets = {asset_name:self.assets[asset_name]["layer"] for asset_name in self.assets if asset_name != "file_location"}
		sorted_assets = sorted(assets.items(), key=operator.itemgetter(1))
		return sorted_assets
