import pygame

from pygame.sprite import Sprite

class Barrier():
    #A class to represent a single barrier shield

    def __init__(self, ai_settings, screen):
        #Initialize the barrier and set its position in the game
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the barrier image and set its rect attribute
        self.image = pygame.image.load('images/barrier_1.png')
        self.rect = self.image.get_rect()

        #Place each barrier near the bottom of the screen
        self.rect.x = 200
        self.rect.y = 500

    def blitme(self):
        #blit the barrier on screen
        self.screen.blit(self.image, self.rect)