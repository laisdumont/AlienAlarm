import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons 


class Start:
    def __init__(self, theme):
        bg = Backgrounds(theme)
        background = pygame.image.load(bg.bg_start())
        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(background, (0, 0))

    def actions(self, theme):
        clockwise = Buttons("clockwise{}".format(theme), 100, 100)
        add = Buttons("add{}".format(theme), 200, 100)
        anticlockwise = Buttons("anticlockwise{}".format(theme), 300, 100)
        left = Buttons("left{}".format(theme), 100, 300)
        down = Buttons("down{}".format(theme), 200, 300)
        right = Buttons("right{}".format(theme), 300, 300)

        pos = pygame.mouse.get_pos()
        pos_clockwise = pos[0] - clockwise.rect.x, pos[1] - clockwise.rect.y
        pos_contols = pos[0] - anticlockwise.rect.x, pos[1] - anticlockwise.rect.y
        pos_add = pos[0] - add.rect.x, pos[1] - add.rect.y
        pos_left = pos[0] - left.rect.x, pos[1] - left.rect.y
        pos_down = pos[0] - down.rect.x, pos[1] - down.rect.y
        pos_right = pos[0] - right.rect.x, pos[1] - right.rect.y

        touching_clockwise = clockwise.rect.collidepoint(*pos) and clockwise.mask.get_at(pos_clockwise)
        touching_anticlockwise = anticlockwise.rect.collidepoint(*pos) and anticlockwise.mask.get_at(pos_contols)
        touching_add = add.rect.collidepoint(*pos) and add.mask.get_at(pos_add)
        touching_left = left.rect.collidepoint(*pos) and left.mask.get_at(pos_left)
        touching_down = down.rect.collidepoint(*pos) and down.mask.get_at(pos_down)
        touching_right = right.rect.collidepoint(*pos) and right.mask.get_at(pos_right)

        SCREEN.blit(clockwise.image, clockwise.rect)
        SCREEN.blit(anticlockwise.image, anticlockwise.rect)
        SCREEN.blit(add.image, add.rect)
        SCREEN.blit(left.image, left.rect)
        SCREEN.blit(down.image, down.rect)
        SCREEN.blit(right.image, right.rect)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_clockwise == 1:
                print("clockwise")
            if e.type == pygame.MOUSEBUTTONUP and touching_add == 1:
                print("add")
            if e.type == pygame.MOUSEBUTTONUP and touching_anticlockwise == 1:
                print("anticlockwise")
            if e.type == pygame.MOUSEBUTTONUP and touching_left == 1:
                print("left")
            if e.type == pygame.MOUSEBUTTONUP and touching_down == 1:
                print("down")
            if e.type == pygame.MOUSEBUTTONUP and touching_right == 1:
                print("right")
            if e.type == pygame.QUIT:
                return False
    
    #def time(self):

    def discard(self):
        self.background = pygame.image.load(self.bg.bg_start())
        SCREEN.blit(self.background, (0, 0))
        