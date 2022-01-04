import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons
from time import sleep


BOARD = BOARD1
class Start:
    def __init__(self, theme):
        bg = Backgrounds(theme)
        background = pygame.image.load(bg.bg_start())
        CLOCK.tick(FIXED_FPS)
        SCREEN.blit(background, (0, 0))

    def pieces(self, theme, list1, list2, lv):
        level = Buttons("{}nv{}".format(theme, lv), 185, 60)
        piece1 = Buttons("pieces/{}piece{}{}".format(theme,
                         list1[0], list2[0]), 816, 95)
        piece2 = Buttons("pieces/{}piece{}{}".format(theme,
                         list1[1], list2[1]), 816, 225)
        piece3 = Buttons("pieces/{}piece{}{}".format(theme,
                         list1[2], list2[2]), 816, 355)
        piece4 = Buttons("pieces/{}piece{}{}".format(theme,
                         list1[3], list2[3]), 816, 485)
        piece5 = Buttons("pieces/{}piece{}{}".format(theme,
                         list1[4], list2[4]), 816, 615)

        SCREEN.blit(level.image, level.rect)
        SCREEN.blit(piece1.image, piece1.rect)
        SCREEN.blit(piece2.image, piece2.rect)
        SCREEN.blit(piece3.image, piece3.rect)
        SCREEN.blit(piece4.image, piece4.rect)
        SCREEN.blit(piece5.image, piece5.rect)

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

    def print_board(self, theme):
        for i in range(19):
            for j in range(14):
                pos_x = 262 + (j * 45)
                pos_y = 39 + (i * 45)
                if BOARD[i][j] == 1 and j > 3 and j < 10 and i < 15:
                    pieces = Buttons("{}p".format(theme), pos_x, pos_y)
                    SCREEN.blit(pieces.image, pieces.rect)
                    pygame.display.update()

    def less(self, algo, menor_anterior):
        mn = 30
        x = 0
        for i in range(6):
            for j in range(len(algo[i])):
                if algo[i][j] < mn and algo[i][j] > menor_anterior and len(algo[i]) > 0:
                    x = i
                    mn = algo[i][j]

        return x, mn

    def tam(self, actions):
        tam = 0

        for i in range(6):
            tam += len(actions[i])

        return tam

    def print_pieces(self, theme, card_img, card_rot, actions, lv, card_list):
        card = 0
        mni = 0
        st = 0
        pos_hr = 0
        sz = self.tam(actions)
        pc, pos_vt = self.matrices([card_img[card], card_rot[card]])
        dn = 0
        for i in range(sz):
            if card > 4 or not self.val():
                break
            Start(theme)
            self.action_cards(theme, actions[0], 100, 239)
            self.action_cards(theme, actions[1], 183, 239)
            self.action_cards(theme, actions[2], 264, 239)
            self.action_cards(theme, actions[3], 100, 511)
            self.action_cards(theme, actions[4], 183, 511)
            self.action_cards(theme, actions[5], 264, 511)
            self.total_card(theme, card_list)
            self.pieces(theme, card_img, card_rot, lv)
            self.print_board(theme)
            coord, mni = self.less(actions, mni)
            print(coord, mni, st)
            
            if coord == 0 and (st == 0 or st == 2):
                if st == 2 and dn == 1:
                    print(st, "escreveu")
                    self.write(pc, pos_hr, pos_vt)
                    pos_hr = 0
                    card += 1
                    dn = 0
                if card_rot[card] == 4:
                    card_rot[card] == 1
                elif card_rot[card] == 8:
                    card_rot[card] == 5
                else:
                    card_rot[card] += 1
                print(st, "rodou")
                self.pieces(theme, card_img, card_rot, lv)
                pc, pos_vt = self.matrices([card_img[card], card_rot[card]])
                st = 0
                continue

            elif coord == 1 and (st == 0 or st == 2):
                if st == 2 and dn == 1:
                    print(st, "escreveu")
                    self.write(pc, pos_hr, pos_vt)
                    pos_hr = 0
                    card += 1
                print(st, "entrou")
                self.print_pc(theme, pc, pos_hr, pos_vt)
                pc, pos_vt = self.matrices([card_img[card], card_rot[card]])
                st = 1
                continue

            elif coord == 2 and (st == 0 or st == 2):
                if st == 2 and dn == 1:
                    print(st, "escreveu")
                    self.write(pc, pos_hr, pos_vt)
                    pos_hr = 0
                    card += 1
                if card_rot[card] == 1:
                    card_rot[card] == 4
                elif card_rot[card] == 5:
                    card_rot[card] == 8
                else:
                    card_rot[card] -= 1
                print(st, "rodou")
                self.pieces(theme, card_img, card_rot, lv)
                pc, pos_vt = self.matrices([card_img[card], card_rot[card]])
                st = 0
                continue

            elif coord == 3 and (st == 1 or st == 2):
                print(st, "esquerda")
                vai = self.left(pc, pos_hr, pos_vt)
                print("vai:", vai)
                print(pos_vt)
                if vai:
                    pos_vt -= 1
                    y = pos_vt
                    self.print_pc(theme, pc, pos_hr, pos_vt)
                    pc, pos_vt = self.matrices([card_img[card], card_rot[card]])
                    pos_vt = y
                continue

            elif coord == 4 and st == 1:
                print(st, "desceu")
                sos = True
                while sos:
                    Start(theme)
                    self.action_cards(theme, actions[0], 100, 239)
                    self.action_cards(theme, actions[1], 183, 239)
                    self.action_cards(theme, actions[2], 264, 239)
                    self.action_cards(theme, actions[3], 100, 511)
                    self.action_cards(theme, actions[4], 183, 511)
                    self.action_cards(theme, actions[5], 264, 511)
                    self.pieces(theme, card_img, card_rot, lv)
                    self.total_card(theme, card_list)
                    self.print_board(theme)
                    pos_hr += 1
                    sos = self.down(pc, pos_hr, pos_vt)
                    if not sos:
                        break
                    self.print_pc(theme, pc, pos_hr, pos_vt)
                pos_hr -= 1
                st = 2
                dn = 1
                if i == (sz - 1):
                    print(st, "escreveu")
                    self.write(pc, pos_hr, pos_vt)
                    dn = 0
                continue

            elif coord == 5 and (st == 1 or st == 2):
                print(st, "direita")
                nvai = self.right(pc, pos_hr, pos_vt)
                print("nvai:", nvai)
                if nvai:
                    pos_vt += 1
                    y = pos_vt
                    self.print_pc(theme, pc, pos_hr, pos_vt)
                    pc, pos_vt = self.matrices([card_img[card], card_rot[card]])
                    pos_vt = y
                continue
        return

    def matrices(self, card):
        mat = []
        if card[0] == 1:
            if card[1] == 1 or card[1] == 3 or card[1] == 6 or card[1] == 8:
                mat = [[1, 0, 0, 0],
                       [1, 0, 0, 0],
                       [1, 0, 0, 0],
                       [1, 0, 0, 0]]
                if card[1] == 1 or card[1] == 3:
                    return mat, 6
                else:
                    return mat, 7
            else:
                mat = [[1, 1, 1, 1],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                if card[1] == 2 or card[1] == 5:
                    return mat, 5
                elif card[1] == 4:
                    return mat, 4
                else:
                    return mat, 6

        elif card[0] == 2:
            if card[1] == 1 or card[1] == 3:
                mat = [[0, 1, 0, 0],
                       [1, 1, 0, 0],
                       [1, 0, 0, 0],
                       [0, 0, 0, 0]]
                if card[1] == 1:
                    return mat, 5
                else:
                    return mat, 6
            elif card[1] == 2 or card[1] == 4:
                mat = [[1, 1, 0, 0],
                       [0, 1, 1, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 5
            elif card[1] == 5 or card[1] == 7:
                mat = [[1, 0, 0, 0],
                       [1, 1, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 0]]
                if card[1] == 5:
                    return mat, 7
                else:
                    return mat, 6
            else:
                mat = [[0, 1, 1, 0],
                       [1, 1, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 6

        elif card[0] == 3:
            mat = [[1, 1, 0, 0],
                   [1, 1, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
            if card[1] == 1 or card[1] == 2 or card[1] == 7 or card[1] == 8:
                return mat, 6
            if card[1] == 3 or card[1] == 4:
                return mat, 5
            else:
                return mat, 7

        elif card[0] == 4:
            if card[1] == 1 or card[1] == 5:
                mat = [[0, 1, 0, 0],
                       [1, 1, 1, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                if card[1] == 1:
                    return mat, 5
                else:
                    return mat, 6
            if card[1] == 2 or card[1] == 6:
                mat = [[1, 0, 0, 0],
                       [1, 1, 0, 0],
                       [1, 0, 0, 0],
                       [0, 0, 0, 0]]
                if card[1] == 2:
                    return mat, 6
                else:
                    return mat, 7
            if card[1] == 3 or card[1] == 7:
                mat = [[1, 1, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                if card[1] == 3:
                    return mat, 5
                else:
                    return mat, 6
            else:
                mat = [[0, 1, 0, 0],
                       [1, 1, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 0]]
                if card[1] == 4:
                    return mat, 5
                else:
                    return mat, 6

        else:
            if card[1] == 1:
                mat = [[0, 0, 1, 0],
                       [1, 1, 1, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 4
            elif card[1] == 2:
                mat = [[1, 0, 0, 0],
                       [1, 0, 0, 0],
                       [1, 1, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 6
            elif card[1] == 3:
                mat = [[1, 1, 1, 0],
                       [1, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 5
            elif card[1] == 4:
                mat = [[1, 1, 0, 0],
                       [0, 1, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 5
            elif card[1] == 5:
                mat = [[1, 0, 0, 0],
                       [1, 1, 1, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 7
            elif card[1] == 6:
                mat = [[1, 1, 0, 0],
                       [1, 0, 0, 0],
                       [1, 0, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 7
            elif card[1] == 7:
                mat = [[1, 1, 1, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 5
            else:
                mat = [[0, 1, 0, 0],
                       [0, 1, 0, 0],
                       [1, 1, 0, 0],
                       [0, 0, 0, 0]]
                return mat, 6

    def down(self, mat_pc, x, y):
        for i in range(4):
            for j in range(4):
                if mat_pc[i][j] == 1 and BOARD[x+i][y+j] == 1:
                    return False

        return True

    def left(self, mat, x, y):
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 1 and BOARD[x][y+4] == 1:
                    return False
        return True

    def right(self, mat, x, y):
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 1 and BOARD[x][y+j+1] == 1:
                    return False
        return True

    def print_pc(self, theme, mat, x, y):
        pygame.display.update()

        self.print_board(theme)
        for k in range(0, 4):
            for m in range(0, 4):
                pos_x = 262 + ((k + y) * 45)
                pos_y = 39 + ((m + x) * 45)
                if mat[m][k] == 1:
                    pieces = Buttons("{}p".format(theme), pos_x, pos_y)
                    SCREEN.blit(pieces.image, pieces.rect)
                    pygame.display.update()

    def write(self, mat, x, y):
        global BOARD
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 1:
                    BOARD[x+i][y + j] = 1

    def validate(self, level):
        c = 0
        for i in range(19):
            for j in range(14):
                if BOARD[i][j] == 0 and i < 14:
                    c += 1
                    break
        x = 14 - c
        print(x)
        if (x) >= (level * 2):
            return True
        else:
            return False

    def total_card(self, theme, card_list):
        discard = Buttons("discard{}".format(theme), 1046, 626)
        card1 = Buttons("card{}{}".format(theme, card_list[-1]), 1046, 152)
        card2 = Buttons("card{}{}".format(theme, card_list[-2]), 1046, 210)
        card3 = Buttons("card{}{}".format(theme, card_list[-3]), 1046, 267)
        card4 = Buttons("card{}{}".format(theme, card_list[-4]), 1046, 324)
        card5 = Buttons("card{}{}".format(theme, card_list[-5]), 1046, 380)
        card6 = Buttons("card{}{}".format(theme, card_list[-6]), 1046, 437)
        card7 = Buttons("card{}{}".format(theme, card_list[-7]), 1046, 494)
        card8 = Buttons("card{}{}".format(theme, card_list[-8]), 1046, 552)

        SCREEN.blit(discard.image, discard.rect)
        SCREEN.blit(card1.image, card1.rect)
        SCREEN.blit(card2.image, card2.rect)
        SCREEN.blit(card3.image, card3.rect)
        SCREEN.blit(card4.image, card4.rect)
        SCREEN.blit(card5.image, card5.rect)
        SCREEN.blit(card6.image, card6.rect)
        SCREEN.blit(card7.image, card7.rect)
        SCREEN.blit(card8.image, card8.rect)
    
    def val(self):
        for i in range(len(BOARD[0])):
            if BOARD[0][i] == 1 and i > 3 and i < 10:
                return False
        return True