import pygame
import time
import random

pygame.init()

# Colors
green = (0, 128, 0)
red = (213, 50, 80)
white = (255, 255, 255)

# Display configurations
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 20

font_style = pygame.font.SysFont(None, 50)

bg_img = pygame.image.load('background.png')
food_img = pygame.image.load('food.png')
food_img = pygame.transform.scale(food_img, (snake_block + 5, snake_block + 5))


def message(msg, text_color, bg_color):
    mesg = font_style.render(msg, True, text_color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
    pygame.display.update()


def snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(dis, white, [segment[0], segment[1], snake_block, snake_block])


def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])


def gameLoop():
    global snake_speed  # Declare snake_speed as global

    snake_speed = 10  # Initial snake speed
    speed_increment = 0  # Speed increment when snake eats food

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    score = 0

    last_key_pressed = None  # Store the last key pressed

    while not game_over:
        while game_close:
            dis.fill(green)
            message("You Lost! Press Q-Quit or C-Play Again", white, green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_key_pressed != pygame.K_RIGHT:  # Check for opposite direction
                    x1_change = -snake_block
                    y1_change = 0
                    last_key_pressed = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and last_key_pressed != pygame.K_LEFT:
                    x1_change = snake_block
                    y1_change = 0
                    last_key_pressed = pygame.K_RIGHT
                elif event.key == pygame.K_UP and last_key_pressed != pygame.K_DOWN:
                    y1_change = -snake_block
                    x1_change = 0
                    last_key_pressed = pygame.K_UP
                elif event.key == pygame.K_DOWN and last_key_pressed != pygame.K_UP:
                    y1_change = snake_block
                    x1_change = 0
                    last_key_pressed = pygame.K_DOWN

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(bg_img, (0, 0))
        dis.blit(food_img, (foodx, foody))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
 

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            score += 1
            # Increase snake speed when it eats food
            snake_speed += speed_increment
            

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
