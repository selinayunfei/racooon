import pygame

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_RETURN,
    K_SPACE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def text_box(text):
    box = pygame.sprite.Sprite()
    box.image = pygame.image.load("box.png")
    box.rect = box.image.get_rect(center = (640,620))
    return box

def box_update(box, delete):
    if delete:
        box.rect.y = -2000

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill((0,0,0))
bg = pygame.image.load("images.jpeg").convert_alpha()

textBox = text_box("hi")
all_sprites = pygame.sprite.Group()
all_sprites.add(textBox)
all_sprites.draw(screen)
running = True
while running:
    for event in pygame.event.get(): # every user input --> an event. This gets each of the events in a list.
        if event.type == KEYDOWN:
            # Check if the user clicked the escape key
            if event.key == K_ESCAPE:
                running = False
        #  Did the user click the window close button?
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    box_update(textBox, pressed_keys[K_RETURN])
    all_sprites.draw(screen)
    pygame.display.update()
    screen.blit(bg, (0, 0))
pygame.quit()