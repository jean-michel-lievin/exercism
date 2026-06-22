"""
Given a person's allergy score, 
determine whether or not they're allergic to a given item, 
and their full list of allergies.
"""
class Allergies:
    """
    Class to handle allergies scores
    """
    scores = {
        "eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8, "tomatoes": 16,
        "chocolate": 32, "pollen":64, "cats":128,
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return item in Allergies.scores.keys() and (self.score & Allergies.scores[item]) > 0

    @property
    def lst(self):
        return [allergy for allergy in Allergies.scores.keys() if self.allergic_to(allergy)]