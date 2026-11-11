import pygame
from pygame.sprite import Sprite



class PetSprite(pygame.sprite.Sprite):
    '''
    Blueprint for PetSprite object to be displayed
    '''
    def __init__(self, base_image, happy_image, x, y):
        '''
        Initialize the Pet sprite object

        Keyword Arguments:
        base_image - pygame.image - the normal / resting image
        happy_image - pygame.image - the hover state of our pet on home screen
        x -- starting x position
        y -- starting y poisiton
        '''
        pygame.sprite.Sprite.__init__(self)

        # different pet image options
        self.normal_image = base_image
        self.hover_image = happy_image

        # current image state of the pet
        self.image = self.normal_image

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Define hitbox as smaller than image_rect for collision checking
        self.hitbox = self.rect.inflate(-150, -175)

    def get_image(self):
        '''Return current image of PetSprite'''
        return self.image

    def set_image(self, image_variant):
        '''Set current image of PetSprite'''
        self.image = image_variant

    def update(self):
        '''Detect User Mouse Position and update self.image if hovering'''
        mouse_pos = pygame.mouse.get_pos()

        # Checks for collision with hitbox instead of the image_rect
        if self.hitbox.collidepoint(mouse_pos):
            self.set_image(self.hover_image)

        else:
            self.set_image(self.normal_image)



