import sys

import pygame

class AlienIvasion:
    """Класс для управлением ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запускает осовной цикл игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Отображение последнего прорисованного экрана.
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    Ai = AlienIvasion()
    Ai.run_game()
