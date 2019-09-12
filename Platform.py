import pygame
import sys
from pygame.locals import *
import math
from Character import *


class Platform:

    white = (255, 255, 255)
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, screen, x_pos, y_pos, width):
        pygame.draw.rect(screen, self.white, (x_pos, y_pos, width, 7), )
        self.x = x_pos
        self.y = y_pos
        self.w = width
        self.h = 7