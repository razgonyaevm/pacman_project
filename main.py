import random
import os

from scripts.draw_game_over import draw_game_over
from scripts.draw_setk import draw
from scripts.block_class import Block
from scripts.coin_class import Coin
from scripts.heart_class import Heart

import pygame

from scripts.load_im import load_image
from scripts.pacman_class import Pacman
from scripts.warrior_class import Warrior

os.environ['SDL_VIDEO_CENTERED'] = '1'


def main(name, n):
    coins = -1
    s = 0

    pygame.init()
    with open('data/life.txt') as life_file:
        life = int(life_file.readline())
    with open('data/map_size.txt') as map_size:
        m = list(map(int, map_size.readline().split()))
        size = width, height = m[0], m[1]
    with open('data/coin.txt', 'w') as file:
        file.write('-1')
    screen = pygame.display.set_mode((size[0] + 400, size[1]))
    pac_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    warrior_sprites = pygame.sprite.Group()
    coin_sprites = pygame.sprite.Group()
    heart_sprites = pygame.sprite.Group()

    with open(f"maps/{name}") as map_file:
        m = list(map(lambda x: x.strip(), map_file.readlines()))
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '#':
                block = Block(block_sprites)
                block.set_coord(width // len(m[i]) * j, height // len(m) * i)
            else:
                if random.choice([0, 1, 2]) == 1:
                    coin = Coin(coin_sprites)
                    coin.set_coord(width // len(m[i]) * j + 10, height // len(m) * i + 10)
                    coins += 1
    for i in range(life):
        heart = Heart(width + 5, 30 * i, heart_sprites)

    pacman = Pacman(name, pac_sprites)
    first_warrior = Warrior(name, "red_ghost.png", 1, warrior_sprites)
    second_warrior = Warrior(name, "pink_ghost.png", 2, warrior_sprites)
    third_warrior = Warrior(name, "light_blue_ghost.png", 3, warrior_sprites)
    fourth_warrior = Warrior(name, "orange_ghost.png", 4, warrior_sprites)
    running = True
    coin = life

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for pac in pac_sprites:
                pac.click(event)
                for i in coin_sprites:
                    i.collision(pac.rect.x, pac.rect.y)
        with open('data/coin.txt') as file:
            if int(file.readline()) == coins:
                return 1
        for i in [first_warrior, second_warrior, third_warrior, fourth_warrior]:
            i.move()
            if i.eat([pacman.rect.x, pacman.rect.y]):
                for hear in heart_sprites:
                    hear.kill()
                    s += 1
                    if s == 1:
                        s = 0
                        break
                coin -= 1
                pacman.rect.x = ((width // 50) // 2) * 50
                pacman.rect.y = height - 53
                pacman.key = 1
                pacman.image = load_image("pacman.png")
                for j in [first_warrior, second_warrior, third_warrior, fourth_warrior]:
                    j.go_home(j.coin)

        if coin == 0:
            draw_game_over(screen, width, height)
            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT and pygame.event.wait().type != pygame.KEYDOWN:
                pass
            pygame.quit()
            return 0
        screen.fill((0, 0, 0))
        pac_sprites.draw(screen)
        block_sprites.draw(screen)
        warrior_sprites.draw(screen)
        coin_sprites.draw(screen)
        heart_sprites.draw(screen)
        with open('data/coin.txt') as file:
            font = pygame.font.Font(None, 40)
            text = font.render(f"Уровень {n}: " + str(int(file.readline()) + 1), True, (255, 255, 255))
            text_x = width + 40
            text_y = height - 40
            screen.blit(text, (text_x, text_y))
        draw("white", screen, width, height)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main('first_map.txt', 1)
