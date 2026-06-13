"""
Determine whether a number is valid according to the Luhn formula.
"""
class Luhn:
    """
    The number will be provided as a string.
    """
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        numbers = list(map(int, self.card_num.strip()))[::-1]
        
        for idx, num in enumerate(numbers):

            if idx % 2:
                num *= 2
                numbers[idx] = num - 9 if num > 9 else num
                    

        return sum(numbers) % 10 == 0
