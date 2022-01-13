import pygame
import os
from hitbox import hitbox
from constant import *

class enemy(object):
	WalkLeft=[pygame.image.load(os.path.join('Game','L1E.png')),pygame.image.load(os.path.join('Game','L2E.png')),pygame.image.load(os.path.join('Game','L3E.png')),pygame.image.load(os.path.join('Game','L4E.png')),pygame.image.load(os.path.join('Game','L5E.png')),pygame.image.load(os.path.join('Game','L6E.png')),pygame.image.load(os.path.join('Game','L7E.png')),pygame.image.load(os.path.join('Game','L8E.png')),pygame.image.load(os.path.join('Game','L9E.png')),pygame.image.load(os.path.join('Game','L10E.png')),pygame.image.load(os.path.join('Game','L11E.png'))]

	WalkRight=[pygame.image.load(os.path.join('Game','R1E.png')),pygame.image.load(os.path.join('Game','R2E.png')),pygame.image.load(os.path.join('Game','R3E.png')),pygame.image.load(os.path.join('Game','R4E.png')),pygame.image.load(os.path.join('Game','R5E.png')),pygame.image.load(os.path.join('Game','R6E.png')),pygame.image.load(os.path.join('Game','R7E.png')),pygame.image.load(os.path.join('Game','R8E.png')),pygame.image.load(os.path.join('Game','R9E.png')),pygame.image.load(os.path.join('Game','R10E.png')),pygame.image.load(os.path.join('Game','R11E.png'))]

	def __init__(self,x,y,width,height,end):

		self.x=x
		self.vel=3
		self.y=y
		self.width=width
		self.height=height
		self.end=end
		self.walkCount=0
		self.path=[x,end]
		self.hitbox= hitbox(self.x + 17, self.y + 1, 33, 57)
		self.health=10
		self.visiable=True


	def draw(self,win):
		self.move()

		if self.visiable:

			if self.walkCount + 1>=33:
				self.walkCount=0

			if self.vel>0:
				win.blit(self.WalkRight[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1

			else:
				win.blit(self.WalkLeft[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1

			self.hitbox.update(self.x + 17, self.y + 2, 31, 57)

			# health bar background 
			
			pygame.draw.rect(win, (black), (self.hitbox.x, self.hitbox.y-20, 50, 10))
			
			#  shrinking health bar
			pygame.draw.rect(win,(red),(self.hitbox.x,self.hitbox.y-20,50-(5*(10-self.health)),10))
			
			pygame.draw.rect(win,red,(self.hitbox.get_rect()),2)	


	def move(self):
		if self.vel>0:
			if self.x + self.vel < self.path[1]:
				self.x+=self.vel

			else:
				self.vel= self.vel * -1
				self.x+self.vel
				self.walkCount=0
		else:
			if self.x - self.vel > self.path[0]:
				self.x+=self.vel
				
			else:
				self.vel= self.vel * -1
				self.x+self.vel
				self.walkCount=0

	def hit(self):
		if self.health>0:
			self.health-=1
		else:
			self.visiable=False