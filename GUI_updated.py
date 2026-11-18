import pygame
import sys
from inventory import Inventory, INVENTORY_BUTTONS
from shop import Shop
from home import Home, HOME_SPRITES, HOME_BUTTONS, BACKGROUND
from button import Button
from pet_sprite import PetSprite
from goal_log import GoalLog, GOAL_BUTTONS




SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('home')
        self.home = Home(self.screen, self.gameStateManager, BACKGROUND,
                         HOME_BUTTONS, HOME_SPRITES)
        self.inventory = Inventory(self.screen, self.gameStateManager, INVENTORY_BUTTONS)
        self.shop = Shop(self.screen, self.gameStateManager)
        self.goallog = GoalLog(self.screen, self.gameStateManager, [], GOAL_BUTTONS)
        self.states = {'home':self.home, 'inventory':self.inventory,
                       'shop':self.shop, 'goal':self.goallog}

    def run(self):
        while True:
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state
        self.state_stack = [current_state]

    def get_state(self):
        return self.current_state

    def set_state(self, new_state):
        self.current_state = new_state
        self.state_stack.append(new_state)

    def go_back(self):
        self.state_stack.pop()
        self.set_state(self.state_stack[-1])





if __name__ == "__main__":
    game = Game()
    game.run()

