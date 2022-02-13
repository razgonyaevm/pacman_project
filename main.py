from scripts.draw_setk import draw
from scripts.block_class import Block

import pygame

from scripts.pacman_class import Pacman

pygame.init()
with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]
screen = pygame.display.set_mode(size)
pac_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()

with open("maps/first_map.txt") as map_file:
    m = list(map(lambda x: x.strip(), map_file.readlines()))
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '#':
            block = Block(block_sprites)
            block.set_coord(width // len(m[i]) * j, height // len(m) * i)
        # нужно добавить класс для отрисовки точек, которые есть герой

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
    block_sprites.draw(screen)
    draw("white", screen, width, height)
    pygame.display.flip()
pygame.quit()
