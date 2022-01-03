import pygame
from pygame.locals import *
from ab import *
from images.codes import Backgrounds, Buttons
from time import sleep


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

    def print_board(self, theme):
        pos_y = 39
        for i in range(16):
            for j in range(8):
                if j == 0:
                    pos_x = 397
                if BOARD[i][j] == 1 and j != 0 and i != 15 and j != 7:
                    pieces = Buttons("{}p".format(theme), pos_x, pos_y)
                    SCREEN.blit(pieces.image, pieces.rect)
                    pygame.display.update()
                pos_x += 45

            pos_y += 45

    def less(self, actions, mx):
        mn = 30
        x = 0
        for i in range(6):
            for j in range(len(actions[i])):
                if actions[i][j] < mn and actions[i][j] != 0 and actions[i][j] > mx:
                    mn = actions[i][j]
                    x = i
        return [x, mn]

    def naguentomais(self, actions, mx):
        if mx == 30:
            return False

        algo = 0
        for i in range(6):
            for j in range(len(actions[i])):
                if actions[i][j] > mx:
                    algo = 1
        print(mx)
     
        if algo == 0:
            return False
        else:
            return True

    def print_pieces(self, theme, card_img, card_rot, actions):
        resp = True
        mx = 0
        less, mx = self.less(actions, mx)
        global BOARD
        st = 0
        card = 0
        pc, pos_vt= self.matrices([card_img[card], card_rot[card]])
        pos_hr = 0
        while(resp):
            self.pieces(theme, card_img, card_rot)

            if st == 3 and (less == 0 or less == 1 or less == 2):
                print("encaixou")
                self.write(pc, pos_hr, pos_vt)
                card += 1
                resp = self.naguentomais(actions, mx)
                if resp:
                    less, mx = self.less(actions, mx)
                    st == 0
                    pc, pos_vt = self.matrices([card_img[card], card_rot[card]])
                    pos_hr = 0
                    v = 0
                print(card_img[card], card_rot[card])
                Start(theme)
                self.pieces(theme, card_img, card_rot)
                self.print_board(theme)
                
            if st == 0 and (less == 0 or less == 1 or less == 2):
                if less == 0:
                    print("girou")
                    if card_rot[card] == 4:
                        card_rot[card] == 1
                    elif card_rot[card] == 8:
                        card_rot[card] == 5
                    else:
                        card_rot[card] += 1
                    resp = self.naguentomais(actions, mx)
                    if resp:
                        less, mx = self.less(actions, mx)
                    self.pieces(theme, card_img, card_rot)

                elif less == 1:
                    print("adicionou")
                    st = 1
                    self.print_pc(theme, pc, pos_hr, pos_vt)
                    print(pos_hr, pos_vt)
                    resp = self.naguentomais(actions, mx)
                    if resp:
                        less, mx = self.less(actions, mx)
                    v = 1

                else:
                    print("girou")
                    if card_rot[card] == 1:
                        card_rot[card] == 4
                    elif card_rot[card] == 5:
                        card_rot[card] == 8
                    else:
                        card_rot[card] -= 1
                    resp = self.naguentomais(actions, mx)
                    if resp:
                        less, mx = self.less(actions, mx)
                    self.pieces(theme, card_img, card_rot)

            if (st == 1 or st == 3) and (less == 3 or less == 5):
                Start(theme)
                self.pieces(theme, card_img, card_rot)
                self.print_board(theme)

                if less == 3:
                    print("esquerda")
                    vai = self.left(pc, pos_hr, pos_vt)
                    if vai and v == 1:
                        pos_vt -= 1
                        self.print_pc(theme, pc, pos_hr, pos_vt)
                    print(pos_hr, pos_vt)

                else:
                    print("direita")
                    nvai = self.right(pc, pos_hr, pos_vt)
                    if nvai and v == 1:
                        pos_vt += 1
                        self.print_pc(theme, pc, pos_hr, pos_vt)
                    print(pos_hr, pos_vt)
                
                resp = self.naguentomais(actions, mx)
                if resp:
                    less, mx = self.less(actions, mx)

            if st == 1 and less == 4 and v == 1:
                print("desceu")
                if st == 1:
                    sos = True
                    while sos:
                        Start(theme)
                        self.pieces(theme, card_img, card_rot)
                        self.print_board(theme)
                        pos_hr += 1
                        sos = self.down(pc, pos_hr, pos_vt)
                        if not sos:
                            break
                        self.print_pc(theme, pc, pos_hr, pos_vt)
                        print(pos_hr, pos_vt)
                    pos_hr -= 1
                resp = self.naguentomais(actions, mx)
                if resp:
                    less, mx = self.less(actions, mx)
                st = 3

            if st == 3 and less == 4:
                resp = self.naguentomais(actions, mx)
                if resp:
                    less, mx = self.less(actions, mx)
                    
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
                    return mat, 3
                else:
                    return mat, 4
            else:
                mat = [[1, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                if card[1] == 2 or card[1] == 5:
                    return mat, 2
                elif card[1] == 4:
                    return mat, 1
                else:
                    return mat, 3

        elif card[0] == 2:
            if card[1] == 1 or card[1] == 3:
                mat = [[0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0]]
                if card[1] == 1:
                    return mat, 2
                else:
                    return mat, 3
            elif card[1] == 2 or card[1] == 4:
                mat = [[1, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 2
            elif card[1] == 5 or card[1] == 7:
                mat = [[1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]]
                if card[1] == 5:
                    return mat, 4
                else:
                    return mat, 3
            else:
                mat = [[0, 1, 1, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 3

        elif card[0] == 3:
            mat = [[1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
            if card[1] == 1 or card[1] == 2 or card[1] == 7 or card[1] == 8:
                return mat, 3
            if card[1] == 3 or card[1] == 4:
                return mat, 2
            else:
                return mat, 4

        elif card[0] == 4:
            if card[1] == 1 or card[1] == 5:
                mat = [[0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                if card[1] == 1:
                    return mat, 2
                else:
                    return mat, 3
            if card[1] == 2 or card[1] == 6:
                mat = [[1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0]]
                if card[1] == 2:
                    return mat, 3
                else:
                    return mat, 4
            if card[1] == 3 or card[1] == 7:
                mat = [[1, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                if card[1] == 3:
                    return mat, 2
                else:
                    return mat, 3
            else:
                mat = [[0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]]
                if card[1] == 4:
                    return mat, 2
                else:
                    return mat, 3

        else:
            if card[1] == 1:
                mat = [[0, 0, 1, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 1
            elif card[1] == 2:
                mat = [[1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 3
            elif card[1] == 3:
                mat = [[1, 1, 1, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 3
            elif card[1] == 4:
                mat = [[1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 2
            elif card[1] == 5:
                mat = [[1, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 4
            elif card[1] == 6:
                mat = [[1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 4
            elif card[1] == 7:
                mat = [[1, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 2
            else:
                mat = [[0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0]]
                return mat, 3
    
    def down(self, mat_pc, x, y):
        for i in range(4):
            for j in range(4):
                if mat_pc[i][j] == 1 and BOARD[x+i][y+j] == 1:
                    return False
        
        return True
    
    def left(self, mat, x, y):
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 1 and BOARD[x - 1][y] == 1:
                    return False
        return True

    def right(self, mat, x, y):
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 1 and BOARD[x + 1][y] == 1:
                    return False
        return True

    def print_pc(self, theme, mat, x, y):
        pygame.display.update()

        self.print_board(theme)
        for k in range(0, 4):
            for m in range(0, 4):
                pos_x = 397 + ((k + y) * 45)
                pos_y = 39 + ((m + x) * 45)
                if mat[m][k] == 1:
                    pieces = Buttons("{}p".format(theme), pos_x, pos_y)
                    SCREEN.blit(pieces.image, pieces.rect)
                    pygame.display.update()
        sleep(1)

    def write(self, mat, x, y):
        global BOARD
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 1:
                    BOARD[x + i][y + j] = 1
