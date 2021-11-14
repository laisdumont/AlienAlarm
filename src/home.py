import pygame
from pygame.locals import *
from ab import *
from images.codes import Images, Buttons

THEME = Images("1")
BACKGROUND = pygame.image.load(THEME.bg())


def home():
    start = Buttons("images/backgrounds/bot.png", 370)
    controls = Buttons("images/backgrounds/bot.png", 485)
    exit = Buttons("images/backgrounds/bot.png", 600)

    choice = True

    while choice:
        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(BACKGROUND, (0, 0))

        pos = pygame.mouse.get_pos()
        pos_start = pos[0] - start.rect.x, pos[1] - start.rect.y
        pos_contols = pos[0] - controls.rect.x, pos[1] - controls.rect.y
        pos_exit = pos[0] - exit.rect.x, pos[1] - exit.rect.y

        touching_start = start.rect.collidepoint(*pos) and start.mask.get_at(pos_start)
        touching_controls = controls.rect.collidepoint(*pos) and controls.mask.get_at(pos_contols)
        touching_exit = exit.rect.collidepoint(*pos) and exit.mask.get_at(pos_exit)

        SCREEN.blit(start.image, start.rect)
        SCREEN.blit(controls.image, controls.rect)
        SCREEN.blit(exit.image, exit.rect)

        pygame.display.update()

        resp = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_start == 1:
                resp = 1
                choice = False
                print("clicoustart")
            if e.type == pygame.MOUSEBUTTONUP and touching_controls == 1:
                resp = 2
                choice = False
                print("clicoucontrols")
            if e.type == pygame.MOUSEBUTTONUP and touching_exit == 1:
                choice = False
                print("clicouexit")
            if e.type == pygame.QUIT:
                choice = False

    return resp