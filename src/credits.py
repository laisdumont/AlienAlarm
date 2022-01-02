import pygame
import webbrowser
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons


def credits(theme):
    PAGE = 1
    BG = Backgrounds(theme)

    back = Buttons("back", 600, 620)
    bgPinheiro = Buttons("bgPinheiro", 1050, 620)

    choice = True

    while choice:
        BACKGROUND = pygame.image.load(BG.bg_credits())

        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(BACKGROUND, (0, 0))

        pos = pygame.mouse.get_pos()
        pos_back = pos[0] - back.rect.x, pos[1] - back.rect.y
        pos_bgPinheiro = pos[0] - bgPinheiro.rect.x, pos[1] - bgPinheiro.rect.y

        touching_back = back.rect.collidepoint(*pos) and back.mask.get_at(pos_back)
        touching_bgPinheiro = bgPinheiro.rect.collidepoint(*pos) and bgPinheiro.mask.get_at(pos_bgPinheiro)

        SCREEN.blit(back.image, back.rect)
        SCREEN.blit(bgPinheiro.image, bgPinheiro.rect)

        pygame.display.update()

        resp = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_back == 1:
                resp = 1
                choice = False
            if e.type == pygame.MOUSEBUTTONUP and touching_bgPinheiro == 1:
                new = 2

                site = "https://www.pinheirobg.com/index.php/portfolio/alien-alarm/"

                webbrowser.open(site, new=new)
            if e.type == pygame.QUIT:
                resp = 0
                choice = False

    return resp