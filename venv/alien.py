import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #a class to represent a single alien in the fleet

    def __init__(self, ai_settings, screen):
        #initialize the alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/skull_1.png')
        self.image2 = pygame.image.load('images/skull_2.png')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #draw the alien at its current location
        #now = pygame.time.get_ticks()
        #if (now / 1000 % 2 == 1):
        #    self.screen.blit(self.image2, self.rect)
        #else:
        #    self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect)

    def check_edges(self):
        #return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #move the alien right or left
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
