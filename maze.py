#создай игру "Лабиринт"!
from pygame import *

class Sprite_game(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite_game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 645:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
            
class Enemy(Sprite_game):
    def update(self, x_min, x_max):
        if self.rect.x <= x_min:
            self.direction = "right"
        if self.rect.x >= x_max:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
        
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def Draw_wall(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

win = display.set_mode((700, 500))
display.set_caption("Maze")
cvet = transform.scale(image.load("background.jpg"), (700, 500))

player = Player('hero.png', 5, 445, 2) #445 - это координата по y поэтому она не может быть больше чем 500
vrag1 = Enemy('cyborg.png', 645, 5, 3)
vrag2 = Enemy('cyborg.png', 645, 445, 1)
socrovisha = Sprite_game('treasure.png', 390, 370, 0)
stena1 = Wall(200, 150, 50, 60, 70, 10, 430)
stena2 = Wall(100, 150, 50, 540, 60, 10, 70)
stena3 = Wall(100, 150, 50, 60, 60, 400, 10)
stena4 = Wall(100, 150, 50, 140, 270, 120, 10)
stena5 = Wall(100, 150, 50, 70, 200, 120, 10)
stena6 = Wall(100, 150, 50, 140, 130, 555, 10)
stena7 = Wall(100, 150, 50, 70, 340, 120, 10)
stena8 = Wall(100, 150, 50, 140, 410, 120, 10)
stena9 = Wall(100, 150, 50, 540, 200, 10, 240)
stena10 = Wall(100, 150, 50, 260, 140, 10, 300)
stena11 = Wall(100, 150, 50, 340, 350, 290, 10)
stena12 = Wall(100, 150, 50, 270, 430, 180, 10)
stena13 = Wall(100, 150, 50, 450, 350, 10, 90)
stena14 = Wall(100, 150, 50, 430, 140, 10, 140)
stena15 = Wall(100, 150, 50, 340, 210, 10, 140)
stena16 = Wall(100, 150, 50, 640, 270, 55, 10)

run = True
pobeda = False
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 90)
viigrish = font.render('Ты победил!', True, (0, 200, 0))
proigrish = font.render('Ты проиграл!', True, (200, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

dengi = mixer.Sound('money.ogg')
udar = mixer.Sound('kick.ogg')

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if pobeda != True:
        win.blit(cvet, (0, 0))
        player.update()
        vrag1.update(350, 645)
        vrag2.update(260, 645)
        player.reset()
        vrag1.reset()
        vrag2.reset()
        socrovisha.reset()
        stena1.Draw_wall()
        stena2.Draw_wall()
        stena3.Draw_wall()
        stena4.Draw_wall()
        stena5.Draw_wall()
        stena6.Draw_wall()
        stena7.Draw_wall()
        stena8.Draw_wall()
        stena9.Draw_wall()
        stena10.Draw_wall()
        stena11.Draw_wall()
        stena12.Draw_wall()
        stena13.Draw_wall()
        stena14.Draw_wall()
        stena15.Draw_wall()
        stena16.Draw_wall()

        if sprite.collide_rect(player, vrag1) or sprite.collide_rect(player, vrag2) or sprite.collide_rect(player, stena1) or sprite.collide_rect(player, stena2) or sprite.collide_rect(player, stena3) or sprite.collide_rect(player, stena4) or sprite.collide_rect(player, stena5) or sprite.collide_rect(player, stena6) or sprite.collide_rect(player, stena7) or sprite.collide_rect(player, stena8) or sprite.collide_rect(player, stena9) or sprite.collide_rect(player, stena10) or sprite.collide_rect(player, stena11) or sprite.collide_rect(player, stena12) or sprite.collide_rect(player, stena13) or sprite.collide_rect(player, stena14) or sprite.collide_rect(player, stena15) or sprite.collide_rect(player, stena16):
            pobeda = True
            win.blit(proigrish, (100, 200))
            udar.play()
        if  sprite.collide_rect(player, socrovisha):
            pobeda = True
            win.blit(viigrish, (150, 200))
            dengi.play()

    display.update()
    clock.tick(FPS)