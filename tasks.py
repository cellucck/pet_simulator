'''
This is the file for a parent class of tasks. Both Self Care goals and
in app tasks are considered children of this class; quantitiative and
qualitative self-care goals are grandchildren
'''

class Task:
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