import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    #GAME ASSESTS AND RESOURCES
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        #Create an instance to store game statistics
        self.stats = GameStats(self)
        #Scoreboard
        self.sb = Scoreboard(self)
        # Active State to start the game
        self.game_active = False
        #make a play button
        self.play_button = Button(self, "Play")

    #MAIN LOOP FOR GAME
    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                print(len(self.bullets))
                self._update_aliens()        
            self._update_screen()
            self.clock.tick(60)

    #CHECK EVENTS ON MOUSE AN KEYBOARD
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    #start the game when the player clicks play
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #reset game settings
            self.settings.initialize_dynamic_settings()
            #reset game satistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.game_active = True
            #get rid of any old sprites
            self.bullets.empty()
            self.aliens.empty()
            #create new sprites center the ship
            self._create_fleet()
            self.ship.center_ship()
            #hide cursor
            pygame.mouse.set_visible(False)

    #SHIP MOVEMENT
    def _check_keydown_events(self,event):        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # Fire Photon Torpedos
    def _fire_bullet(self):

        #create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    #Create an alien fleet
    def _create_fleet(self):
        alien = Alien(self)
        alien_width ,alien_height = alien.rect.size
        self.aliens.add(alien)

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #After finishing a row reset x and y value
            current_x = alien_width
            current_y += 2*alien_height

    #create aliens for the fleet        
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        #Respond when an alien reach an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
                    
    #DRAW WHAT JUST HAPPENDED
    def _update_bullets(self):
        self.bullets.update()
            #DELETE BULLETS THAT HAVE LEFT THE SCREEN
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #Check if bullet his alien, delet bullet
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
        if not self.aliens:
            #Create new fleet         
            self._create_fleet()
            self.settings.increase_speed()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        #Make ship respond to getting hit
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            #reset sprites
            self.bullets.empty()
            self.aliens.empty()
            #Reset fleet and ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        #check if the aliens have reached the bottom of the screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        #draw play button if the screen is inactive
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()   
     
#RUN THE GAME
if __name__ == '__main__':
    #make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()


####if you're interested in finihsing this you left off on pg 291 rounding the score###