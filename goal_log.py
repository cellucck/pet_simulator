from scene import Scene
import pygame
import sys
from button import Button

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 640

class GoalLog(Scene):
    def __init__(self, display, gameStateManager, goals_list,
                 buttons_list):
        super().__init__(display, gameStateManager)
        self.goals = goals_list
        self.buttons = buttons_list

    def run(self):
        self.display.fill('aquamarine3')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for button in self.buttons:
                button.update(event, self)


        for button in self.buttons:
            button.draw(self.display)

    def go_back(self):
            self.gameStateManager.go_back()




btn_back = Button("Back", 12, SCREEN_HEIGHT - 75, 200, 50,
                  "brown3", "brown2","cornsilk", False, False, GoalLog.go_back)

# Creating Header "Buttons" for the goal list
btn_header1 = Button("Goal Name", 10, 15, 380, 30, "cornsilk4", "cornsilk4",
                     "cornsilk", True, False, None)
btn_header2 = Button("Status", 395, 15, 130, 30, "cornsilk4", "cornsilk4", 
                     "cornsilk", True, False, None)
btn_header3 = Button("Reward", 530, 15, 110, 30, "cornsilk4", "cornsilk4", 
                     "cornsilk", True, False, None)
GOAL_BUTTONS = [btn_back, btn_header1, btn_header2, btn_header3]


def create_goal_slots(i):
     '''
     Create buttons for each of the player's goals on our Goal Screen.
     FIXME - Eventually we will have this function take goal data from
     the player.py file. Numbered goals are just a place holder for now
     '''
     item_button = Button(f'Goal Number {i}', 10, ROWS[i], 380, 55, 
                          "gray90", "gray99", "gray20",
                          True, False, None)
     GOAL_BUTTONS.append(item_button)

def create_status_slots(i):
     status_button = Button(f'[Status]', 395, ROWS[i], 130, 55,
                            "gray90", "gray90", "gray20",
                            True, False, None)
     GOAL_BUTTONS.append(status_button)

def create_reward_slots(i):
    reward_button = Button(f'[Reward]', 530, ROWS[i], 110, 55,
                        "gray90", "gray90", "gray20",
                        True, False, None)
    GOAL_BUTTONS.append(reward_button)   

# Setting the starting y values for each of our rows of goals
ROWS = [50, 110, 170, 230, 290, 350, 410, 470]
for i in range(len(ROWS)):
    create_goal_slots(i)
    create_status_slots(i)
    create_reward_slots(i)