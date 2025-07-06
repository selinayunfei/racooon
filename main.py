import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def create_text_box(text, colour):
    box = pygame.sprite.Sprite()
    if colour == "yellow":
        box.image = pygame.image.load("box.png").convert_alpha()
    elif colour == "red":
        box.image = pygame.image.load("box2.png").convert_alpha()
    else:
        box.image = pygame.image.load("box3.png").convert_alpha()
        
    box.rect = box.image.get_rect(center=(640, 620))
    box.text = text
    return box

def opening_sequence():
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    color = (252, 212, 210)
    screen.fill(color)
    
    texts = ["It's another day. Another great day!", 
             "You walk into Tim Hortons.", 
             "However... you find that...", 
             "Shucks! Raccoons are trying to court you!", 
             "But you don't want to date a raccoon! Work hard to reject them!!"]
    
    index = 0  
    font = pygame.font.SysFont('comicsansms', 20)
    
    running = True
    while running:
        screen.fill(color) 
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                index += 1 
                if index >= len(texts): 
                    running = False
        
        if index < len(texts):
            text = font.render(texts[index], True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)
        
        pygame.display.flip()         


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
bg = pygame.image.load("wp5641813.webp")

all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('comicsansms', 20)

# Game state
levels = ["richguy","weirdguy","bestfriend"]
n = 0
level = levels[n]

newChoice = True
running = True
start = True
while running:
    if start:
        current_dialogue = 0
        current_line = 0
        if level == "richguy":
            colour = "yellow"
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
        if level == "weirdguy":
            colour = "red"
            dialogue = [
                ["*walks in*","are you siri? cuz girl, you auto-complete me."]
            ]
            all_dialogue = {1:["ohhhh skibidi sigma my rizz is getting me so much mewing aura. i love festiness in a lady. as the 9/10 i am, your number's the one thing i need~", "you don't? but i certainly know you, darling. and i'd love to get to know you better~","hm. maybe we should come to my house then. according to quantum physics, anything could happen~"],2:["but it was such a blessing for me to meet you. i'm pulled to you in so many ways... don't you feel it too?","oh, but i'd quite like it if we did. don't you feel those sparks between us?","mn, i'll stay a little farther. but god, can't you see the connection between us, like we were meant to be?"],3:["turn that to the positive, won't you? maybe it's simply attraction, and your heart is just pounding so loudly being next to me.","try a little harder, maybe you'll hear your heart beat, just for me.","ah. yes. isn't your heart pounding so loudly?"], 4:["oh, but i simply can't control my love, baby~ i'd love to continue this later on~","mn, perhaps another day. i'll see you for now."]}
            choices = [
                ["1. um, what the hell? go away, dude. you're disgusting.","2. ...i'm sorry, do i know you?","3. ooh~ i'd love to be autocompleted by such a handsome raccoon."],
                ["1. who the hell introduced me to you? i need to punch them in the face.","2. thanks, i'd rather we didn't.","3. Oh, I just love how direct you are. Won't you come a little closer?"],
                ["1. i only feel digust and vague hatred.","2. i see nothing.","3. i think i see them, but that might simply be the dizziness - you're too much for me to handle."],
                [["1. are you high?","2. you're sick in the head.","fine. maybe it is."], ["1. no.","2.yes, i think i feel something... heartburn. ate my lunch too fast.","3. oh, it was pounding loud enough you could hear it?"],["1. not really.","2. it is - do you perhaps know the cure?","3. pouding with the sheer affection i'm feeling for you~"]]
            ]
        if level == "bestfriend":
            colour = "blue"
            dialogue = [
                ["*appears before you*","hi y/n! lonmhg timdhje nods seewe! hoiwiw hasave yfgou beedsqen thihgs lafsst yeadar?"]
            ]
            all_dialogue = {1:["YESSS!!!! I'M SO HAPPY YOU REMEMBER, I EVEN GOT US THE DINNER WE HAD THAT DAY!!!","the rose! don't you remember? i ordered us the meal we ate that day too!","...oh, okay. Uh, I ordered us the meal i remember you liked!"],2:["*blushes* I'm so glad you're happy! I told you to meet up here because I thought you'd enjoy being at a Tim Hortons, you loved it so much when we were younger!","Okay! How have these last years been? I remember you said you wanted to be a cashier at Tim Hortons!","Damn. Maybe we can change it. Didn't you always want to work here? You can recommend us something!"],3:["oh! *blushes furiously* I thought we could do something else fun after dinner? I'm already so happy being with you!","Ah... I feel that! I thought I'd really enjoy university, but it didn't go how I wanted. How about we go do something else fun then?","you don't have to be so mean... Uhm, uh, maybe I remembered wrong then. We could do something else fun, maybe?"],4:["That sounds really awesome. We should do this again tomorrow! I'll be waiting for you!","Oh. I guess we can meet again tomorrow then."]}
            choices = [
                ["1.OH MY GOD IS THAT THE ROSE FROM OUR CHILDHOOD?","2. what's in your mouth?","3. ew, what's that? spit it out rn"],
                ["1. Haha, you really remembered? That's so sweet.","2. oh, sounds good.","3. ...i hate that."],
                ["1. You remembered? Good boy~", "2. Eh. Didn't quite work out in the end, you know?", "3. What the hell? You're tweaking, bro."],
                [["1. Something else fun, hmm~ I have a few ideas too.", "2. Good. I'm also having a fun time.","3. Oh, just being with me is making you happy?"],["1. Ooh, something else fun? Okay!","2. Sounds good, I'm up for whatever.","3. Not really up to it today."],["1. Sure, since this has been such a disappointment.","2. Eh. Whatever you want.", "3. Who'd want to do something fun with you? You're so clingy."]]
            ]
        text_box = create_text_box(dialogue[current_dialogue][current_line],colour)
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
                    text_box = create_text_box(dialogue[current_dialogue][current_line],colour)
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
                        text_box = create_text_box(dialogue[current_dialogue][current_line],colour)
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

                        if level == "richguy" or level == "weirdguy":
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
                                    
                        if level == "bestfriend":
                            if currentChoice == 0:
                                dialogue.append([all_dialogue[current_dialogue][0]])
                            elif currentChoice == 1 or currentChoice == 2:
                                if pressed_keys[K_1] or pressed_keys[K_2]:
                                    dialogue.append([all_dialogue[current_dialogue][0]])
                                else:
                                    dialogue.append([all_dialogue[current_dialogue][1]])

                        current_line = 0
                        all_sprites.remove(text_box)
                        text_box.kill()
                        text_box = create_text_box(dialogue[current_dialogue][current_line],colour)
                        all_sprites.add(text_box)

            if not newChoice:
                if not pressed_keys[K_1] and not pressed_keys[K_2] and not pressed_keys[K_3]:
                    newChoice = True
        else:
            if pressed_keys[K_RETURN]:
                n += 1
                if n < len(levels):
                    level = levels[n] 
                    start = True
    pygame.display.update()

pygame.quit()