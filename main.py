import sys

from scripts.draw_setk import draw
from scripts.block_class import Block

import pygame

from scripts.pacman_class import Pacman
from scripts.warrior_class import Warrior

pygame.init()
with open('data/life.txt') as life_file:
    life = int(life_file.readline())
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
first_warrior = Warrior("pacman.png", 1, warrior_sprites)  # добавить картинку чупакабрика (ее нет)
second_warrior = Warrior("pacman.png", 2, warrior_sprites)  # и этому чупакабрику
running = True
coin = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for pac in pac_sprites:
            pac.click(event)
    first_warrior.move()
    second_warrior.move()
    if first_warrior.eat([pacman.rect.x, pacman.rect.y]) or second_warrior.eat([pacman.rect.x, pacman.rect.y]):
        coin -= 1
        print(coin)
    if coin == 0:
        print("Game Over!")  # рисовать на экране
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
        sys.exit()
    screen.fill((0, 0, 0))
    pac_sprites.draw(screen)
    block_sprites.draw(screen)
    warrior_sprites.draw(screen)
    draw("white", screen, width, height)
    pygame.display.flip()
pygame.quit()
