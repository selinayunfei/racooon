import pygame
from pygame.locals import *
import math

pygame.init()

def walking_animation(png):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    
    end = False
    
    door_opening = pygame.mixer.Sound("door.mp3")
    walking = pygame.mixer.Sound("walking.mp3")

    door_opening.play()
    pygame.time.set_timer(USEREVENT + 1, 1000)
    pygame.time.set_timer(USEREVENT + 2, 10000)

    def create_raccoon():
        raccoon = pygame.sprite.Sprite()
        raccoon.original_image = pygame.image.load(png).convert_alpha()
        raccoon.image = raccoon.original_image
        raccoon.rect = raccoon.image.get_rect(center=(0, 0))  # Start from top-left corner
        raccoon.speed_x = 2   # Horizontal speed
        raccoon.speed_y = 1   # Vertical speed
        raccoon.angle = 0
        return raccoon

    def update_raccoon(raccoon, frame):
        # Move diagonally
        raccoon.rect.x += raccoon.speed_x
        raccoon.rect.y += raccoon.speed_y

        # Waddle animation using sin wave
        raccoon.angle = 10 * math.sin(frame / 10)
        rotated_image = pygame.transform.rotate(raccoon.original_image, raccoon.angle)
        old_center = raccoon.rect.center
        raccoon.image = rotated_image
        raccoon.rect = raccoon.image.get_rect(center=old_center)


    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    bg = pygame.image.load("bg 2 - Tim Hortons, entrance.png")
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    raccoon = create_raccoon()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(raccoon)

    clock = pygame.time.Clock()
    running = True
    frame = 0
    walking_started = False

    while running:
        frame += 1
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
            elif event.type == USEREVENT + 1 and not walking_started:
                walking.play(loops = 1)
                walking_started = True
            elif event.type == USEREVENT + 2:
                return

        update_raccoon(raccoon, frame)

        screen.blit(bg, (0, 0))
        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)  # Limit frame rate
        
walking_animation("good_rich_guy_fat_chibi.png")
