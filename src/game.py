'''
David Dalisay
game.py

Runs the game as a pyglet application.
'''
import pyglet
from pyglet.gl import *
from grid import Grid
from hud import Hud
from scene import Scene
from window import Window

# Create a grid with a specific atlas.
g = Grid(10,10,50,50,"terrain_atlas.json")

# Create a few HUDs.
meter_hud = Hud(x_offset=15, y_offset=80, hud_image_loc="../images/ui/hud-test.png")
heart_hud0 = Hud(x_offset=120, y_offset=40, hud_image_loc="../images/ui/heart.png")
heart_hud0.image.scale = 0.55
heart_hud1 = Hud(x_offset=140, y_offset=40, hud_image_loc="../images/ui/heart.png")
heart_hud1.image.scale = 0.55
huds = [meter_hud, heart_hud0, heart_hud1]

# Create a scene with a grid and some huds attached.
s = Scene(g,huds)

# Create the window, run the game.
window = Window(400,400,scene=s)

pyglet.app.run()

