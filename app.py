import pygame
from pygame.locals import *
from src.ab import *
from src.home import home

pygame.init()
pygame.display.set_caption("ALIEN ALARM")

game = True

while game:
    game = home()
    if game == 1:
        print("start")
    if game == 2:
        print("controles")
