import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons

THEME = Backgrounds("2")
BACKGROUND = pygame.image.load(THEME.bg_home())


def home():
    start = Buttons("bot", 600, 340)
    controls = Buttons("bot", 600, 430)
    credits = Buttons("bot", 600, 520)
    exit = Buttons("bot", 600, 610)

    choice = True

    while choice:
        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(BACKGROUND, (0, 0))

        pos = pygame.mouse.get_pos()
        pos_start = pos[0] - start.rect.x, pos[1] - start.rect.y
        pos_contols = pos[0] - controls.rect.x, pos[1] - controls.rect.y
        pos_credits = pos[0] - credits.rect.x, pos[1] - credits.rect.y
        pos_exit = pos[0] - exit.rect.x, pos[1] - exit.rect.y

        touching_start = start.rect.collidepoint(*pos) and start.mask.get_at(pos_start)
        touching_controls = controls.rect.collidepoint(*pos) and controls.mask.get_at(pos_contols)
        touching_credits = credits.rect.collidepoint(*pos) and credits.mask.get_at(pos_credits)
        touching_exit = exit.rect.collidepoint(*pos) and exit.mask.get_at(pos_exit)

        SCREEN.blit(start.image, start.rect)
        SCREEN.blit(controls.image, controls.rect)
        SCREEN.blit(credits.image, credits.rect)
        SCREEN.blit(exit.image, exit.rect)

        pygame.display.update()

        resp = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_start == 1:
                resp = 1
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_controls == 1:
                resp = 2
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_credits == 1:
                resp = 3
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_exit == 1:
                choice = False
            if e.type == pygame.QUIT:
                choice = False

    return resp