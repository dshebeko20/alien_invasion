import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Класс для управлением ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Создание экземпляров для хранения статистики и панели результатов.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
        # Игра "Инопланетное вторжение" запускается в неактивном состоянии.
        self.game_active = False

        # Созданлие кнопки Play.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Запускает осовной цикл игры"""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Сброс игровых настроек.
            self.settings.initialize_dinamic_settings()
            self._start_game()
            
    def _start_game(self):
        # Сброс игровой статиистики.
        self.stats.reset_stats()
        self.sb.prep_score()
        self.game_active = True

        # Очистка групп aliens и bullets.
        self.bullets.empty()
        self.aliens.empty()

        # Создание нового флота и размещение корабля в центре.
        self._create_fleet()
        self.ship.center_ship()

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)
                
    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""      
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif (event.key == pygame.K_p) and (not self.game_active):
            self._start_game()
        elif event.key == pygame.K_q:
            sys.exit()   

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""       
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def fire_bullet(self):
        # Создаёт новый снаряд и добавляет его в группу bullets.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Обновляет позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()
        
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Обрабатывает коллизии снарядов с пришельцами."""
        # Удаление снарядов и приишельцев, уаствующих в колизиях.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increace_speed()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _ship_hit(self):
        """Обрабатыват столкновение корабля с пришельцем."""
        if self.stats.ships_left > 0:
            # Уменьшение ships_left.
            self.stats.ships_left -= 1

            # Очистка групп aliens и bullets.
            self.bullets.empty()
            self.aliens.empty()

            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()

            # Пауза
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """
        Проверяет, достиг ли флот края экрана, с последующим обновлением
        позиций всех пришельцев во флоте.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Проверка коллизий "пришелец - кораль".
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Проверить, сталкивается ли пришелец с нижним краем экрана.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Проверяет, добралиась ли пришельцы до нижнего кра экрана."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Происходит то же, что и при столкновении с кораблём.
                self._ship_hit()
                break

    def _create_fleet(self):
        """Создаёт флот пришеьцев."""
        # Создание пришельца и добавление других, пока остаётся место.
        # Рассстояние между пришельцами составляет одну ширину 
        # и одну выстоу пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Конец ряда: сбрасываем значение x и инкрементируем значение y.
            current_x = alien_width
            current_y += 2 * alien_height
           
    def _create_alien(self, x_position, y_position):
        """Создаёт пришельца и размещает его в ряду."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и именяет его направление."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Вывод информации о счёте.
        self.sb.show_score()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.game_active:
            self.play_button.draw_button()
            
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    Ai = AlienInvasion()
    Ai.run_game()
