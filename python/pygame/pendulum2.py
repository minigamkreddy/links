import pygame
import sys
import math
import time
from pygame.locals import *

pygame.init()

PI = math.pi
Xside = 2000
Yside = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#RED = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (1,255,255)
#BLUE = (0, 0, 255)
#angle1 = PI/3
angle1 = PI/4
aAccel1 = 0
aVel1 = 0
L1 = 500
#L1 = 150
angle2 = PI/2
aAccel2 = 0
aVel2 = 0
L2 = 300
g = 1
m1 = 15
m2 = 15

L1x = Xside/2 + L1 * math.sin(angle1)
L1y = 50 + L1 * math.cos(angle1)

L2x = L1x + L2 * math.sin(angle2)
L2y = L1y + L2 * math.cos(angle2)

#display function
DISPLAY = pygame.display.set_mode((Xside, Yside))
pygame.display.set_caption('_____ball_____')

#pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
#pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
while True: # main game loop
	DISPLAY.fill(WHITE)
	#draw pendulum 
	pygame.draw.circle(DISPLAY, BLUE, (Xside/2, 50), 5, 2)
	pygame.draw.aaline(DISPLAY, RED, (Xside/2, 50), (L1x, L1y), 4)
	pygame.draw.circle(DISPLAY, GREEN, (int(L1x), int(L1y)), 15, 0)
	pygame.draw.aaline(DISPLAY, RED, (L1x, L1y), (L2x, L2y), 4)
	pygame.draw.circle(DISPLAY, GREEN, (int(L2x), int(L2y)), 15, 0)
	L1x = Xside/2 + L1 * math.sin(angle1)
	L1y = 50 + L1 * math.cos(angle1)
	L2x = L1x + L2 * math.sin(angle2)
	L2y = L1y + L2 * math.cos(angle2)
	aAccel1 = (-g*(2*m1+m2)*math.sin(angle1)-m2*g*math.sin(angle1-2*angle2)-2*math.sin(angle1-angle2)*m2*(aVel2*aVel2*L2+aVel1*aVel1*L1*math.cos(angle1-angle2)))/(L1*(2*m1+m2-m2*math.cos(2*angle1-2*angle2)))
	aAccel2 = (2*math.sin(angle1-angle2)*(aVel1*aVel1*L1*(m1+m2)+g*(m1+m2)*math.cos(angle1)+aVel2*aVel2*L2*math.cos(angle1-angle2)))/(L2*(2*m1+m2-m2*math.cos(2*angle1-2*angle2)))

	angle1 += aVel1
	aVel1 += aAccel1
	aVel1 *= 0.99
	angle2 += aVel2
	aVel2 += aAccel2
	aVel2 *= 0.99
#exit event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	time.sleep(0.1)
	pygame.display.update()
