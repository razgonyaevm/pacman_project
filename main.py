from scripts.draw_setk import draw
from scripts.block_class import Block

import pygame

from scripts.pacman_class import Pacman
from scripts.warrior_class import Warrior

pygame.init()
with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]
screen = pygame.display.set_mode(size)
pac_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
warrior_sprites = pygame.sprite.Group()

with open("maps/first_map.txt") as map_file:
    m = list(map(lambda x: x.strip(), map_file.readlines()))
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '#':
            block = Block(block_sprites)
            block.set_coord(width // len(m[i]) * j, height // len(m) * i)
        # нужно добавить класс для отрисовки точек, которые ест герой

pacman = Pacman(pac_sprites)
first_warrior = Warrior("first_warrior.png", 1, warrior_sprites)  # добавить картинку чупакабрика (ее нет)
second_warrior = Warrior("second_warrior.png", 2, warrior_sprites)  # и этому чупакабрику
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
    warrior_sprites.draw(screen)
    draw("white", screen, width, height)
    pygame.display.flip()
pygame.quit()
