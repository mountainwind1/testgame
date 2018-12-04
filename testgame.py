import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()

    isettings = Settings()

    screen = pygame.display.set_mode((isettings.screen_width, isettings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    ship = Ship(isettings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(isettings, screen, ship)


run_game()
