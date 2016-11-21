import pygame
from pygame.locals import *

pygame.init()

ventana      = pygame.display.set_mode((800,600))
greenScreen  = (80,120,80)
green_object = (30,40,30)
greenlight   = (50,60,50)

help_text     = "Presione Z para entrar"
return_text   = "Presione X para volver"
title_text    ="CSLUNI Game ;)"
item_text     ="One player"
credits_text  ="Creditos"
credits1_text ="Desarrollado por:"
credits2_text ="La comunidad de software Libre de la UNI"
credits3_text ="para el taller de Python 2016."

press_start_font = "fonts/PressStart2P.ttf"
# fonts
font_title = pygame.font.Font(press_start_font, 50)
font_menu  = pygame.font.Font(press_start_font, 25)
font_text  = pygame.font.Font(press_start_font, 15)

# renders
titulo     = font_title.render(title_text, True, green_object)
one_player = font_menu.render(item_text, True, green_object)
helpText   = font_text.render(help_text, True, greenlight)
returnText = font_text.render(return_text, True, greenlight)
credits_0  = font_menu.render(credits_text, True, green_object)
credits_1  = font_text.render(credits1_text, True, greenlight)
credits_2  = font_text.render(credits2_text, True, greenlight)
credits_3  = font_text.render(credits3_text, True, greenlight)

class Grafica(object):
	def __init__(self):
		print("nuevas graficas creadas")
		pass

	def fondo(self):
		ventana.fill(greenScreen)

	def titulo(self, selection):
		if selection == 0:
			pygame.draw.rect(ventana, greenlight, (110,200,300,25))
		elif selection == 1:
			pygame.draw.rect(ventana, greenlight, (110,230,300,25))
		ventana.blit(titulo, (80,50))
		ventana.blit(one_player, (120,200))
		ventana.blit(credits_0, (120,230))
		ventana.blit(helpText, (10,550))
		pass

	def creditos(self):
		ventana.blit(credits_0, (120,230))
		ventana.blit(credits_1, (120,265))
		ventana.blit(credits_2, (120,295))
		ventana.blit(credits_3, (120,325))
		ventana.blit(returnText, (10,550))

	def drawSnake(self, secciones):
		for i in secciones:
			pygame.draw.rect(ventana, green_object, (i[0]+1,i[1]+1, 8, 8))