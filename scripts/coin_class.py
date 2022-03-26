from scripts.load_im import load_image

import pygame

with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]


class Coin(pygame.sprite.Sprite):
    """Размечает точки на игровом окне, который поедает герой"""
    image = load_image("coin.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Coin.image
        self.rect = self.image.get_rect()

    def set_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def collision(self, x, y):
        if self.rect.x - 10 == x and self.rect.y - 10 == y:
            with open('data/coin.txt') as file:
                m = int(file.readline())
            with open('data/coin.txt', 'w') as file:
                file.write(str(m + 1))
            self.kill()
