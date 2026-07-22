"""
Write a random character generator that follows the above rules.
"""
import random

ABILITIES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """
        This character has, among other things, six abilities; strength, dexterity, constitution,           intelligence, wisdom and charisma. These six abilities have scores that are determined randomly. You do this by rolling four 6-sided dice and recording the sum of the largest three dice. You do this six times, once for each ability.
        """
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dice_rolls)[1:])


def modifier(value):
    return (value - 10) // 2
