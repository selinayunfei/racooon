import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def create_text_box(text):
    box = pygame.sprite.Sprite()
    box.image = pygame.image.load("box.png").convert_alpha()
    box.rect = box.image.get_rect(center=(640, 620))
    box.text = text
    return box


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('comicsansms', 20)

start = True
running = True

def ending(end): 
    level = end
    while running:
        if start:
            current_dialogue = 0
            current_line = 0
            if level == "WeddingH":
                bg = pygame.image.load("EweddingH.png")
                dialogue = ["There's no one here...", "He abandoned you because of your gold digging!", "Yikes!", "You're free, but really poor :(", "Go find a job, buddy."]
            elif level == "WeddingB":
                bg = pygame.image.load("EweddingB.png")
                dialogue = ["Your future husband is waiting for you.", "He thinks you like him for his personality (you don't)", "He thinks you don't care about money (you really do)","You live miserably for like a few years", "then you die lol", "better luck next time!"]
            text_box = create_text_box(dialogue[current_dialogue])
            all_sprites.add(text_box)
            start = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_RETURN:
                    if current_dialogue < len(dialogue) - 1:
                        current_dialogue += 1
                    else:
                        if level[-1] == 'H':
                            start = True
                        else:
                            running = False
        screen.blit(bg, (0,0))
        all_sprites.draw(screen)
        all_sprites.remove(text_box)
        text_box.kill()
        text_box = create_text_box(dialogue[current_dialogue])
        all_sprites.add(text_box)
        if text_box.alive():
            text_surface = font.render(text_box.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(640, 620))
            screen.blit(text_surface, text_rect)
        pygame.display.update()

ending("WeddingH")
pygame.quit()