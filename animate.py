import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def create_raccoon():
    raccoon = pygame.sprite.Sprite()
    raccoon.image = pygame.image.load("richguy_default_smirk.png").convert_alpha()
    raccoon.image = pygame.transform.scale(raccoon.image, (1280, 720))
    raccoon.rect = raccoon.image.get_rect(center = (640, 360))
    raccoon.speed = 1
    return raccoon

def update_raccoon(raccoon):
    raccoon.rect.move_ip(0,raccoon.speed)
    if raccoon.rect.centery <= 340 or raccoon.rect.centery >= 380:
        raccoon.speed = -raccoon.speed

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
bg = pygame.image.load("wp5641813.webp")
raccoon = create_raccoon()
all_sprites = pygame.sprite.Group()
all_sprites.add(raccoon)

running = True
frame = 0
while running:
    frame += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    if frame % 20 == 0:
        update_raccoon(raccoon)
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    pygame.display.update()
