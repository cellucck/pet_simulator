import pygame
import sys

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans", 24)

class Button:
    def __init__(self, text, x, y, width, height, normal_color, hover_color,
                 action = None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.color = normal_color    #what the button rests at
        self.action = action


        self.text_surf = font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surf, self.text_rect)


    def check_interaction(self, event):
        mouse_pos = pygame.mouse.get_pos()

        #Hover effect
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color

            #click action
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.action:
                    self.action()
        else:
            self.color = self.normal_color

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, base_image, happy_image, x, y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.normal_image = base_image
       self.hover_image = happy_image
       
       self.image = self.normal_image
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.bottomleft = (x, y)
       self.rect.width -= 100

    def set_image(self, new_image):
        self.image = pygame.image.load(new_image)


    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.image = self.hover_image

        else:
            self.image = self.normal_image



new_size = (500, 400)
dragon_normal = pygame.image.load('/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/practice_code/assets/dragon0.png')
scaled_dragon_normal = pygame.transform.scale(dragon_normal, new_size)
dragon_happy = pygame.image.load('/Users/kevincellucci/Downloads/School_Work/CIS 350 - Software Engineering/Pet Sim Project/practice_code/assets/dragon_happy.png')
scaled_dragon_happy = pygame.transform.scale(dragon_happy, new_size)
dragon = Block(scaled_dragon_normal, scaled_dragon_happy, 150, 500)

sprites = pygame.sprite.Group()
sprites.add(dragon)

def open_inventory():
    print("Opened Inventory")

def open_shop():
    print("Opened Shop")

def quit_game():
    pygame.quit()
    sys.exit()


#instantiate buttons
btn_inventory = Button("Open Inventory", 15, SCREEN_HEIGHT // 1.5, 200, 50, 'chartreuse4', 'chartreuse3', open_inventory)
btn_shop = Button("Open Shop", 15, SCREEN_HEIGHT // 1.5 + 75, 200, 50, "cadetblue", "cadetblue1", open_shop)

btn_quit = Button("Quit Game", 15, 650, 135, 50, "brown3", "brown2", quit_game)


#instatiate sprite



while True:
    screen.fill(('darkslategray'))
    
    # Event Handling Loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit_game()
            
        # Pass window events to the buttons
        btn_inventory.check_interaction(event)
        btn_shop.check_interaction(event)
        btn_quit.check_interaction(event)
        dragon.update()


    # Draw elements to the screen
    btn_inventory.draw(screen)
    btn_shop.draw(screen)
    btn_quit.draw(screen)
    sprites.draw(screen)

    
    pygame.display.flip()
    clock.tick(60)
