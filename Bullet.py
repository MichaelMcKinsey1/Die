import pygame
import sys
from pygame.locals import *
import math
from Character import *


class Bullet:

    x = 0
    y = 0
    play = ""
    facing = "right"
    can_draw = False
    char = ""

    black = (0, 0, 0)

    def __init__(self, player, p):
        super(Bullet, self).__init__()
        self.play = player
        char = p
        if self.play == "":
            self.x = 0
            self.y = 0
        else:
            self.x = char.x + 48
            self.y = char.y + 30
            self.facing = char.facing

    def draw(self, screen):
        if self.can_draw:
            pygame.draw.circle(screen, self.black, (math.floor(self.x), math.floor(self.y)), 2)

    def update(self):
        if self.facing == "right":
            self.x += 3
        else:
            self.x -= 3