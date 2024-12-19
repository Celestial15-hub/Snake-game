import pygame
import sys 
import random


screen_width = 640
screen_height = 480
background_colour = (0, 255, 0)
snake_colour = (255, 0, 0)
food_colour = (255, 0, 0)

snake_size = 10
snake_speed = 15
starting_position = 100
starting_length = 7


food_size = 15
spawn_rate = 7
score = 0

score_increment = 3
game_over_conditions = ("snake hits wall ", " snake bites itself, ")

font = "Arial black "
font_size = 40
pygame.init()
screen = pygame.display.set_mode(640, 480)
clock = pygame.time.clock()

font = pygame.font.FONT(None, 36)
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_up and snake[0][1] >0:
                snake.insert(0, (snake[0][0], snake[0][1] - snake_size))
            elif event.key == pygame.K_DOWN and snake[0][1] < screen_height - snake_size:
                snake.insert(0, (snake[0][0], snake[0][1] + snake_size))
            elif event.key == pygame.K_LEFT and snake[0][0] > 0:
                snake.insert(0, snake[0][0] - snake_size, snake[0][1])
            elif event.key == pygame.K_RIGHT and snake[0][0] and snake[0][1] < screen_width - snake_size:
                snake.insert(0, (snake[0][0] - snake_size, snake[0][1]))
                
    if snake[0] == food:
        score += 1
        food = (random.randint(0, screen_width - food_size)) // food_size * food_size, random.randint(0, screen_height - food_size) // food_size * food_size
    else:
        snake.pop()

    if snake [0][0] < 0 or snake[0][0] >= screen_width or snake [0][1] < 0 or snake [0][1] >= screen_height or snake[0] in snake [1]:
        print("Game Over! Final Score: ", score)

    pygame.quit()
    sys.exit()
    screen.fill(background_color) for x,y in snake:
    pygame.draw. 
    
