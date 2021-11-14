import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons

def tutorial(theme):
    PAGE = 1
    BG = Backgrounds(theme)

    previous = Buttons("previous", 520, 620)
    back = Buttons("back", 600, 620)
    next = Buttons("next", 680, 620)

    choice = True

    while choice:
        BACKGROUND = pygame.image.load(BG.bg_tutorial(PAGE))

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
                if PAGE > 1:
                    PAGE -= 1
            if e.type == pygame.MOUSEBUTTONUP and touching_next == 1:
                if PAGE < 3:
                    PAGE += 1
            if e.type == pygame.MOUSEBUTTONUP and touching_back == 1:
                resp = 1
                choice = False
            if e.type == pygame.QUIT:
                resp = 0
                choice = False

    return resp