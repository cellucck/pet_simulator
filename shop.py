from scene import Scene
import pygame
import sys
from button import Button
from pet_sprite import PetSprite
import random

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640


class Shop(Scene):
    def __init__(self, display, gameStateManager, pet, player,
                 background, button_list, perm_sprites, condit_sprites):
        super().__init__(display, gameStateManager, pet, player)
        self.buttons = button_list
        self.permanent_sprites = perm_sprites
        self.background = background
        self.conditional_sprites = condit_sprites
        self.current_comment_type = ''
        self.new_comment_type = 'welcome'
        self.message_button = self.buttons[2]
        self.comment = ''
    
    def run(self):
        self.display.fill('lightgreen')
        self.permanent_sprites.draw(self.display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_i]:
                self.gameStateManager.set_state('inventory')
            if keys[pygame.K_h]:
                self.gameStateManager.set_state('home')


            for button in self.buttons:
                button.update(event, self)
            
    

        self.update_credits()
        self.conditional_sprites.draw(self.display)
        for button in self.buttons:
            button.draw(self.display)
        

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
        print('You have inspected this Item. GREAT JOB')
        self.new_comment_type = 'item'
        self.display_shopkeeper_text()

    def display_shopkeeper_text(self):
        welcome_comments = [
            'Welcome in! What item are you looking for today?',
            'Hi there! What can I do for you?',
            'What brings you in?']
        item_comments = [
            'A mighty fine item right there if I say so myself!',
            'You have great tast I see!',
            "That one has been flying off my shelves!",
            "A classic!"]
        purchase_comments = [
            'Pleasure doing business. Have a great day!',
            "Hope your pet likes that one!"]

        if self.new_comment_type != self.current_comment_type:
            if self.new_comment_type == 'welcome':
                print('accessed welcome')
                choice = random.randint(0, 2)
                self.set_comment(welcome_comments[choice])
            elif self.new_comment_type  == 'item':
                print('accessed item')
                choice = random.randint(0, 3)
                self.set_comment(item_comments[choice])
            elif self.new_comment_type  == 'purchase':
                print('accessed purchase')
                choice = random.randint(0, 1)
                self.set_comment(purchase_comments[choice])
            

        
            self.buttons[2] = Button(f"{self.comment}", 120, 150, 250, 100,
                                "white", "white", "black", True, False, None)
            self.current_comment_type = self.new_comment_type
        
    def update_credits(self):
        self.buttons[1] = Button(f"Credits: {self.player.get_credits()}", 440, 15, 200, 50,
                     "cadetblue3", "cadetblue3", "white", False, False, None)

        
        





                   




btn_back = Button("Back", 12, 15, 200, 50,
                "brown3", "brown2","cornsilk", False, False, Shop.go_back)
btn_credits = Button("Credits: [Data]", 440, 15, 200, 50,
                     "cadetblue3", "cadetblue3", "cornsilk", False, False, None)
shopkeeper_message = Button("", 120, 150, 250, 100,
                            "white", "white", "black", True, False, None)

SHOP_BUTTONS = [btn_back, btn_credits, shopkeeper_message]

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





message_image = pygame.image.load(
    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/merchant_sprites/Message_Bubble.png'
)
MESSAGE_BUBBLE = PetSprite(message_image, message_image, message_image, -20, -15)

SHOP_SPRITES = pygame.sprite.Group()
SHOP_SPRITES.add(wallpaper_sprite)
SHOP_SPRITES.add(merchant_sprite)
SHOP_SPRITES.add(shop_panel)
SHOP_SPRITES.add(desk_sprite)

MESSAGE_SPRITES = pygame.sprite.Group()
MESSAGE_SPRITES.add(MESSAGE_BUBBLE)
