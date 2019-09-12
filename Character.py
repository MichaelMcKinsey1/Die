import pygame
import sys
from pygame.locals import *
import math


class Character(pygame.sprite.Sprite):

    character = ""
    rect = (0, 0, 0, 0)
    x, y, w, h = 540, 360, 50, 50
    y_vel, x_vel = 0, 0
    facing = "right"
    can_shoot, jumping, falling, can_move, touching_platform = True, False, False, True, True
    health = 1.0
    bar_color = (66, 244, 69)
    yellow = (244, 229, 66)
    red = (255, 0, 0)
    prev_char = ""
    gravity = .01
    hir, hil, hwr, hwl, hjump, hfjump, hshoot, hfshoot, hhurt, hfhurt = [], [], [], [], [], [], [], [], [], []
    sir, sil, swr, swl, shurt, sfhurt, sjump, sfjump, sshoot, sfshoot = [], [], [], [], [], [], [], [], [], []
    dead = []
    score = 0
    juiced = False
    timer = 0
    healthfont = "oof"
    health_font = "oof"
    can_die = True


    def append(self, name):
        if name == "hero_idle_right":
            self.images = self.hir
            self.facing = "right"

        elif name == "hero_idle_left":
            self.images = self.hil
            self.facing = "left"

        elif name == "hero_walk_right":
            self.images = self.hwr
            self.facing = "right"

        elif name == "hero_walk_left":
            self.images = self.hwl
            self.facing = "left"

        elif name == "hero_jump":
            if self.facing == "right":
                self.images = self.hjump
            else:
                self.images = self.hfjump
            self.jumping = True
            self.touching_platform = False

        elif name == "hero_shoot":
            if self.can_shoot:
                if self.facing == "right":
                    self.images = self.hshoot
                    self.facing = "right"
                else:
                    self.images = self.hfshoot
                    self.facing = "left"

        elif name == "hero_hurt":
            if self.facing == "right":
                self.images = self.hhurt
            else:
                self.images = self.hfhurt
            if self.health < 0:
                self.health = 0

        elif name == "soldier_idle_right":
            self.images = self.sir
            self.facing = "right"

        elif name == "soldier_idle_left":
            self.images = self.sil
            self.facing = "left"

        elif name == "soldier_walk_right":
            self.images = self.swr
            self.facing = "right"

        elif name == "soldier_walk_left":
            self.images = self.swl
            self.facing = "left"

        elif name == "soldier_hurt":
            if self.facing == "right":
                self.images = self.shurt
            else:
                self.images = self.sfhurt
            if self.health < 0:
                self.health = 0

        elif name == "soldier_jump":
            if self.facing == "right":
                self.images = self.sjump
            else:
                self.images = self.sfjump
            self.jumping = True
            self.touching_platform = False

        elif name == "soldier_shoot":
            if self.can_shoot:
                if self.facing == "right":
                    self.images = self.sshoot
                    self.facing = "right"
                else:
                    self.images = self.sfshoot
                    self.facing = "left"

        elif name == "dead":
            self.images = self.dead
            self.can_move = False

    def __init__(self, char, x, y):
        #Hero Idle Right##############################################################
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\0.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\1.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\2.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\3.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\4.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\5.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\6.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\7.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\8.png").convert_alpha(), (self.w, self.h)))
        self.hir.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\9.png").convert_alpha(), (self.w, self.h)))
        #Hero Idle Left##############################################################
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\0.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\1.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\2.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\3.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\4.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\5.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\6.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\7.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\8.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\01-Idle\\9.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #Hero Walk Right##############################################################
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\0.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\1.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\2.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\3.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\4.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\5.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\6.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\7.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\8.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hwr.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\9.png").convert_alpha(),
                                   (self.w, self.h)))
        #Hero Walk Left##############################################################
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\0.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\1.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\2.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\3.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\4.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\5.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\6.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\7.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\8.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.hwl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\02-Run\\9.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #Hero Jump##############################################################
        self.hjump.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\05-Jump\\0.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hfjump.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\05-Jump\\0.png").convert_alpha(), True,
                                  False), (self.w, self.h)))
        #Hero Shoot##############################################################
        self.hshoot.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\03-Shot\\2.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hfshoot.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\03-Shot\\2.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #Hero Hurt##############################################################
        self.hhurt.append(
            pygame.transform.scale(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\04-Hurt\\3.png").convert_alpha(),
                                   (self.w, self.h)))
        self.hfhurt.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Hero-Guy-PNG\\_Mode-Gun\\04-Hurt\\3.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #Soldier Idle Right##############################################################
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\0.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\1.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\2.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\3.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\4.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\5.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\6.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\7.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\8.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sir.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\9.png").convert_alpha(),
                                   (self.w, self.h)))
        #Soldier Idle Left##############################################################
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\0.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\1.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\2.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\3.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\4.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\5.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\6.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\7.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\8.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.sil.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\01-Idle\\9.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #Soldier Walk Right##############################################################
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\0.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\1.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\2.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\3.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\4.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\5.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\6.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\7.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\8.png").convert_alpha(),
                                   (self.w, self.h)))
        self.swr.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\9.png").convert_alpha(),
                                   (self.w, self.h)))
        #soldier Walk Left##############################################################
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\0.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\1.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\2.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\3.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\4.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\5.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\6.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\7.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\8.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        self.swl.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\02-Run\\9.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #Soldier Hurt##############################################################
        self.shurt.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\04-Hurt\\3.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sfhurt.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\04-Hurt\\3.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #soldier Jump##############################################################
        self.sjump.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\05-Jump\\0.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sfjump.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\05-Jump\\0.png").convert_alpha(), True,
                                  False), (self.w, self.h)))
        #soldier Shoot##############################################################
        self.sshoot.append(
            pygame.transform.scale(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\03-Shot\\2.png").convert_alpha(),
                                   (self.w, self.h)))
        self.sfshoot.append(pygame.transform.scale(
            pygame.transform.flip(pygame.image.load("Soldier-Guy-PNG\\_Mode-Gun\\03-Shot\\2.png").convert_alpha(), True,
                                  False),
            (self.w, self.h)))
        #Dead##############################################################
        self.dead.append(pygame.transform.scale(pygame.image.load("tombstone.png").convert_alpha(), (self.w, self.h)))
        self.character = char
        self.prev_char = char
        self.x = x
        self.y = y
        super(Character, self).__init__()
        self.images = []
        self.append(char)
        self.index = 0
        #print(self.images)
        self.image = self.images[self.index]
        self.health_font = pygame.font.SysFont('Comic Sans MS', 10)

    def update(self):
        self.index += .02
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]
        if not self.touching_platform:
            self.falling = True
        if self.can_move:
            self.x += self.x_vel
            if self.jumping or self.falling:
                self.y_vel += self.gravity
                self.y += self.y_vel
                if self.y_vel > 1.25:
                    self.y_vel = 1.25
        if self.health < .10:
            self.health = 0
        if self.juiced:
            self.timer += 1
            self.can_shoot = True
        if self.timer > 2000:
            self.juiced = False
            self.timer = 0
        self.healthfont = self.health_font.render('{}'.format(math.floor(self.health * 100)) + "%", False, (255, 255, 255))

    def set_char(self, char):
        self.prev_char = self.character
        self.character = char
        self.images = []
        self.append(char)

    def draw(self, screen):
        screen.blit(self.images[int(math.floor(self.index))], (self.x, self.y, 50, 50))
        screen.blit(self.healthfont, (self.x + 15, self.y - 20))
        pygame.draw.rect(screen, self.red, (self.x, self.y - 5, 50, 5))
        if self.health > 0:
            if self.facing == "right":
                if self.juiced:
                    pygame.draw.rect(screen, self.yellow, (self.x, self.y - 5, 50 * self.health, 5))
                else:
                    pygame.draw.rect(screen, self.bar_color, (self.x, self.y - 5, 50 * self.health, 5))
            else:
                if self.juiced:
                    pygame.draw.rect(screen, self.yellow,
                                     (self.x + 50 - (50 * self.health), self.y - 5, 50 * self.health, 5))
                else:
                    pygame.draw.rect(screen, self.bar_color, (self.x + 50 - (50 * self.health), self.y - 5, 50 * self.health, 5))

    def is_touching_platform(self, platforms):
        for i in range(platforms.__len__()):
            plat = platforms[i]
            if self.facing == "right":
                if self.x + 30 >= plat.x and self.x + 10 <= plat.x + plat.w and self.y + 50 >= plat.y and self.y + 50 <= plat.y + plat.h:
                    return plat
            else:
                if self.x + 40 >= plat.x and self.x + 30 <= plat.x + plat.w and self.y + 50 >= plat.y and self.y + 50 <= plat.y + plat.h:
                    return plat
        return False