import pygame
import random
import button

pygame.init()

width = 900
height = 900

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumping fox!")


class Platform():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)
#  ----- Those two lines are optional - if you want to have platforms with grass (pixel art style) you can add them.  #
#  ----- The length of the platforms won't be diverse though------------  #
        # self.graphics = pygame.image.load("platform.png")
        # self.graphics = pygame.transform.scale(self.graphics, (140, 70))

    def draw_platform(self):
        pygame.draw.rect(window, self.color, self.area)

# ----- This function is for the platforms wItH gRaSssSss ----- #
    # def draw_platform(self):
    #     window.blit(self.graphics, (self.x, self.y))


class Coin():
    # -------- class for basic drawn coins -------- #
    # def __init__(self, x, y, r):
    #     self.x = x
    #     self.y = y
    #     self.r = r
    #     self.color = "yellow"
    #     self.is_visible = True
    # ---- and it's method ---- #
    # def draw_coin(self):
    #     if self.is_visible:
    #         pygame.draw.circle(window, self.color, (self.x, self.y), self.r)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.graphics = pygame.image.load("golden_blueberry.png")
        self.graphics = pygame.transform.scale(self.graphics, (60, 60))
        self.is_visible = True

    def draw_coin(self):
        if self.is_visible:
            window.blit(self.graphics, (self.x, self.y))

    def check_picked(self, area):
        if area.collidepoint(self.x, self.y):
            self.is_visible = False


class Character():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load("foxy.png")
        self.graphics = pygame.transform.scale(self.graphics, (90, 90))

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


player = Character(50, 150, 70, 70)

platforms = []

for i in range(0, 20):
    platforms.append(Platform(random.randint(20, 800), random.randint(20, 800),
                              random.randint(70, 100), random.randint(15, 30)))  # so basically, winning the game
    # depends on your luck (how the platforms generate)... so, good luck XD (I'll change this, probably)

platforms.append(Platform(0, 870, width + 50, 30))

coins = []

# ----- This for loop is for the basic drawn coins, where r parameter is required ---- #
# for i in range(0, 4):
#     coins.append(Coin(random.randint(60, 650), random.randint(60, 650), 20))

for i in range(0, 4):
    coins.append(Coin(random.randint(60, 650), random.randint(60, 650)))

jump_range = 0
left_movement_active = False
right_movement_active = False

font = pygame.font.SysFont("Calibre", 35)

TEXT_COL = (255, 255, 255)

resume_img = pygame.image.load("button_resume.png").convert_alpha()
resume_ib = pygame.transform.scale(resume_img, (300, 120))
quit_img = pygame.image.load("button_quit.png").convert_alpha()
quit_ib = pygame.transform.scale(quit_img, (220, 120))

# create button instances
resume_button = button.Button(300, 225, resume_ib, 1)
quit_button = button.Button(340, 445, quit_ib, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


# game variables

game_paused = False
menu_state = "main"
game_on = True

while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_movement_active = True
            if event.key == pygame.K_RIGHT:
                right_movement_active = True
            if event.key == pygame.K_UP:
                jump_range = 20
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_movement_active = False
            if event.key == pygame.K_RIGHT:
                right_movement_active = False

    window.fill("black")

    if jump_range > 0:
        player.move_up()
        jump_range = jump_range - 1

    if left_movement_active:
        player.move_left()
    if right_movement_active:
        player.move_right()

    is_touching = False

    for p in platforms:
        p.draw_platform()
        if player.area.colliderect(p.area):
            is_touching = True
    if not is_touching:
        player.move_down()

    coins_available = False
    for c in coins:
        c.draw_coin()
        c.check_picked(player.area)
        if c.is_visible:
            coins_available = True

    if game_paused:
        window.fill((22, 38, 91))
        jump_range = 0
        left_movement_active = False
        right_movement_active = False
        if menu_state == "main":
            # drawn - clicked
            if resume_button.draw(window):
                game_paused = False
            if quit_button.draw(window):
                game_on = False
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 10, 20)

    if not coins_available:
        # font = pygame.font.SysFont("Helvetica", 25)
        font_image = font.render("Congratulations!", True, "yellow")
        window.blit(font_image, (680, 20))

    player.draw_character()
    pygame.time.wait(10)

    pygame.display.update()

pygame.quit()
