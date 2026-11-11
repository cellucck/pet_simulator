import pygame
import sys
from inventory import Inventory
from shop import Shop
from home import Home
from button import Button



SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('home')
        self.home = Home(self.screen, self.gameStateManager, Buttons)
        self.inventory = Inventory(self.screen, self.gameStateManager)
        self.shop = Shop(self.screen, self.gameStateManager)

        self.states = {'home':self.home, 'inventory':self.inventory,
                       'shop':self.shop}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

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


# Instantiate buttons
btn_inventory = Button("Inventory", 15, SCREEN_HEIGHT - 225, 200, 50,
                       'chartreuse4', 'chartreuse3', False)
btn_shop = Button("Open Shop", 15, SCREEN_HEIGHT - 150 , 200, 50,
                  "cadetblue", "cadetblue1", False)
btn_quit = Button("Quit Game", 15, SCREEN_HEIGHT - 75, 135, 50,
                  "brown3", "brown2", False)
btn_hunger = Button("Hunger", 10, 25, 150, 75,
                    'coral2', 'coral1', True)
btn_hydration = Button("Hydration", 170, 25, 150, 75,
                       'cyan3', 'cyan2', True)
btn_mood = Button("Mood", 330, 25, 150, 75,
                  'darkolivegreen3', 'darkolivegreen3', True)
btn_energy = Button('Energy', 490, 25, 150, 75,
                    'orchid3', 'orchid2', True)

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
Buttons = []
Buttons.append(btn_hunger)
Buttons.append(btn_hydration)
Buttons.append(btn_mood)
Buttons.append(btn_energy)
Buttons.append(hunger_shadow)
Buttons.append(hydration_shadow)
Buttons.append(mood_shadow)
Buttons.append(energy_shadow)
Buttons.append(hunger_bar)
Buttons.append(hydration_bar)
Buttons.append(mood_bar)
Buttons.append(energy_bar)
Buttons.append(btn_inventory)
Buttons.append(btn_shop)
Buttons.append(btn_quit)


if __name__ == "__main__":
    game = Game()
    game.run()

