import pygame
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()

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

hit_sound=pygame.mixer.Sound(os.path.join('Game','hit.mp3'))

bullet_sound=pygame.mixer.Sound(os.path.join('Game','bullet.mp3'))

Background_sound=pygame.mixer.music.load(os.path.join('Game','music.mp3'))
pygame.mixer.music.play(-1)

class hitbox(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width

	def get_rect(self):
		return (self.x,self.y,self.width,self.height)

	def update(self,x,y,width,height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width

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
	# 				pygame.quit()

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

def draw_window():
	win.blit(Background,(0,0))

	text=font.render('score:'+str(score),1,(black))

	win.blit(text,(20,10))

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
font=pygame.font.SysFont('comicsans',30,True)
goblin=enemy(100, 415, 64, 64, 450)

score=0

shootloop=0

run=True
while run:
	Clock.tick(FPS)

	# if health

	if shootloop > 0:
		shootloop +=1
	if shootloop > 3:
		shootloop=0


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False



	# if(man.hitbox[1] < goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3] >  goblin.hitbox[1]):
	# 	if (man.hitbox[0]+goblin.hitbox[1] > goblin.hitbox[0]+goblin.hitbox[2] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[2]):
	# 		man.hit()

	# 		score-=5

	# 		bullets.pop(bullets.index(bullet))	

	for bullet in bullets:

		# Collision of projectile with goblin
		bullet_center_x = bullet.x + bullet.radius
		bullet_center_y = bullet.y + bullet.radius

		if(bullet_center_x > goblin.hitbox.x and bullet_center_x < goblin.hitbox.x + goblin.hitbox.width):
			if (bullet_center_y > goblin.hitbox.y and bullet_center_y < goblin.hitbox.y + goblin.hitbox.height):
				hit_sound.play()
				goblin.hit()

				score+=1

				bullets.pop(bullets.index(bullet))

		# Collision of projectile with wall
		if bullet.x < WIDTH and bullet.x >0:
			bullet.x += bullet.vel
		
		else:
			bullets.pop(bullets.index(bullet))


	keys=pygame.key.get_pressed()

	if keys[pygame.K_SPACE] and shootloop==0:
		bullet_sound.play()
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