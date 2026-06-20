"""
Manage robot factory settings.

When a robot comes off the factory floor, it has no name.
"""
import random
from string import ascii_uppercase

class Robot:
    """
    The names must be random: they should not follow a predictable sequence. 
    Using random names means a risk of collisions. 
    Your solution must ensure that every existing robot has a unique name.
    """
    used_named = set()
    
    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        if self._name is None:
            self._name = self._generate_random_name()
            Robot.used_named.add(self._name)
        return self._name


    def _generate_random_name(self):
        while True:
            letters = "".join(random.choices(ascii_uppercase, k=2))
            digits = "".join(random.choices("0123456789", k=3))
            candidate_name = letters + digits
            if candidate_name not in Robot.used_named:
                return candidate_name
        

    def reset(self):
        self._name = None

        

        
