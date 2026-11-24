from scene import Scene
import pygame
import sys
from button import Button
from pet_sprite import PetSprite
import random
from items import SMALL_ITEMS
from player import Player
import numpy as np

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640


class Shop(Scene):
    def __init__(self, display, gameStateManager, pet, player,
                 background, button_list, perm_sprites, items):
        super().__init__(display, gameStateManager, pet, player)
        self.buttons = button_list
        self.permanent_sprites = perm_sprites
        self.background = background

        # Initializing Item Locations for display in the shop
        self.columns = [SCREEN_HEIGHT - 270, SCREEN_HEIGHT - 135]
        self.rows = [47, 187, 327, 467]
        self.item_slots = {
            1:(self.rows[0], self.columns[0]), 2:(self.rows[1], self.columns[0]),
            3:(self.rows[2], self.columns[0]), 4:(self.rows[3], self.columns[0]),
            5:(self.rows[0], self.columns[1]), 6:(self.rows[1], self.columns[1]),
            7:(self.rows[2], self.columns[1]), 8:(self.rows[3], self.columns[1]),                                         
        }

        # From __init__ arg, all items that we have loaded into the items.py dict
        self.items = items
        self.products = []

        # Randomly picking 8 indexes to select items to display in the shop
        self.item_selections = random.sample(range(0, len(self.items)), 8)
        print(self.item_selections)
        for i in range(len(self.item_selections)):
            self.products.append(self.items[self.item_selections[i]])

        # Randomly picking 8 indexes that correspond to the self.item_slots locations
        self.item_assignments = random.sample(range(1, 9), 8)
        self.item_sprites = pygame.sprite.Group()
        for i in range(len(self.products)):
            new_size = (125, 125)
            item = self.products[i]
            image = pygame.image.load(item.get_image_path())
            scaled_image = pygame.transform.scale(image, new_size)
            location = self.item_assignments[i]
            x = self.item_slots[location][0]
            y = self.item_slots[location][1]
            self.buttons[i+2] = Button(f"${item.get_cost():.2f}", 
                                       x, y, 125, 125, 
                                     'bisque2','blanchedalmond', 'black', 
                                     True, True, Shop.inspect_item)
            new_sprite = PetSprite(scaled_image, scaled_image, scaled_image, x, y)
            self.item_sprites.add(new_sprite)


        #self.conditional_sprites = condit_sprites
        self.current_comment_type = ''
        self.new_comment_type = 'welcome' 
        self.message_button = self.buttons[2]
        self.comment = ''


    
    def run(self):
        self.display.fill('lightgreen')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            for button in self.buttons:
                button.update(event, self)
            
        self.permanent_sprites.draw(self.display)
        self.update_credits()
        #self.conditional_sprites.draw(self.display)
        for button in self.buttons:
            button.draw(self.display)
        
        self.item_sprites.draw(self.display)

        pygame.display.flip()
    
        

    def open_inventory(self):
        self.gameStateManager.set_state('inventory')

    def open_home(self):
        self.gameStateManager.set_state('home')

    def go_back(self):
        self.gameStateManager.go_back()

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def set_comment(self, new_comment):
        self.comment = new_comment

    def say_hi(self):
        self.new_comment_type = 'welcome'
        self.display_shopkeeper_text()

    def inspect_item(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(2, len(self.buttons)):
            button = self.buttons[i]
            product = self.products[i-2]
            if button.rect.collidepoint(mouse_pos):
                print(f"You've Inspected a {product.get_name()}")
                self.player.buy_item(product)

        #self.new_comment_type = 'item'
        #self.display_shopkeeper_text()

    def buy_item(self, item):
        pass
        

    #def display_shopkeeper_text(self):
    #    welcome_comments = [
    #        'Welcome in! What item are you looking for today?',
    #        'Hi there! What can I do for you?',
    #        'What brings you in?']
    #    item_comments = [
    #        'A mighty fine item right there if I say so myself!',
    #        'You have great tast I see!',
    #        "That one has been flying off my shelves!",
    #        "A classic!"]
    #    purchase_comments = [
    #        'Pleasure doing business. Have a great day!',
    #        "Hope your pet likes that one!"]
#
    #    if self.new_comment_type != self.current_comment_type:
    #        if self.new_comment_type == 'welcome':
    #            print('accessed welcome')
    #            choice = random.randint(0, 2)
    #            self.set_comment(welcome_comments[choice])
    #        elif self.new_comment_type  == 'item':
    #            print('accessed item')
    #            choice = random.randint(0, 3)
    #            self.set_comment(item_comments[choice])
    #        elif self.new_comment_type  == 'purchase':
    #            print('accessed purchase')
    #            choice = random.randint(0, 1)
    #            self.set_comment(purchase_comments[choice])
            

        
    #        self.buttons[2] = Button(f"{self.comment}", 120, 150, 250, 100,
    #                            "white", "white", "black", True, False, None)
    #        self.current_comment_type = self.new_comment_type
        
    def update_credits(self):
        self.buttons[1] = Button(f"Credits: {self.player.get_credits()}", 440, 15, 200, 50,
                     "cadetblue3", "cadetblue3", "white", False, False, None)

        
btn_back = Button("Back", 12, 15, 200, 50,
                "brown3", "brown2","cornsilk", False, False, Shop.go_back)
btn_credits = Button("Credits: [Data]", 440, 15, 200, 50,
                     "cadetblue3", "cadetblue3", "cornsilk", False, False, None)
#shopkeeper_message = Button("", 120, 150, 250, 100,
#                           "white", "white", "black", True, False, None)

SHOP_BUTTONS = [btn_back, btn_credits]

COLUMNS = [SCREEN_HEIGHT - 270, SCREEN_HEIGHT - 135]
ROWS = [47, 187, 327, 467]
def create_item_slots(i, j):
    item_button = Button("Price: []", ROWS[i], COLUMNS[j], 125, 125, 
                         'bisque2','blanchedalmond', 'black', 
                         True, True, Shop.inspect_item)
    SHOP_BUTTONS.append(item_button)

for i in range(len(ROWS)):
    for j in range(len(COLUMNS)):
        create_item_slots(i, j)

shop_panel_image = pygame.image.load(
    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/shop.png'
)
merchant_image = pygame.image.load(
    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/merchant_sprites/Merchant_openeye_openmouth.png'
)
wallpaper_image = pygame.image.load(
    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/merchant_sprites/Merchant wallpaper.png'
)
desk_image = pygame.image.load(
    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/merchant_sprites/Merchant desk.png'
)

shop_panel = PetSprite(shop_panel_image, shop_panel_image, shop_panel_image, 0, 90)
merchant_sprite = PetSprite(merchant_image, merchant_image, merchant_image, 75, 10)
wallpaper_sprite = PetSprite(wallpaper_image, wallpaper_image, wallpaper_image, 0, 0)
desk_sprite = PetSprite(desk_image, desk_image, desk_image, 0, -175)





#message_image = pygame.image.load(
#    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/merchant_sprites/Message_Bubble.png'
#)
#MESSAGE_BUBBLE = PetSprite(message_image, message_image, message_image, -20, -15)

SHOP_SPRITES = pygame.sprite.Group()
SHOP_SPRITES.add(wallpaper_sprite)
SHOP_SPRITES.add(merchant_sprite)
SHOP_SPRITES.add(shop_panel)
SHOP_SPRITES.add(desk_sprite)






#MESSAGE_SPRITES = pygame.sprite.Group()
#MESSAGE_SPRITES.add(MESSAGE_BUBBLE)
