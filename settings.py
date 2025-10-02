class Settings:
    """Класс для хранения всех насстроек игры "Инопланетное вторжение"."""

    def __init__(self):
        """Иниициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройка корабля
        self.ship_speed = 2.0
        self.ship_limit = 3
        
        # Папраметры снаряда
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (0, 0, 255)
        self.bullets_allowed = 7

        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение впрааво, а -1 - влево.
        self.fleet_direction = 1