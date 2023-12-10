import sys
import pygame
# initialising pygame
pygame.init()
import random



items = ['bread','fist']

costs = {'wooden sword':2,'stone sword':4,'bow':7,'iron sword':9,'crossbow':10,'grenade':15,'bread':1,'apple':2,'sandwitch':3,'cake':8,'extra large pizza':12}
weapons_dict = {'fist':1,'wooden sword':5,'stone sword':7,'bow':8,'iron sword':9,'crossbow':11,'grenade':14}
food_dict = {'bread':2,'apple':4,'sandwitch':6,'cake':7,'extra large pizza':10}
px = 0
py = 0
health = 20
coins = 0
lose = 0

# creating display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minecraft game")
running = True
image = pygame.image.load("Minecraft_game\idle180.png")
# creating a running loop
while running:
       
    # creating a loop to check events that 
    # are occurring

    for event in pygame.event.get():
            # only do something if the event is of type QUIT
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if keys[pygame.K_w]:
              py -=3
            if keys[pygame.K_s]:
              py+=3
            if keys[pygame.K_a]:
              px -=3
            if keys[pygame.K_d]:
              px+=3
            
            
    screen.fill((0,255,0))
    screen.blit(image, (px,py))
    
    pygame.display.flip()
