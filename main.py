import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def text_box(text):
    box = pygame.sprite.Sprite()
    box.image = pygame.image.load("box.png")
    box.rect = box.image.get_rect(center=(640, 620))
    box.list = text
    box.text_index = 0
    box.text = box.list[box.text_index]
    return box

def box_update(box, all_sprites):
    if box.text_index < len(box.list) - 1:
        box.text_index += 1
        box.text = box.list[box.text_index]
    else:
        all_sprites.remove(box)
        box.kill()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
bg = pygame.image.load("wp5641813.webp").convert_alpha()

textBox = text_box(["hi", "bye", "i hate you"])
all_sprites = pygame.sprite.Group()
all_sprites.add(textBox)

font = pygame.font.Font('comicsansms', 25)
enter = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN and not enter:
                enter = True
                box_update(textBox, all_sprites)

        elif event.type == KEYUP:
            if event.key == K_RETURN:
                enter = False

    screen.blit(bg, (0, 0))

    all_sprites.draw(screen)

    if textBox.alive():  # only draw text if the box still exists
        textRend = font.render(textBox.text, True, (0, 0, 0))
        textRect = textRend.get_rect(center=(640, 600))  # slightly above center to avoid overlap
        screen.blit(textRend, textRect)

    pygame.display.update()

pygame.quit()
