from scene import Scene
import pygame
import sys
from button import Button
from player import Player
from pet_sprite import PetSprite


SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640



class Inventory(Scene):
    def __init__(self, display, gameStateManager, pet, player,
                 button_list, sprites_list=None):
            super().__init__(display, gameStateManager, pet, player)
            self.buttons = button_list
            self.sprites = sprites_list
            self.inventory = self.player.get_inventory()
            self.owned_items = list(self.inventory.keys())
            
            

            self.rows = [57, 192, 327, 462]
            self.columns = [10, 145, 280, 415] 

            self.item_slots = {
                        1:(self.rows[0], self.columns[0]), 2:(self.rows[1], self.columns[0]),
                        3:(self.rows[2], self.columns[0]), 4:(self.rows[3], self.columns[0]),
                        5:(self.rows[0], self.columns[1]), 6:(self.rows[1], self.columns[1]),
                        7:(self.rows[2], self.columns[1]), 8:(self.rows[3], self.columns[1]),
                        9:(self.rows[0], self.columns[2]), 10:(self.rows[1], self.columns[2]),
                        11:(self.rows[2], self.columns[2]), 12:(self.rows[3], self.columns[2]),
                        13:(self.rows[0], self.columns[3]), 14:(self.rows[1], self.columns[3]),
                        15:(self.rows[2], self.columns[3]), 16:(self.rows[3], self.columns[3]),  

                    }

            self.owned_item_sprites = pygame.sprite.Group()
                 
                 

    def run(self):
        self.display.fill('teal')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 self.quit_game()

            for button in self.buttons:
                 button.update(event, self)


        for button in self.buttons:
            button.draw(self.display)
        self.update_credits()
        if self.player.get_inventory != self.inventory:
            self.update_inventory()
        self.owned_item_sprites.draw(self.display)

        pygame.display.flip()

    def open_shop(self):
         self.gameStateManager.set_state('shop')

    def open_home(self):
         self.gameStateManager.set_state('home')

    def go_back(self):
         self.gameStateManager.go_back()

    def quit_game(self):
            pygame.quit()
            sys.exit()
    
    def inspect_item(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self.owned_items)):
            button = self.buttons[i+3]
            product = self.owned_items[i]
            if button.rect.collidepoint(mouse_pos):
                print(f"You've Inspected a {product.get_name()}")

            
        

    def update_credits(self):
        self.buttons[2] = Button(
             f"Credits: {self.player.get_credits()}", 465, SCREEN_HEIGHT- 75, 175, 50, 
                'lightgreen', 'lightgreen', 'white', False, False, None)

    def update_inventory(self):
        self.inventory = self.player.get_inventory()
        self.owned_items = list(self.inventory.keys())
        for i in range(len(self.owned_items)):
            new_size = (125, 125)
            item = self.owned_items[i]
            quantity = self.inventory[item]
            image = pygame.image.load(item.get_image_path())
            x = self.item_slots[i+1][0]
            y = self.item_slots[i+1][1]
            self.buttons[i+3] = Button(f"Count: {quantity}", x, y, 125, 125, 'bisque2', 
                    'blanchedalmond', 'black',
                    True, True, Inventory.inspect_item)
            new_sprite = PetSprite(image, image, image, x, y)
            self.owned_item_sprites.add(new_sprite)





btn_home = Button("Home", 432, SCREEN_HEIGHT - 75, 200, 50,
                  'chartreuse4', 'chartreuse3',"cornsilk", False, False, Inventory.open_home)
btn_shop = Button("Open Shop", 222, SCREEN_HEIGHT - 75 , 200, 50,
                 "cadetblue", "cadetblue1","cornsilk", False, False, Inventory.open_shop)
btn_back = Button("Back", 12, SCREEN_HEIGHT - 75, 200, 50,
                  "brown3", "brown2","cornsilk", False, False, Inventory.go_back)
btn_credits = Button("Credits: ", 490, SCREEN_HEIGHT-95, 150, 75, 
                     'lightgreen', 'lawngreen', 'white', False, False, None)


ROWS = [57, 192, 327, 462]
COLUMNS = [10, 145, 280, 415]

INVENTORY_BUTTONS = [btn_shop, btn_back, btn_credits]

def item_slot(i, j):
    item_button = Button("Count: []", ROWS[i], COLUMNS[j], 125, 125, 'bisque2', 
                        'blanchedalmond', 'black',
                       True, True, Inventory.inspect_item)
    
    INVENTORY_BUTTONS.append(item_button)



for i in range(len(ROWS)):
    for j in range(len(COLUMNS)):
         item_slot(i, j)


