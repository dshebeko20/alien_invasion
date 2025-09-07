class Settings:
    """Класс для хранения всех насстроек игры "Инопланетное вторжение"."""

    def __init__(self):
        """Иниициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройка корабля
        self.ship_speed = 1.5