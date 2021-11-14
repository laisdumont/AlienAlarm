import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons

THEME = "1"

def home():

    start = Buttons("start", 600, 350)
    tutorial = Buttons("tutorial", 600, 440)
    credits = Buttons("credits", 600, 530)
    exit = Buttons("exit", 600, 620)

    choice = True

    while choice:
        BG = Backgrounds(THEME)
        BACKGROUND = pygame.image.load(BG.bg_home())
        theme = Buttons(THEME, 1080, 50)

        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(BACKGROUND, (0, 0))

        pos = pygame.mouse.get_pos()
        pos_start = pos[0] - start.rect.x, pos[1] - start.rect.y
        pos_contols = pos[0] - credits.rect.x, pos[1] - credits.rect.y
        pos_tutorial = pos[0] - tutorial.rect.x, pos[1] - tutorial.rect.y
        pos_exit = pos[0] - exit.rect.x, pos[1] - exit.rect.y
        pos_theme = pos[0] - theme.rect.x, pos[1] - theme.rect.y


        touching_start = start.rect.collidepoint(*pos) and start.mask.get_at(pos_start)
        touching_credits = credits.rect.collidepoint(*pos) and credits.mask.get_at(pos_contols)
        touching_tutorial = tutorial.rect.collidepoint(*pos) and tutorial.mask.get_at(pos_tutorial)
        touching_exit = exit.rect.collidepoint(*pos) and exit.mask.get_at(pos_exit)
        touching_theme = theme.rect.collidepoint(*pos) and theme.mask.get_at(pos_theme)

        SCREEN.blit(start.image, start.rect)
        SCREEN.blit(credits.image, credits.rect)
        SCREEN.blit(tutorial.image, tutorial.rect)
        SCREEN.blit(exit.image, exit.rect)
        SCREEN.blit(theme.image, theme.rect)

        pygame.display.update()

        resp = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_start == 1:
                resp = 1
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_tutorial == 1:
                resp = 2
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_credits == 1:
                resp = 3
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_exit == 1:
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_theme == 1:
                global THEME
                if THEME == "1":
                    THEME = "2"
                else:
                    THEME = "1"
            if e.type == pygame.QUIT:
                choice = False

    return [resp, THEME]