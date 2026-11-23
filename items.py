from pet_sprite import PetSprite
import pygame
'''
Item Dictionary with the following format:
{'item_id':(display_name, price, hunger_effect, hyd_effect, energy_effect,
            image_path)}'''

items = {
    'fft':("French Toast", 2, .15, -0.05, 0.1,
           '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Food sprites/French toast.png'),
    'fs':("Sandwich", 4, .25, -.08, 0.15,
           '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Food sprites/Food sandwich.png'),
    'fsal':("Salad", 3, .18, -0.03, 0.12,
            '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Food sprites/Salad.png'),
    'lemonade':('Lemonade', 2, .01, .12, 0.08,
                '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Food sprites/Lemonade.png'),
    'parfait':('Parfait', 3, .08, 0.02, 0.1,
               '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Food sprites/Food parfait.png'),
    'cola':('Cola', 3, .01, .15, .1,
            '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Food sprites/Cola.png'),
    'brac':("Bracelet", 4, 0, 0, 0,
            '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Clothes sprites/Bracelet.png'),
    'pink_col':('Pink Collar', 5, 0, 0, 0,
                '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Clothes sprites/Pink collar.png'),
    'purp_col':('Purple Collar', 5, 0, 0, 0,
                '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Clothes sprites/Purple collar.png'),
    'red_col':('Red Collar', 5, 0, 0, 0,
               '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Clothes sprites/Red collar.png'),
    'T_breath':('Breath Shirt', 10, 0, 0, 0,
                '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Clothes sprites/Shirt breath.png'),
    'T_moon':('Moon Shirt', 10, 0, 0, 0,
              '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Clothes sprites/Shirt moon.png'),
    'T_star':('Star Shirt', 10, 0, 0, 0,
              '/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/pet_simulator/practice_code/assets/Clothes sprites/Shirt star.png'),        
    }

pygame.init()
class Item:
    def __init__(self, item_id, name, cost,
                 hunger_effect, hydration_effect, energy_effect,
                 image_path):
        self.item_id = item_id
        self.name = name
        self.cost = cost
        self.hunger_effect = hunger_effect
        self.hydration_effect = hydration_effect
        self.energy_effect = energy_effect
        self.image_path = image_path

    def get_item_id(self):
        return self.item_id

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_hunger_effect(self):
        return self.hunger_effect

    def get_hydration_effect(self):
        return self.hydration_effect

    def get_energy_effect(self):
        return self.energy_effect

    def get_image_path(self):
        return self.image_path

ITEMS = []
index = 0
for i in items:
    values = list(items.values())[index]
    ITEMS.append(Item(i, values[0], values[1], values[2], values[3],
                    values[4], values[5]))
    index += 1


print(len(ITEMS))
