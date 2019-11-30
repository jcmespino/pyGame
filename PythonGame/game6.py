import pygame
import time
import random

display_width = 800
display_height = 600

car_width = 144

BLACK	= (0, 0, 0)
WHITE	= (255, 255, 255)
RED		= (255, 0, 0)
GREEN	= (0, 255, 0)
BLUE	= (0, 0, 255)

pygame.init()

game_display = pygame.display.set_mode((display_width, display_height))
# width, height

pygame.display.set_caption("SPLAGADUM")
clock = pygame.time.Clock()

def car(x, y, img):
	game_display.blit(img, (x, y))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(game_display, color, [thingx, thingy, thingw, thingh])

def text_objects(text, font):
	TextSurface = font.render(text, True, BLACK)
	return TextSurface, TextSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 15)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	game_display.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(5)
	game_loop()

def crash():
	message_display("DI UMANO'Y BUMANGGA ANG AMING TEAM!")

def game_loop():
	x = (display_width * 0.4)
	y = (display_height * 0.5)
	x_change = 0
	car_image = pygame.image.load('car_l.jpg')

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	gameExit = False

	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
					car_image = pygame.image.load('car_l.jpg')
				elif event.key == pygame.K_RIGHT:
					x_change = 5
					car_image = pygame.image.load('car_r.jpg')
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
			print(event)

		x += x_change

		game_display.fill(WHITE)
		things(thing_startx, thing_starty, thing_width, thing_height, BLACK)
		thing_starty += thing_speed
		car(x, y, car_image)

		if x < 0:
			game_display.fill(WHITE)
			car_image = pygame.image.load('car_dl.jpg')
			car(x, 500, car_image)
			crash()

		elif x > display_width - car_width:
			game_display.fill(WHITE)
			car_image = pygame.image.load('car_rl.jpg')
			car(500, 500, car_image)
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
exit()