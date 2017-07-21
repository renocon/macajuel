#!/usr/bin/python
# -*- coding: utf-8 -*-

# pygame game

import pygame
import sys
import random

SCREEN_SIZE = (WIDTH, HEIGHT) = (800, 640)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
SCORE_LIMIT = 5
SQUARE_SIDE = 8

pygame.init()
font = pygame.font.SysFont('arial', 30)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
paused = False
game_over = False

x_velocity = 1
y_velocity = 0
snake = []
treat = {'x': -1, 'y': -1}
score = 0
player1 = None
player2 = None

class Mouse():
	"""Mouse Class"""

	def __init__(self,pyg,screen_width = 800, screen_height = 640, side = 8, color = (0,0,0)):
		self.pygame = pyg
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.side = side
		self.color = color


class Snake():
	"""Player class"""

	def __init__(self,pyg,start_orientation = 1, screen_width = 800, screen_height = 640, side = 8,color = (0,0,0), space = 10, baby_length = 5):
		self.start_orientation = start_orientation
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.side = side
		self.color = color
		self.screen = screen
		self.score = 0
		self.space = space
		self.x_velocity = start_orientation
		self.y_velocity = 0
		self.moved = False
		self.pygame = pyg
		self.baby_length = baby_length
		self.init_position()


	def init_position(self):
		self.snake = []
		for i in range(1,self.baby_length+1):
			x = ((self.screen_width / 2) - (self.side * i* self.start_orientation)) 
			y = self.screen_height/2 + (self.start_orientation * self.side)
			self.snake.append({'x':x, 'y':y})


	def draw(self):
		for i in self.snake:
			self.pygame.draw.rect(self.screen, self.color, ((i['x'], i['y']),(self.side, self.side)))

	
	def in_screen(self,x,y):
		if x <= self.screen_width - self.side and x >= 0 and y <= self.screen_height - self.side and y >= 0:
			return True
		return False		

    	
	def update(self, mouse = None, player = None):
		new_x = self.snake[0]['x'] + (self.x_velocity * self.side)
		new_y = self.snake[0]['y'] + (self.y_velocity * self.side)
		inbound = self.in_screen(new_x,new_y)    
		# print(str(inbound)+' '+str(new_x)+' '+str(new_y))
		if (inbound):
			self.snake[0]['x'] = new_x
			self.snake[0]['y'] = new_y
			for (i, j) in reversed(list(enumerate(self.snake))):
				if i > 0:
					self.snake[i]['x'] = self.snake[i - 1]['x']
					self.snake[i]['y'] = self.snake[i - 1]['y']	
		self.moved = True
		# print(str(self.start_orientation)+ '. ' + str(self.snake[0]))
		if mouse is not None:
			return
		if player is not None:
			return


	def up(self):
		if self.moved and self.y_velocity == 0:
			self.x_velocity = 0
			self.y_velocity = -1
		self.moved = False


	def down(self):
		if self.moved and self.y_velocity == 0:
			self.x_velocity = 0
			self.y_velocity = 1
		self.moved = False


	def left(self):
		if self.moved and self.x_velocity == 0:
			self.x_velocity = -1
			self.y_velocity = 0
		self.moved = False


	def right(self):
		if self.moved and self.x_velocity == 0:
			self.x_velocity = 1
			self.y_velocity = 0
		self.moved = False


	def win(self,other_player = None):
		self.score += 1
		if other_player is not None:
			other_player.lose()
	
	def lose(self):
		self.init_snake()
		self.score -= 1




def snake_init():
    for i in range(1, 6):
        x = WIDTH / 2 - SQUARE_SIDE * i
        y = HEIGHT / 2
        snake.append({'x': x, 'y': y})


def treat_init():
    treat['x'] = (random.randint(0, (WIDTH - SQUARE_SIDE)/SQUARE_SIDE) * SQUARE_SIDE)
    treat['y'] = (random.randint(0, (HEIGHT - SQUARE_SIDE)/SQUARE_SIDE) * SQUARE_SIDE)


def score_init():
    global score
    score = 0


def init():
    # treat_init()
    # snake_init()
    # score_init()
    global player1
    global player2
    player1 = Snake(pygame,1,color=GREEN)
    player2 = Snake(pygame,-1,color=BLUE)


def snake_update(key_presses):
    global x_velocity
    global y_velocity
    if (key_presses[pygame.K_w] or key_presses[pygame.K_UP]) and y_velocity == 0:
        y_velocity = -1
        x_velocity = 0
    if (key_presses[pygame.K_s] or key_presses[pygame.K_DOWN]) and y_velocity == 0:
        y_velocity = 1
        x_velocity = 0
    if (key_presses[pygame.K_a] or key_presses[pygame.K_LEFT]) and x_velocity == 0:
        y_velocity = 0
        x_velocity = -1
    if (key_presses[pygame.K_d] or key_presses[pygame.K_RIGHT]) and x_velocity == 0:
        y_velocity = 0
        x_velocity = 1
    


        # print(i)
        # print(j)
    # if player['y'] >= 0:
    #     if key_presses[pygame.K_w] or key_presses[pygame.K_UP]:
    #         player['y'] -= player['velocity']['y']
    # if player['y'] + player['height'] <= HEIGHT:
    #     if key_presses[pygame.K_s] or key_presses[pygame.K_DOWN]:
    #         player['y'] += player['velocity']['y']

# def treat_update():
    # global score
    # global snake
    # if treat['x'] == snake[0]['x'] and treat['y'] == snake[0]['y']:
    	# score += 1
    	# snake.append({'x':0,'y':0})
    	# treat_init()


def update(key_presses,treat):
    # treat_update()
    # snake_u(key_presses)
    if (key_presses[pygame.K_w]):
    	player1.up()
    if (key_presses[pygame.K_s]):
    	player1.down()
    if (key_presses[pygame.K_a]):
    	player1.left()
    if (key_presses[pygame.K_d]):
    	player1.right()
    if (key_presses[pygame.K_UP]):
    	player2.up()
    if (key_presses[pygame.K_DOWN]):
    	player2.down()
    if (key_presses[pygame.K_LEFT]):
    	player2.left()
    if (key_presses[pygame.K_RIGHT]):
    	player2.right()	
    player1.update(mouse = treat, player = player2)
    player2.update(mouse = treat, player = player1)


def draw_snake():
    for i in snake:
        pygame.draw.rect(screen, GREEN, ((i['x'], i['y']),
                         (SQUARE_SIDE, SQUARE_SIDE)))


def render():
    screen.fill(BLACK)

    # Draw score

    player_score = font.render(str(score), True, WHITE)
    screen.blit(player_score, (10, 10))

    # Draw ball

    # draw_snake()
    player1.draw()
    player2.draw()
    # Draw players

    pygame.draw.rect(screen, WHITE, ((treat['x'], treat['y']),
                     (SQUARE_SIDE, SQUARE_SIDE)))

    # if game_over:
    #     game_over_score = font.render('Game Over', True, BLUE)
    #     screen.blit(game_over_score, ((WIDTH // 2) - 275, (HEIGHT // 2) - 200))

    pygame.display.update()
    clock.tick(15)


# def check_game_over():
#     return (player['score']['value'] == SCORE_LIMIT or
            # opponent['score']['value'] == SCORE_LIMIT)

# Setup game before loop starts

init()

# render()
# Start game loop
x = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                paused = not paused

    # if not paused and not game_over:
    #     game_over = check_game_over()
    #     if not game_over:
    # print('update '+str(x))
    update(pygame.key.get_pressed(),treat)
    pygame.event.pump()
    # print('render ' + str(x))
    render()
    # x+=1



