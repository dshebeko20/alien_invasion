import pygame

class Ship:
    """Класс для управления корблём."""
    
    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загржает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляеся у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корбля.
        self.x = float(self.rect.x)

        # Флаги преремещения: начинаем с неподвиного корабля.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Размещает корабль в центре нижней чаасти экрана."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """обновляет позицию корабля с учетом флагов."""
        # Обновляет фтрибут x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    