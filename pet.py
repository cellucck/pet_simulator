'''
This is the Pet file, a specific instance of an 
owned pet. This is DIFFERENT than our general pet_type
class that has general design elements/things for each 
pet (assuming there are some differences)

something like
from pets import pet_type
'''
class Pet:
    def __init__(self, name, pet_type, color):
        self.name = name
        self.pet_type = pet_type
        self.age: float = 0
        self.hunger_status: float = 1
        self.energy_status: float = 1
        self.hydration_status: float = 1
        self.headware = None
        self.outfit = None
        self.footware = None
        self.color = color
        self.current_animation = None #stand still
        

#~~~~~~~~~~~~~~Attribute Getters~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_name(self):
        return self.name

    def get_pet_type(self):
        return self.pet_type

    def get_age(self):
        return self.age

    def get_hunger(self):
        return self.hunger_status

    def get_energy(self):
        return self.energy_status

    def get_hydration(self):
        return self.hydration_status

    #these might get combined (e.g. self.appearance)
    def get_headware(self):
        return self.headware
    def get_outfit(self):
        return self.outfit
    def get_footware(self):
        return self.footware
    def get_color(self):
        return self.color

    def get_current_animation(self):
        return self.current_animation

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    

    def update_status(self, status, value):
        '''
        is called after/when peforming some sort of pet-care activity as
        the player. Essentially a setter function but for any one of our
        statuses as they all will have a range of [0, 1]. So will verify
        the "after update" status and adjust to make valid if needed

        (this might need to be changed if we run into the different
        statuses needing some sort of design difference. )

        args:
        status -str?- the relevant pet status we want to update
        value -float- the +/- value that we will update our status with
        '''
        pass

    def update_appearance(self, new_appearance):
        pass