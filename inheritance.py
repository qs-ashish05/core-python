class Branch:
    def __init__(self, name,no_of_students):
        self.name = name
        self.no_of_students = no_of_students


    def __str__(self):
        return f'Branch {self.name} with {self.no_of_students} students'


class CSE(Branch):
    def __init__(self,name,no_of_students, faculty_strength):
        super().__init__(name,no_of_students)
        self.faculty_strength = faculty_strength

