import pygame.sprite

from scripts.load_im import load_image


class Block(pygame.sprite.Sprite):
    pygame.init()
    image = load_image("block.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Block.image
        self.rect = self.image.get_rect()

    def set_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y