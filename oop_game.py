import pygame
import os

from hitbox import hitbox
from player import player
from projectile import projectile
from enemy import enemy
from constant import *

pygame.init()
pygame.font.init()
pygame.mixer.init()


pygame.display.set_caption('Simple Game')

win=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()


Background=pygame.image.load(os.path.join('Game','bg.jpg'))

char=pygame.image.load(os.path.join('Game','standing.png'))

bullets=[]

hit_sound=pygame.mixer.Sound(os.path.join('Game','hit.mp3'))

bullet_sound=pygame.mixer.Sound(os.path.join('Game','bullet.mp3'))

Background_sound=pygame.mixer.music.load(os.path.join('Game','music.mp3'))
pygame.mixer.music.play(-1)


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