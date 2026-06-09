"""
Given a diagram, determine which plants each child in the kindergarten class is responsible for.
There are 12 children in the class
"""
class Garden:
    """
    Representation of kindergarten
    """

    PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
    
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        if students is None:
            students = [
                "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
            ]
        self.students = sorted(students)    
        self.rows = diagram.splitlines()
    
    def plants(self, student):
        """
        Define student plant order
        """
        pos = self.students.index(student)
        start = (pos) * 2
        end = start + 2

        cups = self.rows[0][start:end] + self.rows[1][start:end]
       
        return [Garden.PLANTS[letter] for letter in cups]
    
        
    