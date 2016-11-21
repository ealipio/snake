import pygame, sys, graph as graficas
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("CSLUNI Game")

g = graficas.Grafica()

# Variables
fase = 0
selectionmenu = 0
secciones = [(80,80), (80,90)]

# loop game:
while True:
	###########################
	if fase == 0:
		g.fondo()
		g.titulo(selectionmenu)
	elif fase == 1:
		g.fondo()
		g.drawSnake(secciones)
		print("access: one player")
		pass
	elif fase == 2:
		g.fondo()
		g.creditos()
		print("access: creditos")
		pass
	###########################
	# events body
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
			pass
		elif evento.type == KEYDOWN:
			if fase == 0:
				if evento.key == pygame.K_DOWN:
					if selectionmenu < 1:
						selectionmenu += 1
					else:
						selectionmenu = 0
				elif evento.key == pygame.K_UP:
					if selectionmenu > 0:
						selectionmenu -= 1
					else:
						selectionmenu = 1
				## eleccion con la tecla [Z]
				elif evento.key == pygame.K_z:
					if selectionmenu == 0:
						fase = 1
					elif selectionmenu == 1:
						fase = 2
		elif evento.type == KEYUP:
			pass
	pygame.display.update()
	pass

print("Todo Funcionando")
# Fuente: youtube.com/watch?v=Dm32c_G_Cik