rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
negro = (0,0,0)
blanco = (255,255,255)
plomo = (150,150,150)
ventana = pygame.display.set_mode((600,400))

class grafica(object):
	def __init__(self):
		print("Graficas creadas")
		pygame.display.set_caption("PySix")
	def fondo(self):
		ventana.fill(negro)
		pygame.draw.line(ventana, plomo, (0,350), (600,350), 2)
	def pelota(self, pp):
		pygame.draw.circle(ventana, blanco, pp, 10)
