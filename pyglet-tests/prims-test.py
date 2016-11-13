import pyglet
from pyglet.gl import *

# Create the window, run the game.
window = pyglet.window.Window(400,400)

@window.event
def on_draw():
    pyglet.graphics.draw(3, pyglet.gl.GL_LINES,
    ('v2i', (10, 15, 30, 35, 45, 45))
)


pyglet.app.run()
