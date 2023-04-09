import pygame

BLUE = (200,255,255)

width = 900
height = 700
win = pygame.display.set_mode((width, height))
win.fill(BLUE)
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_width, player_heigth, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_heigth))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
	# Метод перерисовки персонажа
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, sprite):
        return self.rect.colliderect(sprite)

class Player(GameSprite):
    def update_right(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.rect.y < height - self.rect.height:
            self.rect.y += self.speed 

    def update_left(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_s] and self.rect.y < height - self.rect.height:
            self.rect.y += self.speed 

right_player = Player("platform.png", 880, 300, 15, 100, 3)
left_player = Player("platform.png", 5, 300, 15, 100, 3)
ball = GameSprite("ball.png", 0, 0, 100, 100, 3)

Vx = ball.speed
Vy = ball.speed

game = True
while game:
    win.fill(BLUE)
    right_player.reset()
    right_player.update_right()

    left_player.update_left()
    left_player.reset()

    ball.rect.x += Vx
    ball.rect.y += Vy

    if ball.rect.y < 0 or ball.rect.y > 600:
        Vy *= -1

    if ball.colliderect(left_player.rect) or ball.colliderect(right_player.rect):
        Vx *= -1
    
    ball.reset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False    

    pygame.display.update()
    clock.tick(40)