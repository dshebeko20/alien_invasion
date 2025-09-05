import sys

import pygame

from settings import Settings
from ship import Ship

class AlienIvasion:
    """Класс для управлением ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запускает осовной цикл игры"""
        while True:
            self._check_events()
            self._update_screen()
            
            self.clock.tick(60)
    
    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
            """Обновляет изображения на экране и отображает новый экран."""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    Ai = AlienIvasion()
    Ai.run_game()
