import pygame
from sys import exit
from PROJECT_Player import Player
from PROJECT_Bullet import Bullet, Fast_Bullet, Big_Bullet
from random import randint
from PROJECT_Enemy import Enemy
FPS = 60
SC_HEIGHT = 640
SC_WIDHT = 800
DISPLAY = (SC_WIDHT, SC_HEIGHT)
ship = Player(SC_WIDHT // 2, SC_HEIGHT - 32)

def main():
    win_time = 60
    numb_ordin_bullets = 8 # обычные пули
    numb_fast_bullets = 5
    numb_big_bullets = 5
    lives = 15
    left = right = False
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('Космический бой')
    space_surf = pygame.image.load('space.jpg')
    space_rect = space_surf.get_rect(bottomright = (800, 640))
    screen.blit(space_surf, space_rect)
    clock = pygame.time.Clock()
    Bullets_group = []
    Bullets_fast_group = []
    Bullets_big_group  = []
    Enemy_speed_group = []
    Enemy_group = []
    time_spawn_enemy = 0
    random_time = randint(40, 180)
    Game_time = 0
    while True:
        if Game_time == 3600:
            pygame.quit()
            exit()
        if lives == 0:
            pygame.quit()
            exit()
        else:
            font_lives = pygame.font.SysFont('arial', 17)
            font_ordin_bullets = pygame.font.SysFont('arial', 17)
            font_fast_bullets = pygame.font.SysFont('arial', 17)
            font_big_bullets = pygame.font.SysFont('arial', 17)
            font_time = pygame.font.SysFont('arial', 17)
            Game_time += 1
            time_spawn_enemy += 1
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if i.type == pygame.KEYDOWN and i.key == pygame.K_a:
                    left = True
                if i.type == pygame.KEYDOWN and i.key == pygame.K_d:
                    right = True
                if i.type == pygame.KEYUP and i.key == pygame.K_a:
                    left = False
                if i.type == pygame.KEYUP and i.key == pygame.K_d:
                    right = False
                if i.type == pygame.KEYDOWN and i.key == pygame.K_8 and numb_ordin_bullets > 0:
                    bullet = Bullet(ship)
                    Bullets_group.append(bullet)
                    numb_ordin_bullets -= 1
                if i.type == pygame.KEYDOWN and i.key == pygame.K_9 and numb_fast_bullets > 0:
                    fast_bullet = Fast_Bullet(ship)
                    Bullets_fast_group.append(fast_bullet)
                    numb_fast_bullets -= 1
                if i.type == pygame.KEYDOWN and i.key == pygame.K_0 and numb_big_bullets > 0:
                    big_bullet = Big_Bullet(ship)
                    Bullets_big_group.append(big_bullet)
                    numb_big_bullets -= 1
                    
            screen.blit(space_surf, space_rect)
            if time_spawn_enemy == random_time:
                random_time = randint(40,180)
                time_spawn_enemy = 0
                enemy = Enemy()
                Enemy_group.append(enemy)
                Enemy_speed_group.append(randint(1, 3))

            flag_collide = False # проверка на соприкосновение c обычным снарядом
            for k in range(len(Bullets_group)):
                if  285 <= Bullets_group[k].rect.y <= 502:
                    for p in range(len(Enemy_group)):
                        if Enemy_group[p].rect.colliderect(Bullets_group[k].rect) == 1:
                            Bullets_group[k] = 'a'
                            Enemy_group[p] = 'a'
                            Enemy_speed_group[p] = 'a'
                            flag_collide = True
                            numb_ordin_bullets += 2
                            break

                if flag_collide is True:
                    break

            if flag_collide == True:
                Bullets_group.remove('a')
                Enemy_group.remove('a')
                Enemy_speed_group.remove('a')

            flag_collide_fast = False # проверка на соприкосновение с быстрым снарядом
            for k in range(len(Bullets_fast_group)):
                if 285 <= Bullets_fast_group[k].rect.y <= 505:
                    for p in range(len(Enemy_group)):
                        if Enemy_group[p].rect.colliderect(Bullets_fast_group[k].rect) == 1:
                            Bullets_fast_group[k] = 'a'
                            Enemy_group[p] = 'a'
                            Enemy_speed_group[p] = 'a'
                            flag_collide_fast = True
                            numb_fast_bullets += 2
                            break
                if flag_collide_fast is True:
                    break
            if flag_collide_fast == True:
                Bullets_fast_group.remove('a')
                Enemy_group.remove('a')
                Enemy_speed_group.remove('a')
                
            flag_collide_big = False # проверка на соприкосновение с большим снарядом
            for k in range(len(Bullets_big_group)):
                if 285 <= Bullets_big_group[k].rect.y <= 510:
                    for p in range(len(Enemy_group)):
                        if Enemy_group[p].rect.colliderect(Bullets_big_group[k].rect) == 1:
                            Bullets_big_group[k] = 'a'
                            Enemy_group[p] = 'a'
                            Enemy_speed_group[p] = 'a'
                            flag_collide_big = True
                            numb_big_bullets += 2
                            break
                if flag_collide_big is True:
                    break
            if flag_collide_big == True:
                Bullets_big_group.remove('a')
                Enemy_group.remove('a')
                Enemy_speed_group.remove('a')

            flag_bullets_group = False # проверка на вылетевший за предел экрана снаряд
            for k in range(len(Bullets_group)):
                if Bullets_group[k].rect.y > 0:
                    Bullets_group[k].update()
                    Bullets_group[k].draw(screen)
                else:
                    flag_bullets_group = True
                    Bullets_group[k] = 'a'
            if flag_bullets_group is True:
                Bullets_group.remove('a')

            flag_fast_bullet_group = False # проверка на вылетевший за предел экрана быстрый снаряд
            for k in range(len(Bullets_fast_group)):
                if Bullets_fast_group[k].rect.y > 0:
                    Bullets_fast_group[k].update()
                    Bullets_fast_group[k].draw(screen)
                else:
                    flag_fast_bullet_group = True
                    Bullets_fast_group[k] = 'a'
            if flag_fast_bullet_group is True:
                Bullets_fast_group.remove('a')

            flag_big_bullet_group = False # проверка на вылетевший за предел экрана большой снаряд
            for k in range(len(Bullets_big_group)):
                if Bullets_big_group[k].rect.y > 0:
                    Bullets_big_group[k].update()
                    Bullets_big_group[k].draw(screen)
                else:
                    flag_big_bullet_group = True
                    Bullets_big_group[k] = 'a'
            if flag_big_bullet_group is True:
                Bullets_big_group.remove('a')

            flag_enemy_group = False # проверка на вылетевшего за экран врага
            for n in range(len(Enemy_group)):
                if Enemy_group[n].rect.x <= SC_WIDHT:
                    Enemy_group[n].rect.x += Enemy_speed_group[n]
                    Enemy_group[n].draw(screen)
                else:
                    lives -= 1
                    flag_enemy_group = True
                    Enemy_group[n] = 'a'
                    Enemy_speed_group[n] = 'a'
            if flag_enemy_group is True:
                Enemy_group.remove('a')
                Enemy_speed_group.remove('a')

            if Game_time % 60 == 0:
                win_time -= 1
            text_lives = font_lives.render("Жизни:"+str(lives), 1, (255, 255, 255))
            text_ordin_bullets = font_ordin_bullets.render("Обычные снаряды "+str(numb_ordin_bullets), 1, (255, 255, 255))
            text_fast_bullets = font_fast_bullets.render("Быстрые снаряды "+str(numb_fast_bullets), 1, (255, 255, 255))
            text_big_bullets = font_big_bullets.render("Большие снаряды "+str(numb_big_bullets), 1, (255, 255, 255))
            text_time = font_time.render("Время до победы: "+str(win_time), 1, (255, 255, 255))
            screen.blit(text_fast_bullets, [0, 18])
            screen.blit(text_ordin_bullets, [0,0])
            screen.blit(text_big_bullets, [0, 36])
            screen.blit(text_lives, [737, 0])
            screen.blit(text_time, [650, 18])
            ship.update(left, right)
            ship.draw(screen)
            pygame.display.update()
            clock.tick(FPS)
main()
