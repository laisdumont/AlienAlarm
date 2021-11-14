import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

class Cat:
    def __init__(self, image, heignt):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=(400, heignt))
        self.mask = pygame.mask.from_surface(self.image)


running = True
cat = Cat("images/backgrounds/bot.png", 300)
bat = Cat("images/backgrounds/bot.png", 400)

while running:
    pos = pygame.mouse.get_pos()
    pos_in_mask = pos[0] - cat.rect.x, pos[1] - cat.rect.y
    pos_in_maskb = pos[0] - bat.rect.x, pos[1] - bat.rect.y


    touchingcat = cat.rect.collidepoint(*pos) and cat.mask.get_at(pos_in_mask)
    touchingbat = bat.rect.collidepoint(*pos) and bat.mask.get_at(pos_in_maskb)


    screen.fill(pygame.Color('red') if touchingcat else pygame.Color('green'))
    screen.fill(pygame.Color('red') if touchingbat else pygame.Color('green'))

    screen.blit(cat.image, cat.rect)
    screen.blit(bat.image, bat.rect)

    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONUP and touchingbat == 1:
                    print("clicoubat")
        if e.type == pygame.MOUSEBUTTONUP and touchingcat == 1:
                    print("clicoucat")
        if e.type == pygame.QUIT:
            running = False
