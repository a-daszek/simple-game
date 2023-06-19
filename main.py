import pygame
import random

pygame.init()

width = 900
height = 900

window = pygame.display.set_mode((width, height))


class Platform():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

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

    def check_picked(self, area):
        if area.collidepoint(self.x, self.y) == True:
            self.is_visible = False


class Character():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load("foxy.png")
        self.graphics = pygame.transform.scale(self.graphics, (70, 70))

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
        self.y = self.y - 10  # it can't be 5 because it will equilibrate with the down key
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)


player = Character(50, 150, 45, 45)

platforms = []

for i in range(0, 20):
    platforms.append(Platform(random.randint(20, 800), random.randint(20, 800),
                              random.randint(70, 100), random.randint(15, 30)))  # so basically, winning the game
    # depends on your luck (how the platforms generate)... so, good luck XD (I'll change this, no worries)

platforms.append(Platform(0, 870, width + 50, 30))

coins = []

for i in range(0, 4):
    coins.append(Coin(random.randint(60, 650), random.randint(60, 650), 20))

jump_range = 0
left_movement_active = False
right_movement_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_movement_active = True
            if event.key == pygame.K_RIGHT:
                right_movement_active = True
            if event.key == pygame.K_UP:
                jump_range = 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_movement_active = False
            if event.key == pygame.K_RIGHT:
                right_movement_active = False

    window.fill("black")

    if jump_range > 0:
        player.move_up()
        jump_range = jump_range - 1

    if left_movement_active == True:
        player.move_left()
    if right_movement_active == True:
        player.move_right()

    is_touching = False

    for p in platforms:
        p.draw_platform()
        if player.area.colliderect(p.area) == True:
            is_touching = True
    if is_touching == False:
        player.move_down()

    coins_available = False
    for c in coins:
        c.draw_coin()
        c.check_picked(player.area)
        if c.is_visible == True:
            coins_available = True

    if coins_available == False:
        font = pygame.font.SysFont("Helvetica", 25)
        font_image = font.render("Congratulations!", 1, "purple")
        window.blit(font_image, (300, 200))

    player.draw_character()
    pygame.time.wait(10)

    pygame.display.update()
