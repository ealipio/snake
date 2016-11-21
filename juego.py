import pygame
from pygame.locals import *

SCREENRECT = Rect(0,0,640,480)

def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREENRECT.size)

	#make background
	background = pygame.Surface(SCREENRECT.size).convert()
	background.fill((0,255,0))
	screen.blit(background, (0,0))
	pygame.display.update()

	# keep track of sprites
	all = pygame.sprite.RenderUpdates()
	# keep track of time
	all = pygame.time.Clock()
	# game loop
	while True:
		# get Input
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
				return
		# clear sprites
		all.clear(screen, background)
		# update sprites
		all.update()

		# redraw sprites
		dirty = all.draw(screen)
		pygame.display.update(dirty)

		# maintain frame rate
		clock.tick(30)

if __name__ == '__main__' : main()