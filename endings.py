import pygame
from pygame.locals import *

pygame.init()



def ending(end):
    def create_text_box(text, end):
        box = pygame.sprite.Sprite()
        box.image = pygame.image.load("box.png").convert_alpha()
        if end == "TVG" or end == "TVB":
            box.rect = box.image.get_rect(center=(640, 100))
        else:
            box.rect = box.image.get_rect(center=(640, 620))
        box.text = text
        return box
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    frame = 0
    all_sprites = pygame.sprite.Group()
    font = pygame.font.SysFont('comicsansms', 20)
    running = True
    start = True
    while running:
        if start:
            current_dialogue = 0
            current_line = 0
            if end == "WeddingH":
                bg = pygame.image.load("EweddingH.png")
                dialogue = ["There's no one here...", "He abandoned you because of your gold digging!", "Yikes!", "You're free, but really poor :(", "Go find a job, buddy."]
            elif end == "WeddingB":
                bg = pygame.image.load("EweddingB.png")
                dialogue = ["Your future husband is waiting for you.", "He thinks you like him for his personality (you don't)", "He thinks you don't care about money (you really do)","You live miserably for like a few years", "then you die lol", "better luck next time!"]
            elif end == "TVG":
                bg = pygame.image.load("TVG.png")
                dialogue = ["...who the hell is that on TV???", "oh my god its that really weird guy","i guess he's famous???", "did he just publically doxx you.","his fans are gonna murder you oh my god","at least he hates you so you don't have to date him","good job ig??? watch out for the crazy fans"]
            elif end == "TVB":
                bg = pygame.image.load("TVB.png")
                dialogue = ["...who the hell is that on TV???", "oh my god it's that really weird guy", "he's famous?!?!?!?!?!","DID HE","DID HE JUST PROFESS HIS UNDYING LOVE","ON LIVE TV???? TO YOU???","W H A T T H E F L I P","YOU DON'T EVEN LIKE HIM","the door opens.","you're so screwed.","better luck next time!","i'm so sorryfor this (no)"]
            elif end == "THG":
                bg = pygame.image.load("THG.png")
                dialogue = ["You're here.","...He's not coming is he lol","yeah uh you wouldn't come back either","after how rude you were yesterday","poor dude","is not having to deal with him a L or a W though","depends on what you read ig","good job (?) you made it past all 3","you get to keep single pringle status","should we clap?","do you really hate raccoons that much???","welp","go enjoy your ending animation"]
            elif end == "THB":
                bg = pygame.image.load("THB.png")
                dialogue = ["Oh my god he's already here","How long has he been here???","You'd call him a good boy but i've made you put up with enough","sorry (not)","he looks so eager lol","you had to give in at some point hmmm","...(furry?)","SORRY","YKW ITS VALID OF YOU","enjoy your marriage","although you did lose L","bye IG"]
            text_box = create_text_box(dialogue[current_dialogue], end)
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
                        if end[-1] == 'H':
                            start = True
                        else:
                            running = False
        screen.blit(bg, (0,0))
        all_sprites.draw(screen)
        all_sprites.remove(text_box)
        text_box.kill()
        text_box = create_text_box(dialogue[current_dialogue], end)
        all_sprites.add(text_box)
        if text_box.alive():
            text_surface = font.render(text_box.text, True, (0, 0, 0))
            if end == "TVG" or end == "TVB":
                text_rect = text_surface.get_rect(center=(640, 100))
            else:
                text_rect = text_surface.get_rect(center=(640, 620))
            screen.blit(text_surface, text_rect)
        pygame.display.update()

ending("THB")
pygame.quit()