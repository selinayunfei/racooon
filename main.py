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
bg = pygame.image.load("wp5641813.webp")

all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('comicsansms', 20)

# Game state
level = "richguy"

newChoice = True
running = True
start = True
while running:
    if start:
        current_dialogue = 0
        current_line = 0
        if level == "richguy":
            dialogue = [
                ["*walks in*", "hey babygirl, how you doing?"]
            ]
            all_dialogue = {1:["omg, i can fix that *smirks*. let me get you something to eat. ","that's great, bbg. what do you want to eat?","yeah... i guess. is there anything you want to eat, though?"], 2:["haha you're funny! you're right, i'm nothing but a humble raccoon... would you like one of my banana peels then? i saved it just for u","are you sure you'd want that, bbg? i have a banana peel saved for you","are you serious??? why do you care so much about luxury? i saved a banana peel for you."], 3:["we should get married.","sigh. not your taste? how's an apple core for you.","calm yourself. have an apple core."],4:["that's great! the wedding's tomorrow. i'll see you there *mews*","fine. yes i'm rich. wedding's tomorrow. be there and i'll give you my inheritance. "]}
            choices = [
                ["1. terrible, and you?", "2. ...good", "3. oh my god is that a rolex?"],
                ["1. that trash bin over there. isn't that your house?","2. what's the most expensive here?","3. why are we at timmy's. aren't you rich?"],
                ["1. ... you're weird. but thank you though, i'm starving. ","2. ew.....","3. BRUH I KNOWWWWW YOU HAVE A LAMBO IN THAT DANG PARKING LOT I WANT A FIVE STAR MICHELIN MEAL"],
                [["1. i mean. like sure ? i'm lowkey desperate.","2. AH HELL NAH", "3. yeah? do i get your mansion then?"],["1. bruh. i guess this is all you have. thanks i guess.","2. you're not actually rich, are you? wtf","3. like the core of an apple iphone? i knew it! you're like rich!"],["1. you're not actually rich, are you? wtf","2. like the core of an apple iphone? i knew it! you're like rich!","3. calm YOURself. give me your credit card info."]]
            ]
        text_box = create_text_box(dialogue[current_dialogue][current_line])
        all_sprites.add(text_box)
        start = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN:
                # Advance to next line
                if current_line < len(dialogue[current_dialogue]) - 1:
                    current_line += 1
                    all_sprites.remove(text_box)
                    text_box = create_text_box(dialogue[current_dialogue][current_line])
                    all_sprites.add(text_box)
                else:
                    # Dialogue complete, show choices
                    pass
    pressed_keys = pygame.key.get_pressed()
    # Draw everything
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    
    # Render the current text
    if text_box.alive():
        text_surface = font.render(text_box.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(640, 620))
        screen.blit(text_surface, text_rect)
    # Render choices if at the end of dialogue
    if current_line == len(dialogue[current_dialogue]) - 1:
        choice_height = 350
        if current_dialogue < 4:
            if current_dialogue < 3:
                for choice in choices[current_dialogue]:
                    choice_surface = font.render(choice, True, (0, 0, 0))
                    choice_rect = choice_surface.get_rect(center=(1000, choice_height))
                    screen.blit(choice_surface, choice_rect)
                    choice_height += 40
                    if (pressed_keys[K_1] or pressed_keys[K_2] or pressed_keys[K_3]) and newChoice:
                        newChoice = False
                        current_dialogue += 1
                        if pressed_keys[K_1]:
                            currentChoice = 0
                            dialogue.append([all_dialogue[current_dialogue][0]])
                        elif pressed_keys[K_2]:
                            currentChoice = 1
                            dialogue.append([all_dialogue[current_dialogue][1]])
                        elif pressed_keys[K_3]:
                            currentChoice = 2
                            dialogue.append([all_dialogue[current_dialogue][2]])
                        current_line = 0
                        all_sprites.remove(text_box)
                        text_box.kill()
                        text_box = create_text_box(dialogue[current_dialogue][current_line])
                        all_sprites.add(text_box)
            elif current_dialogue == 3:
                for choice in choices[current_dialogue][currentChoice]:
                    choice_surface = font.render(choice, True, (0, 0, 0))
                    choice_rect = choice_surface.get_rect(center=(1000, choice_height))
                    screen.blit(choice_surface, choice_rect)
                    choice_height += 40
                    if (pressed_keys[K_1] or pressed_keys[K_2] or pressed_keys[K_3]) and newChoice:
                        newChoice = False
                        current_dialogue += 1
                        if level == "richguy":
                            if currentChoice == 0:
                                if pressed_keys[K_1]:
                                    dialogue.append([all_dialogue[current_dialogue][0]])
                                elif pressed_keys[K_2]:
                                    dialogue.append([all_dialogue[current_dialogue][0]])
                                elif pressed_keys[K_3]:
                                    dialogue.append([all_dialogue[current_dialogue][1]])
                            elif currentChoice == 1:
                                if pressed_keys[K_1]:
                                    dialogue.append([all_dialogue[current_dialogue][0]])
                                elif pressed_keys[K_2]:
                                    dialogue.append([all_dialogue[current_dialogue][1]])
                                elif pressed_keys[K_3]:
                                    dialogue.append([all_dialogue[current_dialogue][1]])
                            elif currentChoice == 2:
                                if pressed_keys[K_1]:
                                    dialogue.append([all_dialogue[current_dialogue][0]])
                                elif pressed_keys[K_2]:
                                    dialogue.append([all_dialogue[current_dialogue][1]])
                                elif pressed_keys[K_3]:
                                    dialogue.append([all_dialogue[current_dialogue][1]])
                        current_line = 0
                        all_sprites.remove(text_box)
                        text_box.kill()
                        text_box = create_text_box(dialogue[current_dialogue][current_line])
                        all_sprites.add(text_box)
            if not newChoice:
                if not pressed_keys[K_1] and not pressed_keys[K_2] and not pressed_keys[K_3]:
                    newChoice = True
        else:
            start = True
    pygame.display.update()

pygame.quit()