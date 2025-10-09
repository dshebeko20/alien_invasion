import json
from pathlib import Path

class GameStats:
    """Отслеживвает статистику игры "Инопланетное вторжение"."""
    
    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """Получает сохранённый рекорд из файла."""
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1