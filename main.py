import pygame
import random

pygame.init()

width = 600
height = 600

window = pygame.display.set_mode((width, height))


class Platform():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.area = pygame.Rect(self.x, self.y, self.width, self. height)

    def draw_platform(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            pygame.draw.rect(window, self.color, self.area)


class Coin():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.color = "yellow"
        self.is_visible = True


platforms = []


for i in range(0, 14):
    platforms.append(Platform(random.randint(20, 500), random.randint(20, 500),
                              random.randint(70, 100), random.randint(15, 30)))  # so basically, winning the game
    # depends on your luck (how the platforms generate)... so, good luck XD (I'll change this, no worries)

platforms.append(Platform(0, 570, width, 30))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for p in platforms:
        p.draw_platform()

    pygame.display.update()
