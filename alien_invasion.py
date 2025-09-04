import sys

import pygame

from settings import Settings

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

    def run_game(self):
        """Запускает осовной цикл игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # При каждом проходе цикла прерисовывается экран.
            self.screen.fill(self.settings.bg_color)

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    Ai = AlienIvasion()
    Ai.run_game()
