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
        pygame.draw.rect(window, self.color, self.area)


class Coin():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.color = "yellow"
        self.is_visible = True

    def draw_coin(self):
        if self.is_visible == True:
            pygame.draw.circle(window, self.color, (self.x, self.y), self.r)


class Character():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load("foxy.png")
        self.graphics = pygame.transform.scale(self.graphics, (60, 60))

    def draw_character(self):
        window.blit(self.graphics, (self.x, self.y))

    def move_left(self):
        self.x = self.x - 5
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_right(self):
        self.x = self.x + 5
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_down(self):
        self.y = self.y + 5
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_up(self):
        self.y = self.y - 5
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)


player = Character(50, 150, 60, 60)

platforms = []

for i in range(0, 14):
    platforms.append(Platform(random.randint(20, 500), random.randint(20, 500),
                              random.randint(70, 100), random.randint(15, 30)))  # so basically, winning the game
    # depends on your luck (how the platforms generate)... so, good luck XD (I'll change this, no worries)

platforms.append(Platform(0, 570, width, 30))

coins = []

for i in range(0, 3):
    coins.append(Coin(random.randint(60, 450), random.randint(60, 450), 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for p in platforms:
        p.draw_platform()

    for c in coins:
        c.draw_coin()

    player.draw_character()

    pygame.display.update()
