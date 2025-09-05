import pygame

class Ship:
    """Класс для управления корблём."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загржает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляеся у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Флаг преремещения: начинаем с неподвиного корабля.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)