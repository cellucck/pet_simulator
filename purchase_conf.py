from scene import Scene
import pygame
import sys
from button import Button
from player import Player
from pet_sprite import PetSprite
from items import full_items


SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640

class PurchaseConfirmation(Scene):
    def __init__(self, display, gameStateManager, pet, player,
                     button_list):
        super().__init__(display, gameStateManager, pet, player)
        self.buttons = button_list
        self.sprites_list = pygame.sprite.Group()
        self.item = None
        

        


    def run(self):
        self.display.fill('lightgreen')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    self.gameStateManager.set_state('home')
            for button in self.buttons:
                button.update(event, self)

        if self.item != self.player.get_unconfirmed_item():
            self.confirm_item()
        for button in self.buttons:
            button.draw(self.display)
        self.sprites_list.draw(self.display)


    def confirm_item(self):
        self.sprites_list.empty()
        self.item = self.player.get_unconfirmed_item()
        image = pygame.image.load(self.item.get_image_path())
        new_sprite = PetSprite(image, image, image, 260, 250)
        self.sprites_list.add(new_sprite)
        


    def go_back(self):
        self.gameStateManager.go_back()

    def buy_item(self):
        purchase_item = self.player.get_unconfirmed_item()
        self.player.buy_item(purchase_item)
        self.gameStateManager.set_state('shop')


btn_window = Button("Would you like to buy this item?", 120, 220, 400, 230, 
                    "azure1", "azure1", "black", True, True, None)
btn_no = Button("NO", 130, 400, 175, 40, 
                "firebrick3", "firebrick1", "white", False, False, PurchaseConfirmation.go_back)
btn_purchase = Button("PURCHASE", 315, 400, 175, 40,
                "darkolivegreen4", "darkolivegreen2", "white",
                False, False, PurchaseConfirmation.buy_item)

CONF_BUTTONS = [btn_window, btn_no, btn_purchase]