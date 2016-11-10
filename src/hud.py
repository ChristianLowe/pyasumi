'''
David Dalisay
hud.py

Object representing a HUD in a Scene in the TRPG.
'''
import pyglet
from pyglet.gl import *

class AnchorHud:
    def __init__(self):
        self.infotext = pyglet.text.Label('Hello, world',
                          font_name='Free Serif',
                          font_size=36,
                          x=10, y=20)
        print("created anchorhud")
        
    def draw(self, width, height):
        glPushMatrix()
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity();
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        self.infotext.draw()
        glPopMatrix()

class Hud:
	def __init__(self,x_offset, y_offset, hud_text=None, hud_text_font=None, hud_image_loc=None):
		self.label = None
		if hud_text:
			self.text = hud_text
			self.label = pyglet.text.Label(
							self.text,
                          	font_name='Times New Roman',
                          	font_size=12,
                          	x=x, y=y,
                          	anchor_x='left', anchor_y='center'
                         )

		if hud_image_loc:
			self.image = pyglet.image.load(hud_image_loc)
			self.image = pyglet.sprite.Sprite(self.image)

		self.x_offset = x_offset
		self.y_offset = y_offset

	def update(self, window_width, window_height):
		self.image.x = window_width - (window_width-self.x_offset)
		self.image.y = window_height - self.y_offset

	def draw(self):
		if self.image:
			self.image.draw()
		
		if self.label:
			self.label.draw()

