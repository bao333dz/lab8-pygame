import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,600))
screen_rect = screen.get_rect()
pygame.display.set_caption("10 Moving Squares")
clock = pygame.time.Clock()

cat_original = pygame.image.load("graphics/cat.png").convert_alpha()

cat_list = []
cat_images = []
for i in range (10):
    random_size = random.randint(30, 70)
    cat_scaled = pygame.transform.scale(cat_original, (random_size, random_size))
    cat_images.append(cat_scaled)
    
    random_x = random.randint(0, 1150)
    random_y = random.randint(0, 550)
    cat_rect = cat_scaled.get_rect(topleft = (random_x, random_y))
    cat_list.append(cat_rect)

cat_speed_x = [random.choice([4, -4]) for i in range(10)]
cat_speed_y = [random.choice([4, -4]) for i in range(10)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("Black")

    for i, cat_rect in enumerate(cat_list):
        cat_rect.x += cat_speed_x[i]
        cat_rect.y += cat_speed_y[i]
        
        # LEFT/RIGHT walls - reverse X speed
        if cat_rect.left <= 0:
            cat_speed_x[i] = 4
        if cat_rect.right >= 1200:
            cat_speed_x[i] = -4
        
        # TOP/BOTTOM walls - reverse Y speed
        if cat_rect.top <= 0:
            cat_speed_y[i] = 4
        if cat_rect.bottom >= 600:
            cat_speed_y[i] = -4

    for i, cat_rect in enumerate(cat_list):
        screen.blit(cat_images[i], cat_rect)

    pygame.display.update()

    clock.tick(60)