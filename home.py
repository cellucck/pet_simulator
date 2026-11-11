from scene import Scene
import pygame

class Home(Scene):
    def run(self):
        self.display.fill('teal')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.gameStateManager.set_state('shop')
        if keys[pygame.K_i]:
            self.gameStateManager.set_state('inventory')