import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
vertex_list = batch.add(
	2,
	pyglet.gl.GL_POINTS,
	None,
    ('v2i', (10, 15, 30, 35)),
    ('c3B', (0, 0, 255, 0, 255, 0))
)

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')


@window.event
def on_draw():
 	window.clear()
 	batch.draw()

pyglet.app.run()
