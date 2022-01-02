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
        clockwise = Buttons("clockwise{}".format(theme), 100, 181)
        add = Buttons("add{}".format(theme), 182, 181)
        anticlockwise = Buttons("anticlockwise{}".format(theme), 264, 181)
        left = Buttons("left{}".format(theme), 100, 457)
        down = Buttons("down{}".format(theme), 182, 457)
        right = Buttons("right{}".format(theme), 264, 457)
        discard = Buttons("discard{}".format(theme), 1046, 626)

        pos = pygame.mouse.get_pos()
        pos_clockwise = pos[0] - clockwise.rect.x, pos[1] - clockwise.rect.y
        pos_contols = pos[0] - \
            anticlockwise.rect.x, pos[1] - anticlockwise.rect.y
        pos_add = pos[0] - add.rect.x, pos[1] - add.rect.y
        pos_left = pos[0] - left.rect.x, pos[1] - left.rect.y
        pos_down = pos[0] - down.rect.x, pos[1] - down.rect.y
        pos_right = pos[0] - right.rect.x, pos[1] - right.rect.y
        pos_discard = pos[0] - discard.rect.x, pos[1] - discard.rect.y

        touching_clockwise = clockwise.rect.collidepoint(
            *pos) and clockwise.mask.get_at(pos_clockwise)
        touching_anticlockwise = anticlockwise.rect.collidepoint(
            *pos) and anticlockwise.mask.get_at(pos_contols)
        touching_add = add.rect.collidepoint(*pos) and add.mask.get_at(pos_add)
        touching_left = left.rect.collidepoint(
            *pos) and left.mask.get_at(pos_left)
        touching_down = down.rect.collidepoint(
            *pos) and down.mask.get_at(pos_down)
        touching_right = right.rect.collidepoint(
            *pos) and right.mask.get_at(pos_right)
        touching_discard = discard.rect.collidepoint(
            *pos) and discard.mask.get_at(pos_discard)

        SCREEN.blit(clockwise.image, clockwise.rect)
        SCREEN.blit(anticlockwise.image, anticlockwise.rect)
        SCREEN.blit(add.image, add.rect)
        SCREEN.blit(left.image, left.rect)
        SCREEN.blit(down.image, down.rect)
        SCREEN.blit(right.image, right.rect)
        SCREEN.blit(discard.image, discard.rect)

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and touching_clockwise == 1:
                print("card1")
            elif e.type == pygame.MOUSEBUTTONUP and touching_add == 1:
                print("card2")
            elif e.type == pygame.MOUSEBUTTONUP and touching_anticlockwise == 1:
                print("card3")
            elif e.type == pygame.MOUSEBUTTONUP and touching_left == 1:
                print("card4")
            elif e.type == pygame.MOUSEBUTTONUP and touching_down == 1:
                print("card5")
            elif e.type == pygame.MOUSEBUTTONUP and touching_right == 1:
                print("card6")
            elif e.type == pygame.MOUSEBUTTONUP and touching_discard == 1:
                self.discards(theme)
            elif e.type == pygame.QUIT:
                pygame.quit()
            else:
                return False

    # def time(self):

    def pieces(self, theme, list1, list2):
        piece1 = Buttons("pieces/{}piece{}{}".format(theme, list1[0], list2[0]), 816, 95)
        piece2 = Buttons("pieces/{}piece{}{}".format(theme, list1[1], list2[1]), 816, 225)
        piece3 = Buttons("pieces/{}piece{}{}".format(theme, list1[2], list2[2]), 816, 355)
        piece4 = Buttons("pieces/{}piece{}{}".format(theme, list1[3], list2[3]), 816, 485)
        piece5 = Buttons("pieces/{}piece{}{}".format(theme, list1[4], list2[4]), 816, 615)

        SCREEN.blit(piece1.image, piece1.rect)
        SCREEN.blit(piece2.image, piece2.rect)
        SCREEN.blit(piece3.image, piece3.rect)
        SCREEN.blit(piece4.image, piece4.rect)
        SCREEN.blit(piece5.image, piece5.rect)
        pygame.display.update()


    def discards(self, theme, discard_list):
        BG = Backgrounds(theme)

        discard = Buttons("discard{}".format(theme), 1046, 626)

        choice = True
        while choice:
            BACKGROUND = pygame.image.load(BG.bg_discard())

            CLOCK.tick(FIXED_FPS)
            SCREEN.blit(BACKGROUND, (0, 0))
            self.discard_cards(theme, discard_list)

            pos = pygame.mouse.get_pos()
            pos_discard = pos[0] - discard.rect.x, pos[1] - discard.rect.y

            touching_discard = discard.rect.collidepoint(
                *pos) and discard.mask.get_at(pos_discard)

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

    def discard_cards(self, theme, discard_list):
        if len(discard_list) > 0:
            discard_list = sorted(discard_list, key=int)
            x = 200
            y = 200
            for i in range(len(discard_list)):
                bt = Buttons("card{}{}".format(theme, discard_list[i]), x, y)
                pos = pygame.mouse.get_pos()
                pos_bt = pos[0] - bt.rect.x, pos[1] - bt.rect.y
                touching_bt = bt.rect.collidepoint(
                    *pos) and bt.mask.get_at(pos_bt)
                SCREEN.blit(bt.image, bt.rect)
                x += 100
                if x > 700:
                    x = 200
                    y += 100

    def action_cards(self, theme, list_cards, x, y):
        if len(list_cards) > 0:
            for i in list_cards:
                bt = Buttons("action_card{}{}".format(theme, i), x, y)
                SCREEN.blit(bt.image, bt.rect)

                y = y + 30

    def print_board(self, board, theme):
        pos_y = 39
        for i in range(16):
            for j in range(8):
                if j == 0:
                    pos_x = 397
                if board[i][j] == 1 and j != 0 and i != 15 and j != 7:
                    pieces = Buttons("{}p".format(theme), pos_x, pos_y)
                    SCREEN.blit(pieces.image, pieces.rect)
                    pygame.display.update()
                pos_x += 45

            pos_y += 45

    def print_pieces(self, theme, list1, list2):
        self.pieces(theme, list1, list2)
        
