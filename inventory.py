from scene import Scene
import pygame

class Inventory(Scene):
    def run(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.gameStateManager.set_state('shop')
        if keys[pygame.K_h]:
            self.gameStateManager.set_state('home')