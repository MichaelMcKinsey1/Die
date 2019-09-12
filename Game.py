import pygame
# from TextInput import *
import sys

from pygame.locals import *
from Character import *
from Bullet import *
import time
import random
from Platform import *
from Powerup import *

pygame.init()
pygame.font.init()
w = 1080
h = 720
screen = pygame.display.set_mode((w, h), 0, 32)
pygame.display.set_caption("Die")

background = (15, 160, 195)

# text_input = TextInput()
start_font = pygame.font.SysFont('Comic Sans MS', 30, "bold")
title_font = pygame.font.SysFont('Comic Sans MS', 100, "bold")
name_font = pygame.font.SysFont('Comic Sans MS', 20)
start_button = start_font.render('Start', False, (21, 255, 0))
title = title_font.render('DIE', False, (255, 255, 255))
start_button_2 = start_font.render('Start', False, (255, 0, 0))
start_button_3 = start_font.render('Start', False, (255, 242, 0))
names = name_font.render('By: Michael McKinsey and Zach St. Denis', False, (255, 255, 255))
p1functions = name_font.render("Player 1: A = Left, D = Right, T = Shoot, Y = Jump", False, (0, 0, 0))
p2functions = name_font.render("Player 2: Left Arrow = Left, Right Arrow = Right, 1 = Shoot, 2 = Jump", False, (0, 0, 0))
restarting = name_font.render("Restarting...", False, (255, 255, 255))


