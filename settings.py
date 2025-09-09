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
        
        # Папраметры снаряда
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (0, 0, 255)
        self.bullets_allowed = 7