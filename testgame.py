import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()

    isettings = Settings()

    screen = pygame.display.set_mode((isettings.screen_width, isettings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(isettings.bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()
