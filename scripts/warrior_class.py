import random

import pygame

with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]

with open("maps/first_map.txt") as map_file:
    map_f = list(map(lambda x: x.strip(), map_file.readlines()))

from scripts.load_im import load_image


class Warrior(pygame.sprite.Sprite):
    pygame.init()

    def __init__(self, name, coin, *group):
        super().__init__(*group)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.y = 0
        if coin == 1:
            self.rect.x = 0
        else:
            self.rect.x = width - 50

    def correct(self, x_or_y, coin):
        if x_or_y == 'x':
            if coin == 50:
                if self.rect.x + 50 < width - 50:
                    if map_f[self.rect.y // 53][(self.rect.x + 50) // 50] != '#':
                        return True
                    return False
                return False
            elif coin == -50:
                if self.rect.x - 50 > 0:
                    if map_f[self.rect.y // 53][(self.rect.x - 50) // 50] != '#':
                        return True
                    return False
                return False
        else:
            if coin == 53:
                if self.rect.y + 53 < height - 53:
                    if map_f[(self.rect.y + 53) // 53][self.rect.x // 50] != "#":
                        return True
                    return False
                return False
            elif coin == -53:
                if self.rect.y - 53 > 0:
                    if map_f[(self.rect.y - 53) // 53][self.rect.x // 50] != '#':
                        return True
                    return False
                return False

    def move(self):
        mve = ["x", "y"]
        if random.choice(mve) == 'x':
            if random.choice([50, -50]) == 50:
                if self.correct('x', 50):
                    self.rect.x += 50
            else:
                if self.correct('x', -50):
                    self.rect.x -= 50
        else:
            if random.choice([53, -53]) == 53:
                if self.correct('y', 53):
                    self.rect.y += 53
            else:
                if self.correct('y', -53):
                    self.rect.y -= 53
