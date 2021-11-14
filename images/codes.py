import pygame
from pygame.locals import *

class Images:
    def __init__(self, param):
        self.tema = param

    def bg(self):
        back = "images/backgrounds/bg_inicial{}.png".format(self.tema)
        return back


class Buttons:
    def __init__(self, image, heignt):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=(600, heignt))
        self.mask = pygame.mask.from_surface(self.image)
