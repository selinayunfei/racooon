import pygame
from pygame.locals import *
pygame.init()

def theEnd():
    credits1 = pygame.image.load("credits 1.png")
    credits2 = pygame.image.load("credits 2.png")
    creditsList = [credits1, credits2]
    creditsRect = credits1.get_rect(center = (640, 360))
    running = True
    while running:
        screen.blit(creditsList[0], creditsRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_RETURN:
                    creditsList.append(creditsList[0])
                    creditsList.pop(0)
        pygame.display.update()
    



SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
frame = 0
running = True
frame = 0
while running:
    frame += 1
    if frame == 200:
        running = False
    pygame.display.update()

theEnd()
pygame.quit()
