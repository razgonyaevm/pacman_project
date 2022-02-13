import pygame

with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]

from scripts.load_im import load_image


class Warrior(pygame.sprite.Sprite):
    pygame.init()

    def __init__(self, name, coin, *group):
        super().__init__(*group)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        if coin == 1:
            self.rect.y = 0
        else:
            self.rect.y = height - 50
