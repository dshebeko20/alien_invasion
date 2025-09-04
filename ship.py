import pygame

class Chip:
    """Класс для управления корблём."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = ai_game.screen()
        self.screen_rect = ai_game.screen.get_rect()

        # Загржает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляеся у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)