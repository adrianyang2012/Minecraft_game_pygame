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
items = ['fist','bread','strength potion','turtle potion','brilliant potion']
items_dict_pics = {'fist':pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\punch.png"), (80,80)),'bread':pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\Bread.webp"),(80,80)),'strength potion':pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\strength_potion.png"), (80,80)),'turtle potion':pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\Health_Potion.webp"), (80,80)),'brilliant potion':pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\Brilliant_potion.webp"), (80,80))}
px = 0
py = 0
health = 30
coins = 0
lose = 0
enemys = []
rects = []
def update_strength():
  global strength
  strength = (strength+1)/2
  if abs(strength-1) < 0.1:
    strength = 1
  #print(strength)
for i in range(0,30):
  enemys.append((random.randint(0,800),random.randint(0,600)))
enemys.append((500,300))
# creating display
def lose_screen():
  screen.fill((255,0,0))
  lose_surface = my_font.render('You Lose!', False, (0, 0, 0))
  screen.blit(lose_surface,(300,200))
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minecraft game")
running = True
image = pygame.image.load("Minecraft_game\Minecraft_game\idle180.png")
enemy_image = pygame.image.load("Minecraft_game\Minecraft_game\pigFace.png")
boss_image = pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\pigFace.png"),(200,100))
shop_image = pygame.transform.scale(pygame.image.load("Minecraft_game\Minecraft_game\Shop_button.png"),(80,80))


enemy_battle = pygame.image.load('Minecraft_game\Minecraft_game\Pig_battling.webp')
enemy_battle = pygame.transform.scale(enemy_battle, (100,100))
big_player = pygame.transform.scale(image, (100,100))


losed = 0
boss = 0
coins = 0
shop = 0
# creating a running loop
battle = 0
strength = 1
attacker_type = 'normal'
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

            if event.type == pygame.MOUSEBUTTONDOWN:
              mouse = pygame.mouse.get_pos()
              if pygame.Rect.collidepoint(shop_rect, mouse):
                if shop == 0:
                  shop = 1
                else:
                  shop = 0
            if shop:
              if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0,len(rects)):
                  print(rects)
                  mouse = pygame.mouse.get_pos()
                  if pygame.Rect.collidepoint(rects[i], mouse):
                    if i == 0:
                      if coins > 1:
                        coins-=2
                        items.append('bread')
                      break
                    if i == 1:
                      if coins > 4:
                        coins-=5
                        items.append('strength potion')
                      break
                      
                    if i == 2:
                      if coins > 4:
                        coins-=5
                        items.append('turtle potion')
                      break
                    if i == 3:
                      if coins > 8:
                        coins-=9
                        items.append('brilliant potion')

            if battle:
              if event.type == pygame.MOUSEBUTTONDOWN:
                #print(rects)
                for i in range(0,len(rects)):
                  mouse = pygame.mouse.get_pos()
                  if pygame.Rect.collidepoint(rects[i], mouse):
                    if items[i] == 'fist':
                      p_attacking = 1
                      update_strength()
                      #print(items)
                      break
                    if items[i] == 'bread':
                      attacker = 'e'
                      health +=2
                      update_strength()
                      items.remove('bread')
                      break
                      
                    if items[i] == 'strength potion':
                      health -= 5
                      strength = 8
                      attacker = 'e'
                      items.remove('strength potion')
                      break
                    if items[i] == 'turtle potion':
                      items.remove('turtle potion')
                      health += 5
                      strength = 0.125
                      attacker = 'e'
                      break
                  if items[i] == 'brilliant potion':
                    items.remove('brilliant potion')
                    health+=10
                    strength = 12
                    attacker = 'e'
                    break
                    
    if battle:


      if attacker == 'e':
        if en_attacking:
          en_x-=0.5
          if en_x < 100:
            health -= 1
            if attacker_type == 'boss':
              health-=2
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
        

        if p_attacking:
          p_x+=0.5
          if p_x > 400:
            p_attacking = 0
            en_attacking = 0
            attacker = 'e'
            if random.randint(0,3) == 3:
              en_health -=2*strength
              
            en_health -=1*strength
          


          if p_x > 350:
            en_x+=0.5
        if en_health < 1 or health < 1:
          coins+=random.randint(3,6)
          battle = 0
          if health < 1:
            losed = 1
      if battle:
        screen.fill((0,0,255))
        # place everything after this
        i = 50
        rects = []
        for item in items:
          i += 80
          rects.append(items_dict_pics[item].get_rect(x=i,y=100))
          screen.blit(items_dict_pics[item],(i,100))

        try:
          text_surface = my_font.render(str(health), False, (255-health*11, health*11, 0))
        except:
          text_surface = my_font.render(str(health), False, (0, 255, 0))
        screen.blit(text_surface, (p_x+20,450))
        if attacker_type == 'boss':
          text_surface2 = my_font.render(str(en_health), False, (255-en_health*5, en_health*5, 0))
        else:
          text_surface2 = my_font.render(str(en_health), False, (255-en_health*21, en_health*21, 0))
        screen.blit(text_surface2, (en_x+20,450))
        screen.blit(enemy_battle,(en_x,520))
        screen.blit(big_player,(p_x,500))

    else:
      if shop:
        screen.fill((50,50,50))
        screen.blit(shop_image, (550,0))
        i = 50
        rects = []
        for item in ['bread','strength potion','turtle potion','brilliant potion']:
          i += 120
          rects.append(items_dict_pics[item].get_rect(x=i,y=100))
          screen.blit(items_dict_pics[item],(i,100))
      else:
        if not losed:        
          screen.fill((0,255,0))
          
          player_rect= image.get_rect(x=px,y=py)
          for enemy in enemys:
            if enemy == (500,300):
              screen.blit(boss_image,(enemy[0],enemy[1]))
              boss = 1
            else:  
              screen.blit(enemy_image,(enemy[0],enemy[1]))
              boss = 0
            if pygame.Rect.colliderect(enemy_image.get_rect(x=enemy[0],y=enemy[1]),player_rect):
              en_x = 400
              enemys.remove(enemy)
              attacker_type = 'normal'
              if boss == 1:
                attacker_type = 'boss'
              en_health = random.randint(10,12)
              if attacker_type == 'boss':
                en_health = 50
              p_x = 100
              p_attacking = 0
              en_attacking = 1
              battle = 1
              attacker = 'e'
          text_surface_coins = my_font.render(str(coins), False, (0, 0, 0))
          screen.blit(text_surface_coins,(750,0))
          text_surface_coins = my_font.render("Shop", False, (0, 0, 0))
          
          screen.blit(shop_image, (550,0))
          shop_rect = shop_image.get_rect(x=550,y=0)
          mouse = pygame.mouse.get_pos()

          screen.blit(text_surface_coins,(650,0))
          screen.blit(image, (px,py))
              
          
        else:
          lose_screen()

          
    pygame.display.flip()
    
