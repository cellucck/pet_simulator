from scene import Scene
import pygame

class Home(Scene):
    def __init__(self, display, gameStateManager, button_list):
        super().__init__(display, gameStateManager)
        self.buttons = button_list
    def run(self):
        self.display.fill('teal')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.gameStateManager.set_state('shop')
        if keys[pygame.K_i]:
            self.gameStateManager.set_state('inventory')
        for event in pygame.event.get():
            for button in self.buttons:
                button.update(event)

        for button in self.buttons:
            button.draw(self.display)

        




    