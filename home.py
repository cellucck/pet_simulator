from scene import Scene
import pygame
import sys
from pet_sprite import PetSprite
from button import Button

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640


class Home(Scene):
    def __init__(self, display, gameStateManager, button_list,
                 sprites_list):
        super().__init__(display, gameStateManager)
        self.buttons = button_list
        self.sprites = sprites_list
    def run(self):
        self.display.fill('teal')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.gameStateManager.set_state('shop')
            if keys[pygame.K_i]:
                self.gameStateManager.set_state('inventory')
            
            for button in self.buttons:
                button.update(event, self)

            self.sprites.update()

        self.sprites.draw(self.display)
        for button in self.buttons:
            button.draw(self.display)

    def open_inventory(self):
        self.gameStateManager.set_state('inventory')

    def open_shop(self):
        self.gameStateManager.set_state('shop')

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def open_hunger(self):
        self.gameStateManager.set_state('inventory')

    def open_hydration(self):
        self.gameStateManager.set_state('inventory')

    def open_play(self):
        self.gameStateManager.set_state('inventory')


# Instantiate buttons
btn_inventory = Button("Inventory", 15, SCREEN_HEIGHT - 225, 200, 50,
                       'chartreuse4', 'chartreuse3', False, False, Home.open_inventory)
btn_shop = Button("Open Shop", 15, SCREEN_HEIGHT - 150 , 200, 50,
                  "cadetblue", "cadetblue1", False, False, Home.open_shop)
btn_quit = Button("Quit Game", 15, SCREEN_HEIGHT - 75, 135, 50,
                  "brown3", "brown2", False, False, Home.quit_game)
btn_hunger = Button("Hunger", 10, 25, 150, 75,
                    'coral2', 'coral1', False, True, Home.open_hunger)
btn_hydration = Button("Hydration", 170, 25, 150, 75,
                       'cyan3', 'cyan2', False, True, Home.open_hydration)
btn_mood = Button("Mood", 330, 25, 150, 75,
                  'darkolivegreen3', 'darkolivegreen3', False, True)
btn_energy = Button('Energy', 490, 25, 150, 75,
                    'orchid3', 'orchid2', False, True, Home.open_play)

# Sclars values for status bars, static for prototype build
HUNGER_STAT = 0.75     # FIXME - eventually can do Pet.get_hunger()
HYDRATION_STAT = 0.5    # FIXME - eventuall can do Pet.get_hydration()
MOOD_STAT = 0.3
ENERGY_STAT = 0.8

# Create buttons that represent the actual PetCare statues
hunger_shadow = Button("", 22, 75, 125, 10,
                       "gray",'gray', False, None)
hunger_bar = Button("", 22, 75, 125*HUNGER_STAT, 10,
                    'white', 'white', False, None)


hydration_shadow = Button("", 182, 75, 125, 10,
                          'gray', 'gray', False, None)
hydration_bar = Button("", 182, 75, 125*HYDRATION_STAT, 10,
                       'white', 'white', False, None)


mood_shadow = Button("", 342, 75, 125, 10,
                     'gray', 'gray', False, None)
mood_bar = Button("", 342, 75, 125*MOOD_STAT, 10,
                  'white', 'white', False, None)


energy_shadow = Button("", 502, 75, 125, 10,
                       'gray', 'gray', False, None)
energy_bar = Button("", 502, 75, 125*ENERGY_STAT, 10,
                    'white', 'white', False, None)

# Create Button list and add all created buttons
HOME_BUTTONS = []
HOME_BUTTONS.append(btn_hunger)
HOME_BUTTONS.append(btn_hydration)
HOME_BUTTONS.append(btn_mood)
HOME_BUTTONS.append(btn_energy)
HOME_BUTTONS.append(hunger_shadow)
HOME_BUTTONS.append(hydration_shadow)
HOME_BUTTONS.append(mood_shadow)
HOME_BUTTONS.append(energy_shadow)
HOME_BUTTONS.append(hunger_bar)
HOME_BUTTONS.append(hydration_bar)
HOME_BUTTONS.append(mood_bar)
HOME_BUTTONS.append(energy_bar)
HOME_BUTTONS.append(btn_inventory)
HOME_BUTTONS.append(btn_shop)
HOME_BUTTONS.append(btn_quit)

# Uploading dragon PNGs and converting into pygame images
new_size = (400, 400)
dragon_normal = pygame.image.load(
    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software '
    'Engineering/Pet Sim Project/practice_code/assets/dragon0.png')
scaled_dragon_normal = pygame.transform.scale(dragon_normal, new_size)
dragon_happy = pygame.image.load(
    '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software '
    'Engineering/Pet Sim Project/practice_code/assets/dragon_happy.png')
scaled_dragon_happy = pygame.transform.scale(dragon_happy, new_size)

# Instantiating a PetSprite with Dragon images
dragon = PetSprite(scaled_dragon_normal, scaled_dragon_happy, 125, 75)

HOME_SPRITES = pygame.sprite.Group()
HOME_SPRITES.add(dragon)



          




    