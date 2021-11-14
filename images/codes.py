import pygame
from pygame.locals import *

class Backgrounds:
    def __init__(self, param):
        self.tema = param

    def bg_home(self):
        return "images/backgrounds/bg_home{}.png".format(self.tema)

    def bg_controls(self, page):
        return "images/backgrounds/bg_controls{}{}.png".format(page, self.tema)
    
    def bg_credits(self):
        return "images/backgrounds/bg_credits{}.png".format(self.tema)


class Buttons:
    def __init__(self, image, width, heignt):
        img = "images/backgrounds/{}.png".format(image)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(center=(width, heignt))
        self.mask = pygame.mask.from_surface(self.image)
