import pygame
import random
pygame.init()

i = 0
screen = pygame.display.set_mode((512,512))

class movable_rect:
	def __init__(self,posx,posy,side1,side2 = None):
		self.posy = posy
		self.posx = posx
		self.side1 = side1
		self.side2 = side2

		if self.posx == "random":
				self.posx = random.randint(0-(self.side1 // 2), 512+(self.side1 // 2))

		if self.posy != "random":
			self.posy = random.randint(0-(self.side2 // 2), 512+(self.side2 // 2))
			if self.side2 != None:
				pygame.draw.rect(screen, (255,0,0), (self.posx, self.posy, self.side1, self.side2))
			elif self.side2 == None:
				pygame.draw.rect(screen, (255,0,0), (self.posx, self.posy, self.side1, self.side1))



		if self.posy == "random":
			self.posy = random.randint(0-(self.side2 // 2), 512+(self.side2 // 2))
			if self.side2 != None:
				pygame.draw.rect(screen, (255,0,0), (self.posx, self.posy, self.side1, self.side2))
			elif self.side2 == None:
				pygame.draw.rect(screen, (255,0,0), (self.posx, self.posy, self.side1, self.side1))


		
		

run = True
while run:
	
	screen.fill((255,255,255))
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			run = False


	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		objs = [movable_rect("random", "random", 10,10) for i in range(100)]
			





	pygame.display.update()

pygame.quit()


