"""
Given a person's allergy score, 
determine whether or not they're allergic to a given item, 
and their full list of allergies.
"""
class Allergies:
    """
    Class to handle allergies scores
    """
    def __init__(self, score):
        self.score = score
        self.allergens = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        # binary check with index (1 << i)
        self.allergies = [self.allergens[i] for i in range(len(self.allergens)) if score & (1 << i)]

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies