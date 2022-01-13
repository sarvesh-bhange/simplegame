import pygame

class projectile(object):
	def __init__(self,x,y,radius,colour,facing):

		self.x=x
		self.y=y
		self.radius=radius
		self.colour=colour
		self.facing=facing
		self.vel=8*facing

	def draw(self,win):
		pygame.draw.circle(win,self.colour,(self.x,self.y),self.radius)