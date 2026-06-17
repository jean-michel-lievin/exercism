"""
Write methods that return the highest score from the list, 
the last added score and the three highest scores.
"""
class HighScores:
    """
    Class to manipulate scores
    """
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]