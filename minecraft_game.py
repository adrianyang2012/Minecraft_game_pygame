# imports
import sys
import math
import pygame
import random
# set up pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# set up game varibles
battle = 0
items = ['fist','bread']
items_dict_pics = {'fist':pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\punch.png"), (160,160)),'bread':pygame.image.load("Minecraft_game\Minecraft_game\Bread.webp")}
px = 0
py = 0
health = 20
coins = 0
lose = 0
enemys = []
for i in range(0,30):
  enemys.append((random.randint(0,800),random.randint(0,600)))
# creating display

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minecraft game")
running = True
image = pygame.image.load("Minecraft_game\Minecraft_game\idle180.png")
enemy_image = pygame.image.load("Minecraft_game\Minecraft_game\pigFace.png")
enemy_battle = pygame.image.load('Minecraft_game\Minecraft_game\Pig_battling.webp')
enemy_battle = pygame.transform.scale(enemy_battle, (100,100))
big_player = pygame.transform.scale(image, (100,100))
losed = 0
# creating a running loop
battle = 0
while running:
 

    for event in pygame.event.get():
            # only do something if the event is of type QUIT
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if not battle:
              if keys[pygame.K_w] or keys[pygame.K_UP]:
                py -=3
              if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                py+=3
              if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                px -=3
              if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                px+=3
    if battle:


      if attacker == 'e':
        if en_attacking:
          en_x-=0.5
          if en_x < 100:
            health -= 1
            attacker = 'p'
            p_attacking = 0

          if en_x < 150:
            p_x-=0.5
        else:
          if p_x > 100:
            p_x -= 0.4
          else:
            en_attacking = 1
          if p_x > 350:
            en_x -= 0.4  
      else:
        
        if en_x < 400:
        
          en_x+=0.4
        if p_x < 100:
          p_x+=0.4
        if keys[pygame.K_1]:
          p_attacking = 1
        if keys[pygame.K_2]:
          if items[1] != 0:
            health += 2
            attacker = 'e'
            items[1] = 0
        if p_attacking:
          p_x+=0.5
          if p_x > 400:
            p_attacking = 0
            en_attacking = 0
            attacker = 'e'
            if random.randint(0,3) == 3:
              en_health -=2
            en_health -=1
          


          if p_x > 350:
            en_x+=0.5
        if en_health < 1 or health < 1:
          battle = 0
          if health < 1:
            losed = 1
      if battle:
        screen.fill((0,0,255))
        # place everything after this
        i = 50
        for item in items:
          i += 200
          try:
            screen.blit(items_dict_pics[item],(i,100))
          except:
            pass
        try:
          text_surface = my_font.render(str(health), False, (255-health*11, health*11, 0))
        except:
          text_surface = my_font.render(str(health), False, (0, 255, 0))
        screen.blit(text_surface, (p_x+20,450))
        text_surface2 = my_font.render(str(en_health), False, (255-en_health*21, en_health*21, 0))
        screen.blit(text_surface2, (en_x+20,450))
        screen.blit(enemy_battle,(en_x,520))
        screen.blit(big_player,(p_x,500))

    else:
      if not losed:        
        screen.fill((0,255,0))
      
        screen.blit(image, (px,py))
        for enemy in enemys:
          screen.blit(enemy_image,(enemy[0],enemy[1]))
          if math.sqrt((enemy[0]-px)**2 + (enemy[1]-py)**2) < 30:
            en_x = 400
            enemys.remove(enemy)
            en_health = random.randint(10,12)
            p_x = 100
            p_attacking = 0
            en_attacking = 1
            battle = 1
            attacker = 'e'
      else:
        screen.fill((255,0,0))
        lose_surface = my_font.render('You Lose!', False, (0, 0, 0))
        screen.blit(lose_surface,(300,200))

          
    pygame.display.flip()
    
