import pygame
from pygame.locals import *
from src.ab import *
from src.home import home
from src.tutorial import tutorial
from src.credits import credits

pygame.init()
pygame.display.set_caption("ALIEN ALARM")

game = True

while game:
    resp = 1
    click = home()
    if click[0] == 1:
        print("start")
    if click[0] == 2:
        resp = tutorial(click[1])
    if click[0] == 3:
        resp = credits(click[1])
    if click[0] == 0 or resp == 0:
        game = False
