import pygame
import os
from hitbox import hitbox
from constant import *

WalkRight=[pygame.image.load(os.path.join('Game','R1.png')),pygame.image.load(os.path.join('Game','R2.png')),pygame.image.load(os.path.join('Game','R3.png')),pygame.image.load(os.path.join('Game','R4.png')),pygame.image.load(os.path.join('Game','R5.png')),pygame.image.load(os.path.join('Game','R6.png')),pygame.image.load(os.path.join('Game','R7.png')),pygame.image.load(os.path.join('Game','R8.png')),pygame.image.load(os.path.join('Game','R9.png'))]

WalkLeft=[pygame.image.load(os.path.join('Game','L1.png')),pygame.image.load(os.path.join('Game','L2.png')),pygame.image.load(os.path.join('Game','L3.png')),pygame.image.load(os.path.join('Game','L4.png')),pygame.image.load(os.path.join('Game','L5.png')),pygame.image.load(os.path.join('Game','L6.png')),pygame.image.load(os.path.join('Game','L7.png')),pygame.image.load(os.path.join('Game','L8.png')),pygame.image.load(os.path.join('Game','L9.png'))]

char=pygame.image.load(os.path.join('Game','standing.png'))

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
		self.showHitbox=False

		

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

		self.hitbox.update(self.x + 17, self.y + 14, 26, 49);
		
		if self.showHitbox:
			pygame.draw.rect(win,red,(self.hitbox.get_rect()),2)

	def hit(self,win):
		self.x=60
		self.y=410
		self.walkCount = 0

		winner_font=pygame.font.SysFont('comicsans',100)
		winner_text=winner_font.render('-5',1,(red))
		win.blit(winner_text,(WIDTH/2-(winner_text.get_width()/2),200))
		pygame.display.update()

		i=0
		while i<100:
			pygame.time.delay(10)
			i+=1
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					i=103
					pygame.quit()

			
