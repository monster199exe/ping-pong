from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,image1,speed,x,y,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(image1),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < window_width-80:
            self.rect.x += self.speed
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.x < window_width-80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',-10,self.rect.centerx,self.rect.top,15,20)
        bullets.add(bullet)

back = (200,255,255)
window_width = 600
window_hight = 500
window = display.set_mode((window_width,window_hight))
window.fill(back)
clock = time.Clock()
FPS = 60
ball = GameSprite('tenis_ball.png',4,200,200,50,50)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.reset()
    display.update()
    clock.tick(FPS)
