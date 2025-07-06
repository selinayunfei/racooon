import pygame
from pygame.locals import *
import time
import math

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class LoveBar(pygame.sprite.Sprite):
    def __init__(self, image_path, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (500, 50))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def update_bar(self, new_image_path):
        self.image = pygame.transform.scale(pygame.image.load(new_image_path), (500, 50))
        self.image = self.image.convert_alpha()

def updating_lovebar(index,lovebars,lovebar):
    if pressed_keys[K_1]:
        index += 1
        if index < len(lovebars):
            lovebar.update_bar(lovebars[index])
    elif pressed_keys[K_3]:
        index -= 1
        if index >= 0:
            if index > 4:
                index = 4
            lovebar.update_bar(lovebars[index])
    return index

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

def create_raccoon(image):
    raccoon = pygame.sprite.Sprite()
    raccoon.image = pygame.image.load(image).convert_alpha()
    raccoon.image = pygame.transform.scale(raccoon.image, (1280, 720))
    raccoon.rect = raccoon.image.get_rect(center = (640, 360))
    raccoon.speed = 1
    return raccoon

def update_raccoon(raccoon):
    raccoon.rect.move_ip(0,raccoon.speed)
    if raccoon.rect.centery <= 350 or raccoon.rect.centery >= 390:
        raccoon.speed = -raccoon.speed

def ending(end):
    cont = False
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
                        if (end[-1] == 'H' or end[-1]=='G') and end != "THG":
                            running = False
                            cont = True
                        else:
                            running = False
                            cont = False
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
    return cont

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
bg = pygame.image.load("sittingTH.png")

all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('comicsansms', 20)
pink = (255, 105, 180)

# Add after defining your font (or near top)
def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    return lines

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

# Game state
lovebars = ["0.png","25.png","50.png","75.png","100.png"]
levels = ["richguy","weirdguy","bestfriend"]
n = 0
level = levels[n]

