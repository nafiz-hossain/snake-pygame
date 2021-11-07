import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display configurations
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 15  # Reduce the size of the snake block
snake_speed = 20

font_style = pygame.font.SysFont(None, 50)

bg_img = pygame.image.load('background.png')
food_img = pygame.image.load('food.png')

# Set size of food image (bigger)
food_img = pygame.transform.scale(food_img, (snake_block * 3, snake_block * 3))

# Define padding
padding = 50  # Adjust this value as needed

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(dis, green, [segment[0], segment[1], snake_block, snake_block])

def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(padding, dis_width - padding - snake_block) / 15.0) * 15.0
    foody = round(random.randrange(padding, dis_height - padding - snake_block) / 15.0) * 15.0

    score = 0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
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
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0


        # Boundary collision detection
        if x1 >= dis_width - snake_block:
            print("Right Boundary Collision Detected:", x1, y1)
            game_close = True
        elif x1 < padding:
            print("Left Boundary Collision Detected:", x1, y1)
            game_close = True
        elif y1 >= dis_height - snake_block:
            print("Bottom Boundary Collision Detected:", x1, y1)
            game_close = True
        elif y1 < padding:
            print("Top Boundary Collision Detected:", x1, y1)
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
        for segment in snake_list[:-1]:
            if segment[0] == x1 and segment[1] == y1:
                print("Self-Collision Detected")
                game_close = True
                break

        snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake's head touches the food
        if foodx - snake_block <= x1 <= foodx + snake_block and foody - snake_block <= y1 <= foody + snake_block:
            foodx = round(random.randrange(padding, dis_width - padding - snake_block) / 15.0) * 15.0
            foody = round(random.randrange(padding, dis_height - padding - snake_block) / 15.0) * 15.0
            length_of_snake += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
