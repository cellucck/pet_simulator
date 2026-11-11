import pygame
import sys


class Button:
    def __init__(self, text, x, y, width, height, normal_color,
                 hover_color, rounded=False, status=False, action=None):
        '''
        Intizialize Button appearance and functionality
        Keyword Arguments
        text - The lettering the button will display
        x, y - starting coordinates for the button rect
        width, heigh - size indicators
        normal_color, hover_color - resting and hovering color
        status - True if a Pet Status button, False if not
        action - what the button does if pressed
        '''
        pygame.init()
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont('Comic Sans', 24)
        self.rounded = rounded

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
        if self.rounded is True:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=15)
            surface.blit(self.text_surf, self.text_rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
            surface.blit(self.text_surf, self.text_rect)

    def update(self, event, scene):
        '''Detect User Mouse Position and update self.color if hovering'''
        mouse_pos = pygame.mouse.get_pos()

        # Hover effect
        if self.rect.collidepoint(mouse_pos):
            self.set_color(self.hover_color)

            # Checks for mouse clicks ONLY if
            # cursor is hovering over button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.action:
                    self.action(scene)
        else:
            self.color = self.normal_color