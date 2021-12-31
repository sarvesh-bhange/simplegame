import pygame
import os

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


class projectile(object):
	def __init__(self,x,y,radius,colour,facing):

		self.x=x
		self.x=y
		self.x=radius
		self.x=colour
		self.x=facing
		self.vel=8*facing

	def draw(self,win):
		pygame.draw.circle(win,self.colour,(self.x,self.y),self.radius)

WIDTH,HEIGHT=500,480

pygame.display.set_caption('Simple Game')

win=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()

FPS =27

black=0,0,0

WalkRight=[pygame.image.load(os.path.join('Game','R1.png')),pygame.image.load(os.path.join('Game','R2.png')),pygame.image.load(os.path.join('Game','R3.png')),pygame.image.load(os.path.join('Game','R4.png')),pygame.image.load(os.path.join('Game','R5.png')),pygame.image.load(os.path.join('Game','R6.png')),pygame.image.load(os.path.join('Game','R7.png')),pygame.image.load(os.path.join('Game','R8.png')),pygame.image.load(os.path.join('Game','R9.png'))]

WalkLeft=[pygame.image.load(os.path.join('Game','L1.png')),pygame.image.load(os.path.join('Game','L2.png')),pygame.image.load(os.path.join('Game','L3.png')),pygame.image.load(os.path.join('Game','L4.png')),pygame.image.load(os.path.join('Game','L5.png')),pygame.image.load(os.path.join('Game','L6.png')),pygame.image.load(os.path.join('Game','L7.png')),pygame.image.load(os.path.join('Game','L8.png')),pygame.image.load(os.path.join('Game','L9.png'))]

Background=pygame.image.load(os.path.join('Game','bg.jpg'))

char=pygame.image.load(os.path.join('Game','standing.png'))

bullets=[]

run=True

def draw_window():
	win.blit(Background,(0,0))

	man.draw(win)
	for bullet in bullets:

		bullet.draw(win)

	pygame.display.update()

def man_movement(keys,man):

	if keys[pygame.K_LEFT] and man.x-man.vel > 0:
		man.x-=man.vel
		man.left=True
		man.right=False
		man.standing=False

	elif keys[pygame.K_RIGHT] and man.x+man.width+man.vel < WIDTH:
		man.x+=man.vel
		man.left=False
		man.right=True
		man.standing=False

	else:
		man.standing=True

		man.walkCount=0

man=player(300,410,64,64)

while run:
	Clock.tick(FPS)


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	for bullet in bullets:
		if bullet.x >500 and bullet.x >0:
			bullet.x += bullet.vel
		
		else:
			bullet.pop(bullet.index(bullet))


	keys=pygame.key.get_pressed()

	if keys[pygame.K_SPACE]:
		if man.left:
			facing= -1
		else:
			facing= +1

		if len(bullets)<5:
 			bullet.append(projectile(round(man.x+width//2),round(man.y+height//2),6,(black),facing)

	if not (man.isJump): 
		if keys[pygame.K_UP]:
			man.isJump=True
			man.left=False
			man.right=False
			man.walkCount=0

	else:
		# It is jumping
		if man.JumpCount >= -10:
			neg = 1
		
			if man.JumpCount<0:
				neg = -1
				
			man.y -= (man.JumpCount ** 2) * 0.5 * neg

			man.JumpCount -= 1
		
		else:
			man.isJump=False
			man.JumpCount = 10

	draw_window()
	man_movement(keys,man)

pygame.QUIT
