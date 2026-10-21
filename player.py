'''
File constructing the Player class, main actor
of our system. It contains their account/irl 
information as well as their in game info like
credits, inventory, etc. Most of our app processes
will happen as a result of the methods in this class
'''

class Player:
    def __init__(self, email, password, username):
        self.email: str = email
        self.password: str = password
        self.username: str = username 
        self.pets: list = []
        self.credits: int = 0
        self.inventory: dict = {}


#~~~~~~~~~~~~~~Attribute Getters~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_username(self):
        return self.username 

    def get_pets(self):
        return self.pets

    def get_credits(self):
        return self.credits

    def get_inventory(self):
        return self.inventory

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def feed_pet(self, pet, food_item):
        '''
        method to feed a specified pet (in class player has multiple)
        with a given food_item (will end up calling the pet.update_status
        method)

        arguments:
        pet :pet: object of pet type, this is the pet we are feeding
        food_item :consumable: the food_item we are using

        returns:
        None (for now)
        '''
        pass

    def hydrate_pet(self, pet, drink_item):
        '''
        method to hydrate a specified pet (in class player has multiple)
        with a given drink_item (will end up calling the pet.update_status
        method)

        arguments:
        pet :pet: object of pet type, this is the pet we are feeding
        drink_item :consumable: the drink_item we are using

        returns:
        None (for now)
        '''
        pass

    def play_with_pet(self, pet, activity_item):
        '''
        method to play with a specified pet (in class player has multiple)
        with a given activity_item (will end up calling the pet.update_status
        method)

        arguments:
        pet :pet: object of pet type, this is the pet we are feeding
        activity_item :consumable: the toy/activity item we are using

        returns:
        None (for now)
        '''
        pass

    def equip_pet(self, pet, wearable_item):
        '''
        method to equip pet with a new wearable item from a player's
        inventory (will end up calling the update_appearance)
        
        arguments
        pet :pet: object of pet type, this is the pet we are feeding
        wearable_item :wearable: the item we are equipping
        '''
        pass


    def buy_item(self, current_credits, shop_item):
        '''
        this method actually 'purchases' an in shop item which both
        - adds the item(s) to the player's inventory
        - properly adjusts the player's available credits to use

        If the player is trying to purchase a consumable item, the
        function requests a desired quantity to buy (limited)

        arguments
        current_credits :int: how many credits the player has to spend
        shop_item :item: the item that the player is trying to buy
        '''
        pass


    def create_goal(self):
        '''
        this method prompts the user for all the needed information
        that we will use to classify the goal

        returns
        goal :self-care goal:
        '''
        pass

    def log_goal(self, goal):
        '''
        user selects a goal to update and enters their progress update
        - how much has been completed (quanttitative goals)
        - mark complete (quantitative and yes/no goals)

        method confirms the entry validity and then updates accordingly

        arguments
        goal :goal: the goal we want to update

        returns
        none (for now)
        '''
        pass

    def perform_task(self, task):
        '''
        this will be the function that player has going when they want
        to complete a task/in-app game (i.e game could be pong, or 
        maybe they have to clean up the pet's area)
        
        arguments
        task :task: the task the player is trying to complete. Must
                    be available to complete (not on cooldown)
                    
        '''
        pass




    

