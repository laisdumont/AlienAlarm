import pygame
from pygame.locals import *

class Backgrounds:
    def __init__(self, param):
        self.theme = param

    def bg_home(self):
        return "images/backgrounds/bg_home{}.png".format(self.theme)

    def bg_tutorial(self, page):
        return "images/backgrounds/bg_tutorial{}{}.png".format(page, self.theme)

    def bg_credits(self):
        return "images/backgrounds/bg_credits{}.png".format(self.theme)


class Buttons:
    def __init__(self, image, width, heignt):
        img = "images/buttons/{}.png".format(image)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(center=(width, heignt))
        self.mask = pygame.mask.from_surface(self.image)
