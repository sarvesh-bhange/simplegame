import pygame
import os
from hitbox import hitbox
from constant import *


WalkRight=[pygame.image.load(os.path.join('Game','R1.png')),pygame.image.load(os.path.join('Game','R2.png')),pygame.image.load(os.path.join('Game','R3.png')),pygame.image.load(os.path.join('Game','R4.png')),pygame.image.load(os.path.join('Game','R5.png')),pygame.image.load(os.path.join('Game','R6.png')),pygame.image.load(os.path.join('Game','R7.png')),pygame.image.load(os.path.join('Game','R8.png')),pygame.image.load(os.path.join('Game','R9.png'))]

WalkLeft=[pygame.image.load(os.path.join('Game','L1.png')),pygame.image.load(os.path.join('Game','L2.png')),pygame.image.load(os.path.join('Game','L3.png')),pygame.image.load(os.path.join('Game','L4.png')),pygame.image.load(os.path.join('Game','L5.png')),pygame.image.load(os.path.join('Game','L6.png')),pygame.image.load(os.path.join('Game','L7.png')),pygame.image.load(os.path.join('Game','L8.png')),pygame.image.load(os.path.join('Game','L9.png'))]

class player(object):
	def __init__(self, x,y,width,height):
		
		self.x = x
		self.y= y
		self.vel=5
		self.width= width
		self.height= height
		self.isJump=False
		self.JumpCount=10
		self.left=False
		self.right=False
		self.walkCount=0
		self.standing=True
		self.hitbox= hitbox(self.x + 17,self.y + 4,26,57 )

		

	def draw(self,win):

		if self.walkCount +1 >= 27:

			self.walkCount=0
		if not(self.standing):
			if self.left:
				win.blit(WalkLeft[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1

			elif self.right:
				win.blit(WalkRight[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1
		
		elif self.right:
			win.blit(WalkRight[0],(self.x,self.y))

		else:
			win.blit(WalkLeft[0],(self.x,self.y))

		self.hitbox.update(self.x + 17, self.y + 4, 26, 57);
		pygame.draw.rect(win,red,(self.hitbox.get_rect()),2)

	# def Hit():
	# 	self.x=60
	# 	self.y=410
	# 	self.walkCount=0

	# 	winner_text=pygame.font.SysFont('comicsans',100,True)
	# 	text1=font.render('-5')
	# 	win.blit(win,text1,(250-(pygame.width_get()/2),200))
	# 	pygame.display.update()

	# 	i=0
	# 	while i<300:
	# 		i+=1
	# 		for event in pygame.event.get:
	# 			if event.type==pygame.QUIT:
	# 				i=301