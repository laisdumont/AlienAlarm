import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons


def discards(theme):
    BG = Backgrounds(theme)

    discard = Buttons("discard{}".format(theme), 1044.5, 626)

    choice = True

    while choice:
        BACKGROUND = pygame.image.load(BG.bg_discard())

        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(BACKGROUND, (0, 0))

        pos = pygame.mouse.get_pos()
        pos_discard = pos[0] - discard.rect.x, pos[1] - discard.rect.y

        touching_discard = discard.rect.collidepoint(*pos) and discard.mask.get_at(pos_discard)

        SCREEN.blit(discard.image, discard.rect)

        pygame.display.update()

        resp = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_discard == 1:
                resp = 1
                choice = False
            if e.type == pygame.QUIT:
                resp = 0
                choice = False

    return resp