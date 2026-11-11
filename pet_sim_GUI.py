'''
For Version 1.0 Release, this is the only programming file.
This acts as more of a proof of concept more than anything, with
simple implementation of the pygame package and what we want our
web app to look like. Beyond 1.0 Release, the project will have
multiple files as we implement more features like being able to
display different screens
'''
import pygame
import sys


# Initializing pygame library, and defining display constants
pygame.init()
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans", 24)


class PetSprite(pygame.sprite.Sprite):
    '''
    Blueprint for PetSprite object to be displayed
    '''
    def __init__(self, base_image, happy_image, x, y):
        '''
        Initialize the Pet sprite object

        Keyword Arguments:
        base_image - pygame.image - the normal / resting image
        happy_image - pygame.image - the hover state of our pet on home screen
        x -- starting x position
        y -- starting y poisiton
        '''
        pygame.sprite.Sprite.__init__(self)

        # different pet image options
        self.normal_image = base_image
        self.hover_image = happy_image

        # current image state of the pet
        self.image = self.normal_image

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Define hitbox as smaller than image_rect for collision checking
        self.hitbox = self.rect.inflate(-150, -175)

    def get_image(self):
        '''Return current image of PetSprite'''
        return self.image

    def set_image(self, image_variant):
        '''Set current image of PetSprite'''
        self.image = image_variant

    def update(self):
        '''Detect User Mouse Position and update self.image if hovering'''
        mouse_pos = pygame.mouse.get_pos()

        # Checks for collision with hitbox instead of the image_rect
        if self.hitbox.collidepoint(mouse_pos):
            self.set_image(self.hover_image)

        else:
            self.set_image(self.normal_image)



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

sprites = pygame.sprite.Group()
sprites.add(dragon)

# These methods are placeholders for now, will end up
# being how we switch between displays in final project
# build.


def open_inventory():
    print("Opened Inventory")


def open_shop():
    print("Opened Shop")


def quit_game():
    pygame.quit()
    sys.exit()


def open_hunger():
    print("Opened Hunger")


def open_hydration():
    print("Opened Hydration")


def open_play():
    print("Opened Play")


# Instantiate buttons
btn_inventory = Button("Inventory", 15, SCREEN_HEIGHT - 225, 200, 50,
                       'chartreuse4', 'chartreuse3', False, open_inventory)
btn_shop = Button("Open Shop", 15, SCREEN_HEIGHT - 150 , 200, 50,
                  "cadetblue", "cadetblue1", False, open_shop)
btn_quit = Button("Quit Game", 15, SCREEN_HEIGHT - 75, 135, 50,
                  "brown3", "brown2", False, quit_game)
btn_hunger = Button("Hunger", 10, 25, 150, 75,
                    'coral2', 'coral1', True, open_hunger)
btn_hydration = Button("Hydration", 170, 25, 150, 75,
                       'cyan3', 'cyan2', True, open_hydration)
btn_mood = Button("Mood", 330, 25, 150, 75,
                  'darkolivegreen3', 'darkolivegreen3', True)
btn_energy = Button('Energy', 490, 25, 150, 75,
                    'orchid3', 'orchid2', True, open_play)

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


while True:
    screen.fill(('powderblue'))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit_game()

        # Checks for any button clicks and enacts action
        for button in Buttons:
            button.update(event)

        dragon.update()

    # Draws Dragon Sprite Hitbox for development aid
    pygame.draw.rect(screen, (255, 0, 0), dragon.hitbox, 2)

    # Draws all sprites and Buttons
    sprites.draw(screen)

    for button in Buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    