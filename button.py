import pygame
import sys


class Button:
    '''Blueprint for any Buttons in that will be displayed'''
    def __init__(self, text, x, y, width, height, normal_color,
                 hover_color, status=False, action=None):
        pygame.init()
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont('Comic Sans', 24)

        # Color options
        self.normal_color = normal_color
        self.hover_color = hover_color

        # Current displayed button color
        self.color = normal_color

        # action that the button performs when clicked
        self.action = action

        # True if button is a status button for the pet
        self.status: bool = status

        # Writes button text on top for status buttons,
        # and in the center for non-status buttons
        if self.status is False:
            self.text_surf = self.font.render(text, True, 'cornsilk')
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        else:
            self.text_surf = self.font.render(text, True, 'cornsilk')
            self.text_rect = self.text_surf.get_rect(midtop=self.rect.midtop)

    def get_color(self):
        '''Return current button color'''
        return self.color

    def set_color(self, new_color):
        '''Set current button color to arg: new_color'''
        self.color = new_color

    def draw(self, surface):
        '''draw button_rect and write text on button surface'''
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surf, self.text_rect)

    def update(self, event):
        '''Detect User Mouse Position and update self.color if hovering'''
        mouse_pos = pygame.mouse.get_pos()

        # Hover effect
        if self.rect.collidepoint(mouse_pos):
            self.set_color(self.hover_color)

            # Checks for mouse clicks ONLY if
            # cursor is hovering over button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.action:
                    self.action()
        else:
            self.color = self.normal_color