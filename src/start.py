import pygame
from pygame.locals import *
from ab import *
from discards import discards
from images.codes import Backgrounds, Buttons
from src.start_functions import Start


def start(theme):
    discard = Buttons("discard{}".format(theme), 1044.5, 626)
    choice = True

    while choice:
        bg = pygame.image.load(
            "images/backgrounds/start{}.png".format(theme))
        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(bg, (0, 0))

        pos = pygame.mouse.get_pos()
        pos_discard = pos[0] - discard.rect.x, pos[1] - discard.rect.y

        touching_discard = discard.rect.collidepoint(*pos) and discard.mask.get_at(pos_discard)

        SCREEN.blit(discard.image, discard.rect)

        """up = Start(theme)
        algo = up.actions(theme)
        if algo == False:
            choice = False"""
        pygame.display.update()

        resp = 1

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_discard == 1:
                choice = discards(theme)
            elif e.type == pygame.MOUSEBUTTONUP:
                choice = False
            if e.type == pygame.QUIT:
                resp = 0
                choice = False

    return resp
