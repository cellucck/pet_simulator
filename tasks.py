'''
This is the file for a parent class of tasks. Both Self Care goals and
in app tasks are considered children of this class; quantitiative and
qualitative self-care goals are grandchildren
'''
from abc import ABC


class Task(ABC):
    '''Task Parent Class - Abstract'''
    def __init__(self, name):
        self._name: str = self.set_name(name)
        self._task_id: str = ''
        self._reward: int = 0
        self._bonus_reward_chance: float = 0.0
        self._status: bool = True

    def get_name(self):
        return self._name

    def get_reward(self):
        return self._reward

    def get_bonus_reward_chance(self):
        return self._bonus_reward_chance

    def get_status(self):
        return self._status


    def set_name(self, new_name):
        #FIXME - Include some checks here for name validity
        self._name = new_name

    def update_status(self, new_status):
        #FIXME - Include some checks here for status validation
        self._status = new_status


class SelfCareGoal(Task):
    '''child of taks class, for self-care goals IRL'''
    def __init__(self, name):
        super().__init__(name)
        self._frequency: int = 1 #how often this goal comes up
        self._icon = None     #this will be a Sprite
        self._importance: int = 1  #enum

    def get_frequency(self):
        return self._frequency

    def get_icon(self):
        return self._icon

    def get_importance(self):
        return self._importance

    def set_icon(self, icon_option):
        '''will let player choose a Sprite for icon'''
        #FIXME - Need checks to validate the sprite type
        self._icon = icon_option


class Quantitative(SelfCareGoal):
    '''child of SelfCareGoal, specifically for progressable goals'''
    def __init__(self, name):
        super().__init__(name)
        self._percent_complete: float = 0.0


class Qualitative(SelfCareGoal):
    def __init__(self, name):
        super().__init__(name)
        self._completion_time: int = 0 #enum (i.e. 0 = morning)



class InAppActivity(Task):
    def __init__(self, name):
        super().__init__(name)
        self._difficulty: int = 1 #enum
        self._cooldown_window: float = 0.0


