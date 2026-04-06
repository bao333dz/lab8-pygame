import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,600))
screen_rect = screen.get_rect()
pygame.display.set_caption("10 Moving Squares")
clock = pygame.time.Clock()

cat_load = pygame.image.load("graphics/cat.png").convert_alpha()
cat_load = pygame.transform.scale(cat_load, (50,50))

cat_list = []
for i in range (10):
    cat_rect = cat_load.get_rect(topleft = (i * 100, i * 61))
    cat_list.append(cat_rect)

cat_speed = [4] * 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("Black")

    for i, cat_rect in enumerate(cat_list):
        cat_rect.x += cat_speed[i]
        
        if cat_rect.left <= 0:
            cat_speed[i] = 4
        if cat_rect.right >= 1200:
            cat_speed[i] = -4

    for cat_rect in cat_list:
        screen.blit(cat_load, cat_rect)

    pygame.display.update()

    clock.tick(60)