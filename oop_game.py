import pygame
import os
pygame.init()

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
		self.hitbox=(self.x + 17, self.y + 4, 26, 57)

		

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

		self.hitbox=(self.x + 17, self.y + 4, 26, 57)
		pygame.draw.rect(win,red,(self.hitbox),2)


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
		self.hitbox=(self.x + 17, self.y + 1, 33, 57)


	def draw(self,win):
		self.move()

		if self.walkCount + 1>=33:
			self.walkCount=0

		if self.vel>0:
			win.blit(self.WalkRight[self.walkCount//3],(self.x,self.y))
			self.walkCount+=1

		else:
			win.blit(self.WalkLeft[self.walkCount//3],(self.x,self.y))
			self.walkCount+=1
		self.hitbox=(self.x + 17, self.y + 1, 33, 57)
		pygame.draw.rect(win,red,(self.hitbox),2)		

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

WIDTH,HEIGHT=500,480

pygame.display.set_caption('Simple Game')

win=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()

FPS =27

black=0,0,0
red=255,0,0

WalkRight=[pygame.image.load(os.path.join('Game','R1.png')),pygame.image.load(os.path.join('Game','R2.png')),pygame.image.load(os.path.join('Game','R3.png')),pygame.image.load(os.path.join('Game','R4.png')),pygame.image.load(os.path.join('Game','R5.png')),pygame.image.load(os.path.join('Game','R6.png')),pygame.image.load(os.path.join('Game','R7.png')),pygame.image.load(os.path.join('Game','R8.png')),pygame.image.load(os.path.join('Game','R9.png'))]

WalkLeft=[pygame.image.load(os.path.join('Game','L1.png')),pygame.image.load(os.path.join('Game','L2.png')),pygame.image.load(os.path.join('Game','L3.png')),pygame.image.load(os.path.join('Game','L4.png')),pygame.image.load(os.path.join('Game','L5.png')),pygame.image.load(os.path.join('Game','L6.png')),pygame.image.load(os.path.join('Game','L7.png')),pygame.image.load(os.path.join('Game','L8.png')),pygame.image.load(os.path.join('Game','L9.png'))]

Background=pygame.image.load(os.path.join('Game','bg.jpg'))

char=pygame.image.load(os.path.join('Game','standing.png'))

bullets=[]

def draw_window():
	win.blit(Background,(0,0))

	man.draw(win)
	for bullet in bullets:
		bullet.draw(win)

	goblin.draw(win)

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
goblin=enemy(100, 415, 64, 64, 300)

shootloop=0

run=True
while run:
	Clock.tick(FPS)

	if shootloop > 0:
		shootloop +=1
	if shootloop > 3:
		shootloop=0


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	for bullet in bullets:
		if bullet.x-bullet.radius < goblin.hitbox[0]+goblin.hitbox[2] and bullet.x+bullet.radius:
			if bullet.y-bullet.radius<goblin.hitbox[1]+goblin.hitbox[3]:
				bullets.pop(bullets.index(bullet))

		if bullet.x < WIDTH and bullet.x >0:
			bullet.x += bullet.vel
		
		else:
			bullets.pop(bullets.index(bullet))


	keys=pygame.key.get_pressed()

	if keys[pygame.K_SPACE] and shootloop==0:
		if man.left:
			facing= -1
		else:
			facing= 1

		if len(bullets)<3:
 			bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(black),facing))

 			shootloop=1

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

pygame.quit()