def main(score1, score2):
    pygame.init()
    begin = False
    p1 = Character("soldier_idle_right", 0, h - 57)
    p2 = Character("hero_idle_left", w, h - 57)
    heart = Powerup()
    jump_vel = -1.65
    p1jumps = 0
    p2jumps = 0
    p1bullets = []
    p2bullets = []
    p1kills = score1
    p2kills = score2
    p1limit = p1kills + 1
    p2limit = p2kills + 1

    while not begin:
        # events = pygame.event.get()
        event = pygame.event.poll()
        screen.fill(background)
        screen.blit(start_button, (w / 2 - 50, h / 2))
        screen.blit(title, (w / 2 - 100, 20))
        screen.blit(names, (w / 2 - 175, 150))
        screen.blit(p1functions, (325, 300))
        screen.blit(p2functions, (225, 450))
        # screen.blit(text_input.get_surface(), (10, 10))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if mouse_x > w / 2 - 50 and mouse_x < w / 2 + 30:
            if mouse_y > h / 2 and mouse_y < h / 2 + 40:
                screen.blit(start_button_2, (w / 2 - 50, h / 2))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.blit(start_button_3, (w / 2 - 50, h / 2))
                if event.type == pygame.MOUSEBUTTONUP:
                    begin = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.blit(start_button_2, (w / 2 - 50, h / 2))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                begin = True
        # text_input.update(events)
        pygame.display.flip()

    while begin:
        player1 = start_font.render('Player 1 Kills: {}'.format(p1kills), False, (255, 255, 255))
        player2 = start_font.render('Player 2 Kills: {}'.format(p2kills), False, (255, 255, 255))
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # down
        if event.type == pygame.KEYDOWN:
            # player 2
            if event.key == pygame.K_RIGHT:
                p2.set_char("hero_walk_right")
                if p2.juiced:
                    p2.x_vel = 1.2
                else:
                    p2.x_vel = .8
            if event.key == pygame.K_LEFT:
                p2.set_char("hero_walk_left")
                if p2.juiced:
                    p2.x_vel = -1.2
                else:
                    p2.x_vel = -.8
            if event.key == pygame.K_KP2:
                if p2jumps < 1:
                    if p2.juiced == True:
                        p2.y_vel = jump_vel * 1.35
                    else:
                        p2.y_vel = jump_vel
                    p2.set_char("hero_jump")
                    p2.touching_platform = False
                    p2jumps += 1
            if event.key == pygame.K_KP1:
                if p2bullets.__len__() == 0:
                    if not p2.character == "dead":
                        b = Bullet("p2", p2)
                        b.can_draw = True
                        p2bullets.append(b)
                        p2.set_char("hero_shoot")

            # player 1
            if event.key == pygame.K_d:
                p1.set_char("soldier_walk_right")
                if p1.juiced:
                    p1.x_vel = 1.2
                else:
                    p1.x_vel = .8
            if event.key == pygame.K_a:
                p1.set_char("soldier_walk_left")
                if p1.juiced:
                    p1.x_vel = -1.2
                else:
                    p1.x_vel = -.8
            if event.key == pygame.K_y:
                if p1jumps < 1:
                    if p1.juiced == True:
                        p1.y_vel = jump_vel * 1.35
                    else:
                        p1.y_vel = jump_vel
                    p1.set_char("soldier_jump")
                    p1.touching_platform = False
                    p1jumps += 1
            if event.key == pygame.K_t:
                if p1bullets.__len__() == 0:
                    if not p1.character == "dead":
                        b = Bullet("p1", p1)
                        b.can_draw = True
                        p1bullets.append(b)
                        p1.set_char("soldier_shoot")

        # release
        if event.type == pygame.KEYUP:
            # player 2
            if event.key == pygame.K_RIGHT:
                p2.set_char("hero_idle_right")
                p2.x_vel = 0
            if event.key == pygame.K_LEFT:
                p2.set_char("hero_idle_left")
                p2.x_vel = 0
            if event.key == pygame.K_KP2:
                if p2.facing == "right":
                    p2.set_char("hero_idle_right")
                else:
                    p2.set_char("hero_idle_left")
                # p2.jumping = False
            if event.key == pygame.K_KP1:
                if p2.facing == "right":
                    p2.set_char("hero_idle_right")
                else:
                    p2.set_char("hero_idle_left")

            # player 1
            if event.key == pygame.K_d:
                p1.set_char("soldier_idle_right")
                p1.x_vel = 0
            if event.key == pygame.K_a:
                p1.set_char("soldier_idle_left")
                p1.x_vel = 0
            if event.key == pygame.K_y:
                if p1.facing == "right":
                    p1.set_char("soldier_idle_right")
                else:
                    p1.set_char("soldier_idle_left")
            if event.key == pygame.K_t:
                if p1.facing == "right":
                    p1.set_char("soldier_idle_right")
                else:
                    p1.set_char("soldier_idle_left")

        # hit box
        for x in p2bullets:
            if x.x > p1.x and x.x < p1.x + 3:
                if x.y < p1.y + p1.h and x.y > p1.y:
                    p1.set_char("soldier_hurt")
                    x.can_draw = False
                    p2bullets.remove(x)
                    if not p2.character == "dead":
                        if p1.juiced:
                            p1.health -= .1
                        else:
                            p1.health -= .2
                        # p2.score += random.randint(1000, 1500)
        for x in p1bullets:
            if x.x > p2.x and x.x < p2.x + 3:
                if x.y < p2.y + p2.h and x.y > p2.y:
                    p2.set_char("hero_hurt")
                    x.can_draw = False
                    p1bullets.remove(x)
                    if not p1.character == "dead":
                        if p2.juiced:
                            p2.health -= .1
                        else:
                            p2.health -= .2
                        # p1.score += random.randint(1000, 1500)

        if p1.x > p2.x and p1.x < p2.x + p2.w:
            if p1.y >= p2.y - p2.h and p1.y <= p2.y + p2.h:
                p1.x = p2.x + p1.w
                p1.x_vel = 0
                p2.x_vel = 0
        if p1.x + p1.w > p2.x and p1.x < p2.x + p2.w:
            if p1.y >= p2.y - p2.h and p1.y <= p2.y + p2.h:
                p1.x = p2.x - p1.w
                p1.x_vel = 0
                p2.x_vel = 0

        if p2.x > p1.x and p2.x < p1.x + p1.w:
            if p2.y >= p1.y - p1.h and p2.y <= p1.y + p1.h:
                p2.x = p1.x + p2.w
                p1.x_vel = 0
                p2.x_vel = 0
        if p2.x + p2.w > p1.x and p2.x < p1.x + p1.w:
            if p2.y >= p1.y - p1.h and p2.y <= p1.y + p1.h:
                p2.x = p1.x - p2.w
                p1.x_vel = 0
                p2.x_vel = 0

        # screen borders
        if p2.x > w - p2.w:
            p2.x = w - p2.w
        if p2.x < 0:
            p2.x = 0
        if p1.x > w - p1.w:
            p1.x = w - p1.w
        if p1.x < 0:
            p1.x = 0

        if p1.y > h + 1000:
            p1.health = 0
            p1.y = h - p1.h
        if p2.y > h + 1000:
            p2.health = 0
            p2.y = h - p2.h

        # death
        if p1.health < .10:
            if p1.can_die:
                p1.set_char("dead")
                if p2kills < p2limit:
                    p2kills += 1
                p2.can_die = False
        if p2.health < .10:
            if p2.can_die:
                p2.set_char("dead")
                if p1kills < p1limit:
                    p1kills += 1
                p1.can_die = False

        if heart.can_draw:
            if heart.x >= p1.x and heart.x <= p1.x + p1.h:
                if heart.y >= p1.y and heart.y <= p1.y + p1.h:
                    p1.juiced = True
                    heart.collected = True
                    p1.timer = 0
                    # heart.can_draw = False

            if heart.x >= p2.x and heart.x <= p2.x + p2.h:
                if heart.y >= p2.y and heart.y <= p2.y + p2.h:
                    p2.juiced = True
                    heart.collected = True
                    p2.timer = 0
                    # heart.can_draw = False

        # screen.blit(pygame.transform.scale(pygame.image.load("bg.jpg"), (w, h)), (0, 0, 0, 0))
        screen.fill(background)
        # screen.blit(pygame.transform.scale(pygame.image.load("bg.jpg"), (1080, 720)), (0, 0))
        plat1 = Platform(screen, 0, 713, 225)
        plat2 = Platform(screen, 465, 473, 150)
        plat3 = Platform(screen, 0, 473, 150)
        plat4 = Platform(screen, 232.5, 593, 150)
        plat5 = Platform(screen, 232.5, 353, 150)
        plat6 = Platform(screen, 0, 233, 150)
        plat7 = Platform(screen, 465, 233, 150)
        plat8 = Platform(screen, 390, 713, 300)
        plat9 = Platform(screen, 232.5, 113, 150)
        plat10 = Platform(screen, 855, 713, 250)
        plat11 = Platform(screen, 930, 473, 150)
        plat12 = Platform(screen, 930, 233, 150)
        plat13 = Platform(screen, 697.5, 593, 150)
        plat14 = Platform(screen, 697.5, 353, 150)
        plat15 = Platform(screen, 697.5, 113, 150)
        plat16 = Platform(screen, 0, h - 7, w)

        platforms = [plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, plat9, plat10, plat11, plat12, plat13, plat14, plat15, plat16]
        if not p2.is_touching_platform(platforms) == False and p2.y_vel > 0:
            p2.y = p2.is_touching_platform(platforms).y - p2.h
            p2.touching_platform = True
            p2.jumping = False
            p2.falling = False
            p2.y_vel = 0
            p2jumps = 0
        else:
            p2.falling = True

        if not p1.is_touching_platform(platforms) == False and p1.y_vel > 0:
            p1.y = p1.is_touching_platform(platforms).y - p1.h
            p1.touching_platform = True
            p1.jumping = False
            p1.falling = False
            p1.y_vel = 0
            p1jumps = 0
        else:
            p1.falling = True

        if event.type == KEYUP:
            if event.key == pygame.K_RETURN:
                if p1.character == "dead" or p2.character == "dead":
                    main(p1kills, p2kills)

        p1.update()
        p2.update()
        for x in p1bullets:
            if x.x > w:
                p1bullets.remove(x)
            if x.x < 0:
                p1bullets.remove(x)
            x.update()
            x.draw(screen)
        for x in p2bullets:
            if x.x > w:
                p2bullets.remove(x)
            if x.x < 0:
                p2bullets.remove(x)
            x.update()
            x.draw(screen)
        p1.draw(screen)
        p2.draw(screen)
        heart.update()
        heart.draw(screen)
        screen.blit(player1, (50, 10))
        screen.blit(player2, (w - 325, 10))
        pygame.display.set_caption("Die: P1 ({}".format(math.floor(p1.x)) + ", {}".format(math.floor(p1.y)) + "), P2 ({}".format(math.floor(p2.x)) + ", {}".format(math.floor(p2.y)) + ")" )
        pygame.display.flip()


if __name__ == '__main__':
    main(0, 0)