"""
Write a random character generator that follows the above rules.
"""
import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """
        This character has, among other things, six abilities; strength, dexterity, constitution,           intelligence, wisdom and charisma. These six abilities have scores that are determined randomly. You do this by rolling four 6-sided dice and recording the sum of the largest three dice. You do this six times, once for each ability.
        """
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dice_rolls, reverse=True)[:3])


def modifier(value):
    return (value - 10) // 2
