import pygame
import sys
from inventory import Inventory, INVENTORY_BUTTONS
from shop import Shop
from home import Home, HOME_SPRITES, HOME_BUTTONS
from button import Button
from pet_sprite import PetSprite




SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('home')
        self.home = Home(self.screen, self.gameStateManager, HOME_BUTTONS, HOME_SPRITES)
        self.inventory = Inventory(self.screen, self.gameStateManager, INVENTORY_BUTTONS)
        self.shop = Shop(self.screen, self.gameStateManager)

        self.states = {'home':self.home, 'inventory':self.inventory,
                       'shop':self.shop}

    def run(self):
        while True:
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, new_state):
        self.current_state = new_state



if __name__ == "__main__":
    game = Game()
    game.run()

