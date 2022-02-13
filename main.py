from scripts.draw_setk import draw

import pygame

from scripts.pacman_class import Pacman

pygame.init()
size = width, height = 1000, 954
screen = pygame.display.set_mode(size)
pac_sprites = pygame.sprite.Group()

pacman = Pacman(pac_sprites)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for pac in pac_sprites:
            pac.click(event)
    screen.fill((0, 0, 0))
    pac_sprites.draw(screen)
    draw("white", screen, width, height)
    pygame.display.flip()
pygame.quit()
