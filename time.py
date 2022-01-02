import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 20, '08:00'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            min = counter//60
            sec = counter%60
            text = "0{}:{}".format(min, sec) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)