import pygame
pygame.init()
display = pygame.display.set_mode((400,400))
pygame.display.update()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        print(event)




pygame.quit()
quit()