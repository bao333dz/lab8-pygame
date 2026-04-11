import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,600))
screen_rect = screen.get_rect()
pygame.display.set_caption("10 Moving Squares")
clock = pygame.time.Clock()

#Load the image
cat_original = pygame.image.load("graphics/cat.png").convert_alpha()

# Generate sizes and positions
cat_data = []
for i in range(10):
    random_size = random.randint(30, 70)
    random_x = random.randint(0, 1150)
    random_y = random.randint(0, 550)
    cat_data.append((random_size, random_x, random_y))

# Sort by size (smallest to biggest)
cat_data.sort(key=lambda x: x[0])

cat_list = []
cat_images = []
speeds = []

for i, (size, pos_x, pos_y) in enumerate(cat_data):
    # Scale the image
    cat_scaled = pygame.transform.scale(cat_original, (size, size))
    cat_images.append(cat_scaled)
    
    # Create rect
    cat_rect = cat_scaled.get_rect(topleft=(pos_x, pos_y))
    cat_list.append(cat_rect)
    
    # Assign speed inversely to size (small = fast, big = slow)
    # Size 30 -> speed 300 px/s, Size 70 -> speed 60 px/s
    speed = int((5 - (size - 30) / 10) * 60)
    speeds.append(speed)

# Randomly assign directions (multiply by 1 or -1)
cat_speed_x = [speed * random.choice([1, -1]) for speed in speeds]
cat_speed_y = [speed * random.choice([1, -1]) for speed in speeds]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Calculate delta time (frame time in seconds)
    dt_ms = clock.tick(60)
    delta_time = dt_ms / 1000

    screen.fill("Black")

    #
    for i, cat_rect in enumerate(cat_list):
        cat_rect.x += cat_speed_x[i] * delta_time
        cat_rect.y += cat_speed_y[i] * delta_time
        
        # LEFT/RIGHT walls - reverse X speed
        if cat_rect.left <= 0:
            cat_speed_x[i] = -cat_speed_x[i]
        if cat_rect.right >= 1200:
            cat_speed_x[i] = -cat_speed_x[i]
        
        # TOP/BOTTOM walls - reverse Y speed
        if cat_rect.top <= 0:
            cat_speed_y[i] = -cat_speed_y[i]
        if cat_rect.bottom >= 600:
            cat_speed_y[i] = -cat_speed_y[i]

    for i, cat_rect in enumerate(cat_list):
        screen.blit(cat_images[i], cat_rect)

    pygame.display.update()