"""
Given students' names along with the grade they are in, create a roster for the school.
"""
class School:
    """
    School students class
    """
    def __init__(self):
        self.students = {}
        self._added = []
        
    def add_student(self, name, grade):
        """Add student in dictionary"""
        if name not in self.students:
            self.students[name] = grade
            self._added.append(True)
        else:
            self._added.append(False)

    def roster(self):
        """Sort students name"""
        # Group by grade
        grades = {}
        for name, grade in self.students.items():
            grades.setdefault(grade, []).append(name)
        
        # Return flattened list
        return [
            name 
            for grade in sorted(grades)
            for name in sorted(grades[grade])
        ]
        

    def grade(self, grade_number):
        """Filter students by grade number"""
        return [
            name for name, grade in sorted(self.students.items())
            if grade == grade_number
        ]
        

    def added(self):
        """Monitor added students"""
        return self._added
