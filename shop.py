from scene import Scene
import pygame

class Shop(Scene):
    def run(self):
        self.display.fill('green')
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_i]:
                self.gameStateManager.set_state('inventory')
            if keys[pygame.K_h]:
                self.gameStateManager.set_state('home')