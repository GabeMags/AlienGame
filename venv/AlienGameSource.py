import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from barrier import Barrier
from UFO import UFO

import game_functions as gf

def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    #Make the play button
    play_button = Button(ai_settings, screen, "Play!")

    #Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #make a ship, a group of bullets, and a group of aliens, a group of barriers, and a UFO
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #barrier = Group()
    ufo = UFO(ai_settings, screen)


    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #create a way to keep track of time (for the ufo spawn)
    time_elapsed = 0
    clock = pygame.time.Clock()

    #Start the main loop for the game
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)


        dt = clock.tick()
        time_elapsed += dt
        sec = 0

        if stats.game_active:
            ship.update()
            gf.update_ufo(ai_settings, screen, ufo)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)



        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, ufo)


run_game()