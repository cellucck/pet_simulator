from scene import Scene
import pygame
import sys
from button import Button


SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640



class Inventory(Scene):
    def __init__(self, display, gameStateManager, button_list,
                     sprites_list=None):
            super().__init__(display, gameStateManager)
            self.buttons = button_list
            self.sprites = sprites_list

    def run(self):
        self.display.fill('teal')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 self.quit_game()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.gameStateManager.set_state('shop')
            if keys[pygame.K_h]:
                self.gameStateManager.set_state('home')

            for button in self.buttons:
                 button.update(event, self)

        for button in self.buttons:
             button.draw(self.display)

    def open_shop(self):
         self.gameStateManager.set_state('shop')\

    def open_home(self):
         self.gameStateManager.set_state('home')

    def go_back(self):
         self.gameStateManager.go_back()

    def quit_game(self):
            pygame.quit()
            sys.exit()
    
    def inspect_item(self):
        print('Look at THIS WOWWWW')




btn_home = Button("Home", 432, SCREEN_HEIGHT - 75, 200, 50,
                  'chartreuse4', 'chartreuse3',"cornsilk", False, False, Inventory.open_home)
btn_shop = Button("Open Shop", 222, SCREEN_HEIGHT - 75 , 200, 50,
                 "cadetblue", "cadetblue1","cornsilk", False, False, Inventory.open_shop)
btn_back = Button("Back", 12, SCREEN_HEIGHT - 75, 200, 50,
                  "brown3", "brown2","cornsilk", False, False, Inventory.go_back)


ROWS = [57, 192, 327, 462]
COLUMNS = [10, 145, 280, 415]

INVENTORY_BUTTONS = []

def item_slot(i, j):
    item_button = Button("", ROWS[i], COLUMNS[j], 125, 125, 'bisque2', 'blanchedalmond',
                       True, False, Inventory.inspect_item)
    
    INVENTORY_BUTTONS.append(item_button)



for i in range(len(ROWS)):
    for j in range(len(COLUMNS)):
         item_slot(i, j)


#INVENTORY_BUTTONS.append(btn_home)
INVENTORY_BUTTONS.append(btn_shop)
INVENTORY_BUTTONS.append(btn_back)

