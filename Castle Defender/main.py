import pygame, random, sys
pygame.init()

# create window
screen = pygame.display.set_mode((800, 600))
title = "Castle Defender"
background = pygame.image.load('gui/background.png').convert_alpha()
pygame.display.set_caption(title)
icon = pygame.image.load('gui/controller.png').convert_alpha()
gui_bar = pygame.image.load('gui/gui_bar.png').convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

gui_heart = pygame.image.load('gui/heart.png').convert_alpha()
gui_coin = pygame.image.load('gui/coin.png').convert_alpha()
font_64 = pygame.font.Font('sourcecodepro.ttf', 64)
font_32 = pygame.font.Font('sourcecodepro.ttf', 32)
font_40 = pygame.font.Font('sourcecodepro.ttf', 40)

white = (255, 255, 255)
black = (0, 0, 0)


def show_text(font_size, color, text, x, y):
    font = pygame.font.Font('sourcecodepro.ttf', font_size)
    over_text = font.render(text, True, color)
    screen.blit(over_text, (x, y))


game_over = False
game_paused = False

class Castle:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/castle.png')
        self.rect = self.image.get_rect()
        self.rect.x = 660
        self.rect.y = 315
        self.max_hp = 9
        self.hp = self.max_hp
        self.hp_timer = 0
        self.destroyed = False
        self.coins = 0

    def check_castle_state(self):
        if self.hp == 0:
            self.destroyed = True

    def check_collision(self):
        pass

    def print_coins(self):
        if self.coins > 9:
            show_text(36, white, str(self.coins), 102, 20)
        else:
            show_text(36, white, str(self.coins), 114, 20)

    def print_hearts(self):
        show_text(36, white, str(self.hp), 34, 20)


class Cloud:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/cloud.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-1080, -80)
        self.rect.y = random.randint(50, 80)
        self.velocity = 1

    def update_pos(self):
        self.rect.x += self.velocity
        if self.rect.x >= 880:
            self.rect.x = -80
            self.rect.y = random.randint(50, 80)


# castle
castle = Castle()
# clouds
cloud_01 = Cloud()
cloud_02 = Cloud()
cloud_03 = Cloud()

run = True
# game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    

    if game_paused == False:
        # castle
        castle.check_castle_state()
        castle.check_collision()
        # clouds
        cloud_01.update_pos()
        cloud_02.update_pos()
        cloud_03.update_pos()

    screen.blit(background, (0, 0))
    screen.blit(castle.image, castle.rect)
    screen.blit(cloud_01.image, cloud_01.rect)
    screen.blit(cloud_02.image, cloud_02.rect)
    screen.blit(cloud_03.image, cloud_03.rect)
    screen.blit(gui_bar, (0, 0))
    screen.blit(gui_coin, (93, 13))
    screen.blit(gui_heart, (13, 13))
    castle.print_hearts()
    castle.print_coins()
    pygame.display.update()
    clock.tick(120)
