import random

import pygame
from scripts.load_im import load_image

with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]

timer = 0


class Warrior(pygame.sprite.Sprite):
    """Класс для духов"""
    pygame.init()

    def __init__(self, name_file, name, coin, *group):
        super().__init__(*group)
        with open(f"maps/{name_file}") as map_file:
            self.map_f = list(map(lambda x: x.strip(), map_file.readlines()))
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.coin = coin
        if coin == 1:
            self.rect.x = 0
            self.rect.y = 0
        elif coin == 2:
            self.rect.y = 0
            self.rect.x = width - 50
        elif coin == 3:
            self.rect.x = 0
            self.rect.y = height - 53
        elif coin == 4:
            self.rect.x = width - 50
            self.rect.y = height - 53

    def correct(self, x_or_y, coin):
        if x_or_y == 'x':
            if coin == 50:
                if self.rect.x + 50 < width - 50:
                    if self.map_f[self.rect.y // 53][(self.rect.x + 50) // 50] != '#':
                        return True
                    return False
                return False
            elif coin == -50:
                if self.rect.x - 50 > 0:
                    if self.map_f[self.rect.y // 53][(self.rect.x - 50) // 50] != '#':
                        return True
                    return False
                return False
        else:
            if coin == 53:
                if self.rect.y + 53 < height - 53:
                    if self.map_f[(self.rect.y + 53) // 53][self.rect.x // 50] != "#":
                        return True
                    return False
                return False
            elif coin == -53:
                if self.rect.y - 53 > 0:
                    if self.map_f[(self.rect.y - 53) // 53][self.rect.x // 50] != '#':
                        return True
                    return False
                return False

    def move(self):
        global timer
        mve = ["x", "y"]
        if timer == 40:
            timer = 0
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
        else:
            timer += 1

    def eat(self, coords):
        if self.rect.x == coords[0] and self.rect.y == coords[1]:
            return True
        return False

    def go_home(self, coin):
        if coin == 1:
            self.rect.x = 0
            self.rect.y = 0
        elif coin == 2:
            self.rect.y = 0
            self.rect.x = width - 50
        elif coin == 3:
            self.rect.x = 0
            self.rect.y = height - 53
        elif coin == 4:
            self.rect.x = width - 50
            self.rect.y = height - 53