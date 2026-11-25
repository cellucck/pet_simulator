import pygame
import sys
from inventory import Inventory, INVENTORY_BUTTONS
from shop import Shop, SHOP_BUTTONS, SHOP_SPRITES #MESSAGE_SPRITES
from home import Home, HOME_SPRITES, HOME_BUTTONS, BACKGROUND
from button import Button
from pet_sprite import PetSprite
from goal_log import GoalLog, GOAL_BUTTONS
from pet import Pet
from player import Player
import random
from items import SMALL_ITEMS
from purchase_conf import PurchaseConfirmation, CONF_BUTTONS




SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640
FPS = 60

class Game:
    def __init__(self, pet, player):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.player = player
        self.pet = pet
        self.gameStateManager = GameStateManager('home')
        self.home = Home(self.screen, self.gameStateManager, self.pet,
                         self.player, BACKGROUND,
                         HOME_BUTTONS, HOME_SPRITES)
        self.inventory = Inventory(self.screen, self.gameStateManager, self.pet, 
                                   self.player, INVENTORY_BUTTONS)
        self.shop = Shop(self.screen, self.gameStateManager, self.pet, self.player,
                         None, SHOP_BUTTONS, SHOP_SPRITES, SMALL_ITEMS)
        self.goallog = GoalLog(self.screen, self.gameStateManager, self.pet, 
                               self.player, [], GOAL_BUTTONS)
        self.purchase_confirmation = PurchaseConfirmation(self.screen, self.gameStateManager, 
                                                          self.pet, self.player, CONF_BUTTONS)
        self.states = {'home':self.home, 'inventory':self.inventory,
                       'shop':self.shop, 'goal':self.goallog,
                       'purchase':self.purchase_confirmation, 
                       }



    def run(self):
        last_update = pygame.time.get_ticks()
        update_delay = 2000

        while True:
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()

            #now = pygame.time.get_ticks()
            #if now - last_update >= update_delay:
            #    update_values = [5, 10, 20]
            #    hunger_val = self.pet.get_hunger()
            #    hyration_val = self.pet.get_hyration()
            #    energy_val = self.pet.get_energy()

            #    self.pet.update_status()
                
            self.clock.tick(FPS)



            
            


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state
        self.state_stack = [current_state]

    def get_state(self):
        return self.current_state

    def set_state(self, new_state):
        if new_state not in self.state_stack:
            self.state_stack.append(new_state)
        self.current_state = new_state

    def go_back(self):
        self.state_stack.pop()
        self.set_state(self.state_stack[-1])





if __name__ == "__main__":
    reginald = Pet("Reginald")
    user1 = Player('krcellucci@gmail.com', '123abc', 'krcellucci')
    game = Game(reginald, user1)

    game.run()

