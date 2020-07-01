import pygame, sys, math, time
from pygame.locals import *

pygame.init()

PI = math.pi
Xside = 2000
Yside = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
angle = PI/3
angac = 0
angvel = 0
#LENGTH = 300
LENGTH = 700
Lx = Xside/2 + LENGTH * math.sin(angle)
Ly = 50 + LENGTH * math.cos(angle)

#display function
DISPLAY = pygame.display.set_mode((Xside, Yside))
#DISPLAY = pygame.display.set_mode((, 20))
pygame.display.set_caption('pendulum')

#pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
#pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
while True: # main game loop
	#DISPLAY.fill(WHITE)
	DISPLAY.fill(RED)
	#draw pendulum
	for i in range(1,1000): 
		#pygame.draw.circle(DISPLAY, BLUE, (Xside/2, i), 5, 2)
		pygame.draw.circle(DISPLAY, GREEN, (Xside/2, i), 1, 1)
		pygame.draw.aaline(DISPLAY, YELLOW, (Xside/2, i), (Lx, Ly), 4)
		pygame.draw.circle(DISPLAY, GREEN, (int(Lx), int(Ly)), 20, 0)
	
	#pygame.draw.circle(DISPLAY, BLUE, (Xside/2, 0), 4, 2)
	#pygame.draw.aaline(DISPLAY, WHITE, (Xside/2, 0), (Lx, Ly), 3)
	#pygame.draw.circle(DISPLAY, GREEN, (int(Lx), int(Ly)), 20, 0)
		
	Lx = Xside/2 + LENGTH * math.sin(angle)
	Ly = 1 + LENGTH * math.cos(angle)
	#math calculas
	angac = -0.01 * math.sin(angle)
	angle += angvel
	angvel += angac
	angvel *= 0.99
	
#exit event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	time.sleep(0.1)
	pygame.display.update()
