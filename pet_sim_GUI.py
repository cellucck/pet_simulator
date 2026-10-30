'''
This will be the file for all the visuals/the actual
interface the a user interacts with for the pet sim. 
(GUI = graphical user interface)
'''
import pygame
import sys

pygame.init()
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans", 24)

class Pet(pygame.sprite.Sprite):
    def __init__(self, base_image, happy_image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.normal_image = base_image
        self.hover_image = happy_image 

        self.image = self.normal_image

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hitbox = self.rect.inflate(-150, -175)

    

    def get_image(self):
        return self.image

    def set_image(self, image_variant):
        self.image = image_variant

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.hitbox.collidepoint(mouse_pos):
            self.set_image(self.hover_image)

        else:
            self.set_image(self.normal_image)

class Button:
    def __init__(self, text, x, y, width, height, normal_color, 
                 hover_color, status=False, action = None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.color = normal_color
        self.action = action
        self.status = status

        if self.status == False:
            self.text_surf = font.render(text, True, 'cornsilk')
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        else:
            self.text_surf = font.render(text, True, 'cornsilk')
            self.text_rect = self.text_surf.get_rect(midtop=self.rect.midtop)

    def set_color(self, new_color):
        self.color = new_color
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surf, self.text_rect)
        

    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()

        #hover effect
        if self.rect.collidepoint(mouse_pos):
            self.set_color(self.hover_color)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.action:
                    self.action()
        else:
            self.color = self.normal_color

#creating dragon sprites
new_size = (400, 400)
dragon_normal = pygame.image.load('/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/practice_code/assets/dragon0.png')
scaled_dragon_normal = pygame.transform.scale(dragon_normal, new_size)
dragon_happy = pygame.image.load('/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/practice_code/assets/dragon_happy.png')
scaled_dragon_happy = pygame.transform.scale(dragon_happy, new_size)
dragon = Pet(scaled_dragon_normal, scaled_dragon_happy, 125, 75)

sprites = pygame.sprite.Group()
sprites.add(dragon)

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


#Instantiate buttons
btn_inventory = Button("Inventory", 15, SCREEN_HEIGHT - 225, 200, 50, 'chartreuse4', 'chartreuse3', False, open_inventory)
btn_shop = Button("Open Shop", 15, SCREEN_HEIGHT - 150 , 200, 50, "cadetblue", "cadetblue1", False, open_shop)
btn_quit = Button("Quit Game", 15, SCREEN_HEIGHT - 75, 135, 50, "brown3", "brown2", False, quit_game)

#FIXME - Need Buttons for all the Statuses

btn_hunger = Button("Hunger", 10, 25, 150, 75, 'coral2', 'coral1', True, open_hunger)
btn_hydration = Button("Hydration", 170, 25, 150, 75, 'cyan3', 'cyan2', True, open_hydration)
btn_mood = Button("Mood", 330, 25, 150, 75, 'darkolivegreen3', 'darkolivegreen3', True)
btn_energy = Button('Energy', 490, 25, 150, 75, 'orchid3', 'orchid2', True, open_play)

##idealy would have some status data coming from another file (pet.py I think)
HUNGER_STAT = 0.75     #FIXME - eventually can do Pet.get_hunger()
HYDRATION_STAT = 0.5    #FIXME - eventuall can do Pet.get_hydration()
MOOD_STAT = 0.3
ENERGY_STAT = 0.8


hunger_shadow = Button("", 22, 75, 125, 10, "gray",'gray', False, None)
hunger_bar = Button("", 22, 75, 125*HUNGER_STAT, 10, 'white', 'white', False, None)


hydration_shadow = Button("", 182, 75, 125, 10, 'gray', 'gray', False, None)
hydration_bar = Button("", 182, 75, 125*HYDRATION_STAT, 10, 'white', 'white', False, None)


mood_shadow = Button("", 342, 75, 125, 10, 'gray', 'gray', False, None)
mood_bar = Button("", 342, 75, 125*MOOD_STAT, 10, 'white', 'white', False, None)


energy_shadow = Button("", 502, 75, 125, 10, 'gray', 'gray', False, None)
energy_bar = Button("", 502, 75, 125*ENERGY_STAT, 10, 'white', 'white', False, None)






Buttons = []

Buttons.append(btn_hunger)
Buttons.append(btn_hydration)
Buttons.append(btn_mood)
Buttons.append(btn_energy)


#These need to be drawn first so that the status bars are on top
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

        for button in Buttons:
            button.update(event)
        
        dragon.update()

    pygame.draw.rect(screen, (255, 0, 0), dragon.hitbox, 2)
    sprites.draw(screen)
    for button in Buttons:
        button.draw(screen)
    pygame.display.flip()
    clock.tick(60)

        