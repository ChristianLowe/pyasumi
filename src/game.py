'''
David Dalisay
game.py

Runs the game as a pyglet application.
'''
import pyglet
from pyglet.gl import *
from grid import Grid

window = pyglet.window.Window(500,500,resizable=True)

atlas_file = "terrain_atlas.json"
g = Grid(10,10,50,50,atlas_file)

@window.event
def on_draw():
 	window.clear()
 	g.draw()

pyglet.app.run()
