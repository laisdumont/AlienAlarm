import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons

THEME = Backgrounds("1")
BACKGROUND = pygame.image.load(THEME.bg_home())


def controls():
    previous = Buttons("bot", 200, 600)
    next = Buttons("bot", 600, 600)
    back = Buttons("bot", 1000, 600)

    choice = True

    while choice:
        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(BACKGROUND, (0, 0))

        pos = pygame.mouse.get_pos()
        pos_previous = pos[0] - previous.rect.x, pos[1] - previous.rect.y
        pos_contols = pos[0] - next.rect.x, pos[1] - next.rect.y
        pos_back = pos[0] - back.rect.x, pos[1] - back.rect.y

        touching_previous = previous.rect.collidepoint(*pos) and previous.mask.get_at(pos_previous)
        touching_next = next.rect.collidepoint(*pos) and next.mask.get_at(pos_contols)
        touching_back = back.rect.collidepoint(*pos) and back.mask.get_at(pos_back)

        SCREEN.blit(previous.image, previous.rect)
        SCREEN.blit(next.image, next.rect)
        SCREEN.blit(back.image, back.rect)

        pygame.display.update()

        resp = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_previous == 1:
                resp = 1
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_next == 1:
                resp = 2
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_back == 1:
                choice = False
            if e.type == pygame.QUIT:
                choice = False

    return resp