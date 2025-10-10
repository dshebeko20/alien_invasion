class Settings:
    """Класс для хранения всех насстроек игры "Инопланетное вторжение"."""

    def __init__(self):
        """Иниициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройка корабля
        self.ship_limit = 3
        
        # Папраметры снаряда
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (0, 0, 255)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры.
        self.speedup_scale = 1.1
        
        # Темп роста стоиости пришельцев.
        self.score_scale = 1.5

        self.initialize_dinamic_settings()

    def initialize_dinamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 обозначает движение впрааво, а -1 - влево.
        self.fleet_direction = 1

        # Подсчёт очков.
        self.alien_points = 50

    def increace_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)