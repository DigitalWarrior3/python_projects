from pygame import  mixer
import pygame as pg
import random, time, math, sys

pg.init()
pg.mixer.init()

def game():

    #Screen
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    #Title and icon
    pg.display.set_caption("Game")
    background = pg.image.load('Gui/background.png').convert_alpha()
    iconImg = pg.image.load('Gui/controller.png').convert_alpha()
    pg.display.set_icon(iconImg)

    Gui_bar = pg.image.load('Gui/Gui_bar.png')

    class Player(pg.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.health = 3
            self.max_health = 3
            self.velocity = 8
            self.image = pg.image.load('images/rocket.png')
            self.rect = self.image.get_rect()
            self.rect.x = 376
            self.rect.y = 486
            self.freezing = False
    
        def move_right(self):
            self.rect.x += self.velocity
    
        def move_left(self):
            self.rect.x -= self.velocity
    
    def isCollision(pixel, asteroidX, asteroidY, playerX, playerY):
        distance = math.sqrt((math.pow(asteroidX - playerX, 2)) + (math.pow(asteroidY -playerY,2)))
        if distance < pixel:
            return True
        else:
            return False

    explosion = pg.image.load('images/explosion.png')

    class Asteroid(pg.sprite.Sprite):
        def __init__(self, image, velocity):
            super().__init__()
            self.velocity = velocity
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(7, 716)
            self.rect.y = random.randint(-800, 8)
            self.origin_image = self.image
            self.angle = 0
            self.collision = False 
    
        def fall(self):
            self.rect.y += self.velocity
        
        def rotate(self, angle):
            self.angle += angle
            self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
        
        def check_collision(self):
            if isCollision(50, self.rect.x, self.rect.y, player.rect.x, player.rect.y):
                self.collision = True
        
        def update_position(self):
            if self.rect.y >= 864 and game_over == False:
                self.rect.x = random.randint(7, 716)
                self.rect.y = random.randint(-800, 8)

    asteroid_img_01 = pg.image.load('images/asteroid_01.png').convert_alpha()
    asteroid_img_02 = pg.image.load('images/asteroid_02.png').convert_alpha()
    asteroid_img_03 = pg.image.load('images/asteroid_03.png').convert_alpha()
    asteroid_img_04 = pg.image.load('images/asteroid_04.png').convert_alpha()

    player = Player()
    asteroid_01 = Asteroid(asteroid_img_01, 7)
    asteroid_02 = Asteroid(asteroid_img_01, 6)
    asteroid_03 = Asteroid(asteroid_img_02, 7)
    asteroid_04 = Asteroid(asteroid_img_04, 8)
    asteroid_05 = Asteroid(asteroid_img_03, 6)
    asteroid_06 = Asteroid(asteroid_img_03, 7)
    pressed = {}

    game_bar_1 = pg.image.load('Gui/game_bar_1.png')
    game_bar_2 = pg.image.load('Gui/game_bar_2.png')
    game_bar_3 = pg.image.load('Gui/game_bar_3.png')
    game_bar_empty = pg.image.load('Gui/game_bar_empty.png')
    game_bar_full = pg.image.load('Gui/game_bar_full.png')
    freezing_img = pg.image.load('Gui/freezing.png')
    not_freezing_img = pg.image.load('Gui/not_freezing.png')
    
    slow_motion_start_sound = pg.mixer.Sound('Audio/slow_motion_start.wav')
    slow_motion_end_sound = pg.mixer.Sound('Audio/slow_motion_end.wav')
    player_explosion_sound = pg.mixer.Sound('Audio/axiom-boom.wav')
    explosion_sound = pg.mixer.Sound('Audio/muffled-distant-explosion.wav')
    
    slow_motion_start_sound.set_volume(0.07)
    slow_motion_end_sound.set_volume(0.07)
    player_explosion_sound.set_volume(0.2)
    explosion_sound.set_volume(0.07)

    fire_img = pg.image.load('images/fire.png')
    fireX = 0
    fireY = 0

    explosion_time = 0

    game_over = False
    game_start = True 

    font_64 = pg.font.Font('sourcecodepro.ttf', 64)
    font_32 = pg.font.Font('sourcecodepro.ttf', 32)

    score = 0
    secondary_score = 0

    def show_score(score):
        over_text = font_32.render(f"Score : {score}", True, (255, 255, 255))
        screen.blit(over_text, (18, 22))

    def show_game_over_text():
        over_text = font_64.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (230, 280))
    
    def show_start_text():
        over_text = font_64.render("Press 'SPACE'", True, (255, 255, 255))
        screen.blit(over_text, (165, 250))

    freezing_recharge = 0
    freezing_consume = 0
    freezing_nbr_recharche = 4
    freezing_timer = 0

    #Game loop
    not_running = False
    running = True
    while running:  
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = not_running 
                pg.quit()
                sys.exit()
            
            if event.type == pg.KEYDOWN:
                pressed[event.key] = True

            elif event.type == pg.KEYUP:
                pressed[event.key] = False
        
        screen.blit(background, (0, 0))
        if game_start == False and game_over == False:
            screen.blit(fire_img, (fireX, fireY))
        screen.blit(player.image, player.rect)
        screen.blit(asteroid_01.image, asteroid_01.rect)
        screen.blit(asteroid_02.image, asteroid_02.rect)
        screen.blit(asteroid_03.image, asteroid_03.rect)
        screen.blit(asteroid_04.image, asteroid_04.rect)
        screen.blit(asteroid_05.image, asteroid_05.rect)
        screen.blit(asteroid_06.image, asteroid_06.rect)
        if game_over == True and explosion_time <= 20:
            explosion_time += 1
            screen.blit(explosion, (player.rect.x - 32, player.rect.y - 32))
        if game_over == True and explosion_time == 1:
            player_explosion_sound.play() 
        if freezing_nbr_recharche == 4:
            screen.blit(game_bar_full, (0, 0))
        if freezing_nbr_recharche == 3:
            screen.blit(game_bar_3, (0, 0))
        if freezing_nbr_recharche == 2:
            screen.blit(game_bar_2, (0, 0))
        if freezing_nbr_recharche == 1:
            screen.blit(game_bar_1, (0, 0))
        if freezing_nbr_recharche == 0:
            screen.blit(game_bar_empty, (0, 0))

        if game_start == False:
            asteroid_01.fall()
            asteroid_02.fall()
            asteroid_03.fall()
            asteroid_04.fall()
            asteroid_05.fall()
            asteroid_06.fall()

        asteroid_01.check_collision()
        asteroid_02.check_collision()
        asteroid_03.check_collision()
        asteroid_04.check_collision()
        asteroid_05.check_collision()
        asteroid_06.check_collision()
        
        asteroid_01.update_position()
        asteroid_02.update_position()
        asteroid_03.update_position()
        asteroid_04.update_position()
        asteroid_05.update_position()
        asteroid_06.update_position()
        show_score(score)

        if player.freezing == False:
            if freezing_nbr_recharche <= 4:
                freezing_recharge += 1
            screen.blit(not_freezing_img, (725, 10))
            player.velocity = 7
            asteroid_01.velocity = 7
            asteroid_02.velocity = 6
            asteroid_03.velocity = 7
            asteroid_04.velocity = 8
            asteroid_05.velocity = 6
            asteroid_06.velocity = 7
            asteroid_01.rotate(1)
            asteroid_02.rotate(-1.5)
            asteroid_03.rotate(1)
            asteroid_04.rotate(-2)
            asteroid_05.rotate(1.5)
            asteroid_06.rotate(-1)
            freezing_timer = 0

        if player.freezing == True:
            if freezing_nbr_recharche >= 0:
                freezing_consume += 1
            screen.blit(freezing_img, (725, 10))
            player.velocity = 2.5
            asteroid_01.velocity = 2.5
            asteroid_02.velocity = 2
            asteroid_03.velocity = 2.5
            asteroid_04.velocity = 3
            asteroid_05.velocity = 2
            asteroid_06.velocity = 2.5
            asteroid_01.rotate(0.5)
            asteroid_02.rotate(-1)
            asteroid_03.rotate(0.5)
            asteroid_04.rotate(-1.5)
            asteroid_05.rotate(1)
            asteroid_06.rotate(-0.5)
            freezing_timer += 1    

        if pressed.get(pg.K_RIGHT) and game_over == False:
            player.move_right()
        
        if pressed.get(pg.K_LEFT) and game_over == False:
            player.move_left()
        
        if pressed.get(pg.K_SPACE) and game_start == True:
            game_start = False
        
        if pressed.get(pg.K_DOWN) and game_over == False and freezing_nbr_recharche != 0:
            player.freezing = True
        else:
            player.freezing = False

        if player.rect.x >= 729:
            player.rect.x = 729
        
        if player.rect.x <= 7:
            player.rect.x = 7
        
        if asteroid_01.collision == True or asteroid_02.collision == True or asteroid_03.collision == True or asteroid_04.collision == True or asteroid_05.collision == True or asteroid_06.collision == True:
            game_over = True

        if explosion_time >= 20:
            player.rect.y = 1000
        
        if game_over == True:
            show_game_over_text()
        
        if game_start == True:
            show_start_text()
        
        if player.freezing == False:
            fireX = player.rect.x + 18
            fireY = random.randint(player.rect.y + 50, player.rect.y + 53)
        else:
            fireX = player.rect.x + 18
            fireY = player.rect.y + 50
        
        if game_over == False and game_start == False:
            secondary_score += 1
        if secondary_score >= 10 and player.freezing == False:
            secondary_score = 0
            score += 1
        if secondary_score >= 25 and player.freezing == True:
            secondary_score = 0
            score += 1

        if freezing_consume >= 80 and freezing_nbr_recharche >= 0:
            freezing_consume = 0
            freezing_nbr_recharche -= 1
        
        if freezing_recharge >= 1500 and freezing_nbr_recharche <= 4:   
            freezing_recharge = 0
            freezing_nbr_recharche += 1
        
        if freezing_nbr_recharche <= -1:
            freezing_nbr_recharche = 0
        if freezing_nbr_recharche >= 5:
            freezing_nbr_recharche = 4
        
        if freezing_timer == 1:
            slow_motion_start_sound.play()

        pg.display.flip()
        clock.tick(80) 

game()  