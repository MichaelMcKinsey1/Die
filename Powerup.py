import pygame
import sys
from pygame.locals import *
import math
from Character import *
import random


class Powerup:

    x= 0
    y = 0
    w = 20
    h = 20
    collected = False
    timer = 0
    image = pygame.transform.scale(pygame.image.load("heart.png"), (w, h))
    can_draw = True

    def __init__(self):
        super(Powerup, self).__init__()
        self.x = 540
        self.y = 120

    def update(self):
        rand = 8000
        if self.collected:
            self.timer += 1
            self.can_draw = False
        if self.timer > rand:
            self.timer = 0
            self.can_draw = True
            self.collected = False
            self.x = random.randint(200, 880)
            self.y = random.randint(100, 620)

    def draw(self, screen):
        if self.can_draw:
            screen.blit(self.image, (self.x, self.y))