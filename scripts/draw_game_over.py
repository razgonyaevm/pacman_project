import pygame.font


def draw_game_over(screen, width, height):
    """отрисовка экрана после поражения пользователя"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("GAME OVER!", True, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)