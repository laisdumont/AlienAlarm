from ab import *
from images.codes import Backgrounds
from time import sleep


def result(theme, res):
    BG = Backgrounds(theme)
    BACKGROUND = pygame.image.load(BG.bg_result(res))
    CLOCK.tick(FIXED_FPS)
    SCREEN.blit(BACKGROUND, (300, 175))
    pygame.display.update()
    sleep(5)