newChoice = True
running = True
start = True
frame = 0
opening_sequence()
clock = pygame.time.Clock()
while running:
    frame += 1
    if start:
        frame = 0
        current_dialogue = 0
        current_line = 0
        if level == "richguy":
            walking_animation("good_rich_guy_fat_chibi.png")
            raccoon = create_raccoon("richguy_default_smirk.png")
            all_sprites.add(raccoon)
            lovebar = LoveBar('25.png',(300,60))
            nl = 1

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
            walking_animation("good_weird_guy_fat_chibi.png")
            lovebar = LoveBar('50.png',(300,60))
            nl = 2

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
            all_sprites.remove(raccoon)
            raccoon.kill()
            
            walking_animation("good_childhood_friend_fat_chibi.png")
            raccoon = create_raccoon("childhood bestie 2 entrance w rose.png")
            all_sprites.add(raccoon)
            lovebar = LoveBar('75.png',(300,60))
            nl = 3

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
        all_sprites.add(lovebar)

        text_box = create_text_box(dialogue[current_dialogue][current_line],colour)
        all_sprites.add(text_box)

        start = False
    if frame % 3 == 0:
        update_raccoon(raccoon)
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
        lines = wrap_text(text_box.text, font, 900)
        y = 590  # Start a bit above 620 to center multi-line
        for line in lines:
            text_surface = font.render(line, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(640, y))
            screen.blit(text_surface, text_rect)
            y += 25  # Adjust spacing between lines

    # Render choices if at the end of dialogue
    if current_line == len(dialogue[current_dialogue]) - 1:
        choice_height = 375
        if current_dialogue < 4:
            choices_image = pygame.image.load("actualchoices.png")
            choices_image = pygame.transform.scale(choices_image, (460, 160))
            choices_rect = choices_image.get_rect(center = (1020, 450))
            screen.blit(choices_image, choices_rect)
            if current_dialogue < 3:
                for choice in choices[current_dialogue]:                
                    wrapped = wrap_text(choice, font, 450)
                    for line in wrapped:
                        choice_surface = font.render(line, True, (0, 0, 0))
                        choice_rect = choice_surface.get_rect(topleft=(800, choice_height))
                        screen.blit(choice_surface, choice_rect)
                        choice_height += 25
                    if (pressed_keys[K_1] or pressed_keys[K_2] or pressed_keys[K_3]) and newChoice:
                        newChoice = False
                        current_dialogue += 1
                        nl = updating_lovebar(nl,lovebars,lovebar)
                        if pressed_keys[K_1]:
                            if current_dialogue == 1 and level == "bestfriend":
                                memory = pygame.image.load("childhood best friend - the first meeting, pictures.png")
                                memory = pygame.transform.scale(memory, (1400,800))
                                memory_rect = memory.get_rect(center = (640, 360))
                                screen.blit(memory, memory_rect)
                                pygame.display.update()
                                time.sleep(5)
                            if current_dialogue == 2 and level == "bestfriend":
                                all_sprites.remove(raccoon)     
                                raccoon.kill()
                                raccoon = create_raccoon("childhood bestie 3 small blush.png")
                                all_sprites.add(raccoon)
                            if current_dialogue == 3 and level == "bestfriend":
                                all_sprites.remove(raccoon)     
                                raccoon.kill()
                                raccoon = create_raccoon("childhood bestie 4 big blush.png")
                                all_sprites.add(raccoon)
                            currentChoice = 0
                            dialogue.append([all_dialogue[current_dialogue][0]])
                        elif pressed_keys[K_2]:
                            if level == "richguy" and current_dialogue == 3:
                                all_sprites.remove(raccoon)     
                                raccoon.kill()
                                raccoon = create_raccoon("richguy_sigh_WITH_sigh_bubble.png")
                                all_sprites.add(raccoon)
                            currentChoice = 1
                            dialogue.append([all_dialogue[current_dialogue][1]])
                        elif pressed_keys[K_3]:
                            if level == "richguy" and current_dialogue == 1:
                                all_sprites.remove(raccoon)     
                                raccoon.kill()
                                raccoon = create_raccoon("richguy_sad_look_at_watch.png")
                                all_sprites.add(raccoon)
                            if current_dialogue == 3 and level == "bestfriend":
                                all_sprites.remove(raccoon)     
                                raccoon.kill()
                                raccoon = create_raccoon("childhood bestie 5 heartbroken.png")
                                all_sprites.add(raccoon)
                            currentChoice = 2
                            dialogue.append([all_dialogue[current_dialogue][2]])
                        current_line = 0
                        if current_dialogue >= 1 and current_dialogue < 3 and level == "bestfriend":
                            all_sprites.remove(raccoon)     
                            raccoon.kill()
                            raccoon = create_raccoon("childhood bestie 1 normal.png")
                            all_sprites.add(raccoon)
                        all_sprites.remove(text_box)
                        text_box.kill()
                        text_box = create_text_box(dialogue[current_dialogue][current_line],colour)
                        all_sprites.add(text_box)
            elif current_dialogue == 3:
                for choice in choices[current_dialogue][currentChoice]:
                    wrapped = wrap_text(choice, font, 450)
                    for line in wrapped:
                        choice_surface = font.render(line, True, (0, 0, 0))
                        choice_rect = choice_surface.get_rect(topleft=(800, choice_height))
                        screen.blit(choice_surface, choice_rect)
                        choice_height += 25  # smaller spacing since it's in a tighter box
                    if (pressed_keys[K_1] or pressed_keys[K_2] or pressed_keys[K_3]) and newChoice:
                        nl = updating_lovebar(nl,lovebars,lovebar)
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
                            if dialogue[-1] == [all_dialogue[current_dialogue][0]]:
                                all_sprites.remove(raccoon)     
                                raccoon.kill()
                                raccoon = create_raccoon("richguy_default_V2_blush_and_heart.png")
                                all_sprites.add(raccoon)
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
            all_sprites.remove(lovebar)
            if pressed_keys[K_RETURN]:
                n += 1
                start = True
            if start:
                if level == "richguy":
                    if nl <= 0:
                        running = ending("WeddingH")
                    else:
                        running = ending("WeddingB")
                elif level == "weirdguy":
                    if nl <= 0:
                        running = ending("TVG")
                    else:
                        running = ending("TVB")
                elif level == "bestfriend":
                    if nl <= 0:
                        running = ending("THG")
                    else:
                        running = ending("THB")
                if n < len(levels):
                    level = levels[n]
    clock.tick(60)
    pygame.display.update()

pygame.quit()