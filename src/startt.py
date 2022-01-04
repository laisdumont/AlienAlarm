import pygame
from pygame.locals import *
from ab import *
from images.codes import Buttons
from src.start_functions import BOARD, Start
from random import shuffle
from end import *


def start(theme, level):
    choice = True
    global BOARD
    BOARD = BOARD1
    while choice:
        play = Start(theme)
        play.print_board(theme)

        card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        shuffle(card_list)

        card_img = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        card_rot = [1, 2, 3, 4, 5, 6, 8]
        # shuffle(card_img)
        # shuffle(card_rot)

        list_clockwise = []
        list_add = []
        list_anticlockwise = []
        list_left = []
        list_down = []
        list_right = []
        list_discard = []
        y = 0
        while choice:
            play.pieces(theme, card_img, card_rot, level)
            lc = Buttons("{}nv{}".format(theme, level), 185, 60)

            actions = [list_clockwise, list_add, list_anticlockwise,
                        list_left, list_down, list_right]

            clockwise = Buttons("clockwise{}".format(theme), 100, 181)
            add = Buttons("add{}".format(theme), 182, 181)
            anticlockwise = Buttons("anticlockwise{}".format(theme), 264, 181)
            left = Buttons("left{}".format(theme), 100, 457)
            down = Buttons("down{}".format(theme), 182, 457)
            right = Buttons("right{}".format(theme), 264, 457)
            discard = Buttons("discard{}".format(theme), 1046, 626)
            card1 = Buttons("card{}{}".format(theme, card_list[-1]), 1046, 152)
            card2 = Buttons("card{}{}".format(theme, card_list[-2]), 1046, 210)
            card3 = Buttons("card{}{}".format(theme, card_list[-3]), 1046, 267)
            card4 = Buttons("card{}{}".format(theme, card_list[-4]), 1046, 324)
            card5 = Buttons("card{}{}".format(theme, card_list[-5]), 1046, 380)
            card6 = Buttons("card{}{}".format(theme, card_list[-6]), 1046, 437)
            card7 = Buttons("card{}{}".format(theme, card_list[-7]), 1046, 494)
            card8 = Buttons("card{}{}".format(theme, card_list[-8]), 1046, 552)

            pos = pygame.mouse.get_pos()
            pos_lc = pos[0] - lc.rect.x, pos[1] - lc.rect.y
            pos_clockwise = pos[0] - clockwise.rect.x, pos[1] - clockwise.rect.y
            pos_anticlockwise = pos[0] - anticlockwise.rect.x, pos[1] - anticlockwise.rect.y
            pos_add = pos[0] - add.rect.x, pos[1] - add.rect.y
            pos_left = pos[0] - left.rect.x, pos[1] - left.rect.y
            pos_down = pos[0] - down.rect.x, pos[1] - down.rect.y
            pos_right = pos[0] - right.rect.x, pos[1] - right.rect.y
            pos_discard = pos[0] - discard.rect.x, pos[1] - discard.rect.y
            pos_card1 = pos[0] - card1.rect.x, pos[1] - card1.rect.y
            pos_card2 = pos[0] - card2.rect.x, pos[1] - card2.rect.y
            pos_card3 = pos[0] - card3.rect.x, pos[1] - card3.rect.y
            pos_card4 = pos[0] - card4.rect.x, pos[1] - card4.rect.y
            pos_card5 = pos[0] - card5.rect.x, pos[1] - card5.rect.y
            pos_card6 = pos[0] - card6.rect.x, pos[1] - card6.rect.y
            pos_card7 = pos[0] - card7.rect.x, pos[1] - card7.rect.y
            pos_card8 = pos[0] - card8.rect.x, pos[1] - card8.rect.y
        
            touching_lc = lc.rect.collidepoint(*pos) and lc.mask.get_at(pos_lc)
            touching_clockwise = clockwise.rect.collidepoint(*pos) and clockwise.mask.get_at(pos_clockwise)
            touching_anticlockwise = anticlockwise.rect.collidepoint(*pos) and anticlockwise.mask.get_at(pos_anticlockwise)
            touching_add = add.rect.collidepoint(*pos) and add.mask.get_at(pos_add)
            touching_left = left.rect.collidepoint(*pos) and left.mask.get_at(pos_left)
            touching_down = down.rect.collidepoint(*pos) and down.mask.get_at(pos_down)
            touching_right = right.rect.collidepoint(*pos) and right.mask.get_at(pos_right)
            touching_discard = discard.rect.collidepoint(*pos) and discard.mask.get_at(pos_discard)
            touching_card1 = card1.rect.collidepoint(*pos) and card1.mask.get_at(pos_card1)
            touching_card2 = card2.rect.collidepoint(*pos) and card2.mask.get_at(pos_card2)
            touching_card3 = card3.rect.collidepoint(*pos) and card3.mask.get_at(pos_card3)
            touching_card4 = card4.rect.collidepoint(*pos) and card4.mask.get_at(pos_card4)
            touching_card5 = card5.rect.collidepoint(*pos) and card5.mask.get_at(pos_card5)
            touching_card6 = card6.rect.collidepoint(*pos) and card6.mask.get_at(pos_card6)
            touching_card7 = card7.rect.collidepoint(*pos) and card7.mask.get_at(pos_card7)
            touching_card8 = card8.rect.collidepoint(*pos) and card8.mask.get_at(pos_card8)

            SCREEN.blit(lc.image, lc.rect)
            SCREEN.blit(clockwise.image, clockwise.rect)
            SCREEN.blit(anticlockwise.image, anticlockwise.rect)
            SCREEN.blit(add.image, add.rect)
            SCREEN.blit(left.image, left.rect)
            SCREEN.blit(down.image, down.rect)
            SCREEN.blit(right.image, right.rect)
            SCREEN.blit(discard.image, discard.rect)
            SCREEN.blit(card1.image, card1.rect)
            SCREEN.blit(card2.image, card2.rect)
            SCREEN.blit(card3.image, card3.rect)
            SCREEN.blit(card4.image, card4.rect)
            SCREEN.blit(card5.image, card5.rect)
            SCREEN.blit(card6.image, card6.rect)
            SCREEN.blit(card7.image, card7.rect)
            SCREEN.blit(card8.image, card8.rect)

            play.action_cards(theme, list_clockwise, 100, 239)
            play.action_cards(theme, list_add, 183, 239)
            play.action_cards(theme, list_anticlockwise, 264, 239)
            play.action_cards(theme, list_left, 100, 511)
            play.action_cards(theme, list_down, 183, 511)
            play.action_cards(theme, list_right, 264, 511)
            
            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP and touching_card1 == 1 and card_list[-1] != 0:
                    x = -1
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_card2 == 1 and card_list[-2] != 0:
                    x = -2
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_card3 == 1 and card_list[-3] != 0:
                    x = -3
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_card4 == 1 and card_list[-4] != 0:
                    x = -4
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_card5 == 1 and card_list[-5] != 0:
                    x = -5
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_card6 == 1 and card_list[-6] != 0:
                    x = -6
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_card7 == 1 and card_list[-7] != 0:
                    x = -7
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_card8 == 1 and card_list[-8] != 0:
                    x = -8
                    y = 1
                if e.type == pygame.MOUSEBUTTONUP and touching_clockwise == 1 and y == 1:
                    list_clockwise.append(card_list[x])
                    del card_list[x]
                    list_clockwise.sort()
                    y = 0
                if e.type == pygame.MOUSEBUTTONUP and touching_add == 1 and y == 1:
                    list_add.append(card_list[x])
                    list_add.sort()
                    del card_list[x]
                    y = 0
                if e.type == pygame.MOUSEBUTTONUP and touching_anticlockwise == 1 and y == 1:
                    list_anticlockwise.append(card_list[x])
                    del card_list[x]
                    list_anticlockwise.sort()
                    y = 0
                if e.type == pygame.MOUSEBUTTONUP and touching_left == 1 and y == 1:
                    list_left.append(card_list[x])
                    del card_list[x]
                    list_left.sort()
                    y = 0
                if e.type == pygame.MOUSEBUTTONUP and touching_down == 1 and y == 1:
                    list_down.append(card_list[x])
                    del card_list[x]
                    list_down.sort()
                    y = 0
                if e.type == pygame.MOUSEBUTTONUP and touching_right == 1 and y == 1:
                    list_right.append(card_list[x])
                    del card_list[x]
                    list_right.sort()
                    y = 0
                if e.type == pygame.MOUSEBUTTONUP and touching_discard == 1 and y == 1:
                    list_discard.append(card_list[x])
                    del card_list[x]
                    y = 0
                elif e.type == pygame.MOUSEBUTTONUP and touching_discard == 1:
                    play.discards(theme, list_discard)
                if e.type == pygame.QUIT:
                    pygame.quit()
                    choice = False
                if e.type == pygame.MOUSEBUTTONUP and touching_lc == 1:
                    choice = False
            if len(card_list) < 8:
                card_list.insert(0, 0)
        
        choice = True
        
        play.print_board(theme)
        # actions = [list_clockwise, list_add, list_anticlockwise,
        #             list_left, list_down, list_right]
        actions = [[1, 16], [2, 5, 9, 11, 17], [],
                    [3, 18, 19, 20], [4, 8, 10, 15, 21],
                    [6, 7, 12, 13, 14]]
        play.pieces(theme, card_img, card_rot, level)
        play.print_pieces(theme, card_img, card_rot, actions, level, card_list)
        play.print_board(theme)
        
        choice = play.validate(level)
        level += 3
        if not choice:
            result(theme, 2)
            pygame.quit()
        elif level < 3 and choice:
            result(theme, 3)
        elif level >= 4:
            result(theme, 1)
            pygame.quit()
        
        for e in pygame.event.get():
            
            if e.type == pygame.QUIT:
                pygame.quit()
                choice = False

    return level
