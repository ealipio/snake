import pygame, sys 
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()


#def factorial(n):
#	if(n==0):
#		return 1
#	else:
#		return n*factorial(n-1)
#
#cinco = factorial(5)
#print(cinco)	