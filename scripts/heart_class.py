import pygame.sprite

from scripts.load_im import load_image


class Heart(pygame.sprite.Sprite):
    pygame.init()
    image = load_image("heart.png")

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Heart.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
