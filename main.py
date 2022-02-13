from scripts.draw_setk import draw

import pygame

from scripts.pacman_class import Pacman

pygame.init()
with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]
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
