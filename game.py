import pygame
import moviepy.editor as mp
import os
import time
import json

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 1200, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sword&Shield | The game")

# Set up the player character
player_size = 64
if os.path.exists("saves"):
    with open("saves", "r") as s:
        save_data = s.read().strip()  # Leggi il contenuto del file e rimuovi eventuali spazi bianchi
    if save_data:
        ps = save_data.split("|")
        player_x = int(ps[0])
        player_y = int(ps[1])
        invsel=int(ps[2])
        invel=ps[3].split("-")
    else:
        player_x = width // 2 - player_size // 2
        player_y = 700
        invsel=1
        invel=["Spada Classica.png","","","Scudo base.png"]
else:
    player_x = width // 2 - player_size // 2
    player_y = 700
    invsel=1
    invel=["Spada Classica.png","","","Scudo base.png"]

player_speed = 4

# Load the GIF and convert it to a series of frames
walking = mp.VideoFileClip("assets/walking.gif")
wfr = walking.iter_frames()

with open("data.json", "r") as f:
    data=json.loads(f.read())

nwalking = mp.VideoFileClip("assets/nwalking.gif")
nwfr = nwalking.iter_frames()

bg=pygame.image.load("assets/bg.png")
inv=pygame.image.load("assets/inv.png")
invs=pygame.image.load("assets/invs.png")
invshield=pygame.image.load("assets/invshield.png")
cards={}
for root, dirs, files in os.walk("assets/swords"):
    for file in files:
        cards[file] = pygame.transform.scale(pygame.image.load(os.path.join(root, file)), (51, 72))


def draw_player(frame):
    player_surface = pygame.surfarray.make_surface(frame)
    player_surface.set_alpha(255)
    screen.blit(player_surface, (player_x%1200, player_y%1000))


def coll(index):
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    object_rect=pygame.Rect(elements[index]["x"],elements[index]["y"],elements[index]["w"],elements[index]["h"])
    return player_rect.colliderect(object_rect)

elements=[{}]

elements[0]["x"]=500
elements[0]["y"]=500
elements[0]["texture"]=cards["Baal GS.png"]
elements[0]["w"]=51
elements[0]["h"]=72
elements[0]["name"]="Baal GS.png"

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    wk=True
    
    if keys[pygame.K_LCTRL]:
        player_speed=7
    else:
        player_speed=4
    
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d] and not keys[pygame.K_w]:
        wk=False
    
    if keys[pygame.K_1]:
        invsel=1
    elif keys[pygame.K_2]:
        invsel=2
    elif keys[pygame.K_3]:
        invsel=3
    
    if keys[pygame.K_LEFT]:
        invsel-=1
        time.sleep(0.05)
    elif keys[pygame.K_RIGHT]:
        invsel+=1
        time.sleep(0.05)
    
    with open("saves", "w") as s:
        s.write(str(player_x)+"|"+str(player_y)+"|"+str(invsel)+"|"+str(invel[0])+"-"+str(invel[2])+"-"+str(invel[2])+"-"+str(invel[3]))
        

    if wk:
        try:
            frame = next(wfr)
        except StopIteration:
            wfr = walking.iter_frames()
            frame = next(wfr)
        screen.blit(bg, (0, 0))
        draw_player(frame)
    else:
        try:
            frame = next(nwfr)
        except StopIteration:
            nwfr = nwalking.iter_frames()
            frame = next(nwfr)
        screen.blit(bg, (0, 0))
        draw_player(frame)
    screen.blit(invshield, (0, 1000-96))
    if invsel%3 == 1:
        screen.blit(invs, (((1200-96*3)/2), 1000-96))
        screen.blit(inv, (((1200-96*3)/2)+96, 1000-96))
        screen.blit(inv, (((1200-96*3)/2)+96*2, 1000-96))
    elif invsel%3 == 2:
        screen.blit(inv, (((1200-96*3)/2), 1000-96))
        screen.blit(invs, (((1200-96*3)/2)+96, 1000-96))
        screen.blit(inv, (((1200-96*3)/2)+96*2, 1000-96))
    elif invsel%3 == 0:
        screen.blit(inv, (((1200-96*3)/2), 1000-96))
        screen.blit(inv, (((1200-96*3)/2)+96, 1000-96))
        screen.blit(invs, (((1200-96*3)/2)+96*2, 1000-96))
    
    for i in invel:
        if i == "":
            pass
        else:
            if i == invel[0]:
                screen.blit(cards[i], (((1200-96*3)/2)+22.5, 1000-96+12))
            elif i == invel[1]:
                screen.blit(cards[i], (((1200-96*3)/2)+96+22.5, 1000-96+12))
            elif i == invel[2]:
                screen.blit(cards[i], (((1200-96*3)/2)+96+96+22.5, 1000-96+12))
            elif i == invel[3]:
                screen.blit(cards[i], (22.5, 1000-96+12))
    
    
    for i in elements:
        screen.blit(i["texture"], (i["x"],i["y"]))
    
    for i in range(len(elements)):
        if coll(i):
            for n in range(len(invel)):
                if n == 3:
                    pass
                else:
                    if invel[n] == "":
                        invel[n] == elements[i]["name"]
    
    # Update the game display
    pygame.display.flip()
    
# Quit the game
pygame.quit()


"""

objx=obj_x-(player_x%1200)
objy=obj_y-(player_y%1000)

"""
