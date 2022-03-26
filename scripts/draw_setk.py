import pygame

pygame.init()


def draw(color, screen, width, height):
    """отрисовка клетчатой сетки на поле"""
    for i in range(height // 53):
        for j in range(width // 50):
            pygame.draw.rect(screen, color, (j * 50, i * 53, 50, 53), 1)
