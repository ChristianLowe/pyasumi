from pyglet.gl import *
import pyglet

class hud():
    def __init__(self):
        self.infotext = pyglet.text.Label('Hello, world',
                          font_name='Free Serif',
                          font_size=36,
                          x=10, y=20)
        
    def draw(self, width, height):
        glPushMatrix()
        glViewport(0, 0, width, height)
        glMatrixMode(gl.GL_PROJECTION)
        glLoadIdentity();
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(gl.GL_MODELVIEW)
        self.infotext.draw()
        glPopMatrix()


window = pyglet.window.Window(500,500,resizable=True)
h = hud()
@window.event
def on_draw():
	window.clear()
	h.draw(500,500)
pyglet.app.run()
