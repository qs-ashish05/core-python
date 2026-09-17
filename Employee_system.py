# Design a simple Employee Management System:
# Create a base class Employee with:
# Attributes: name, emp_id, base_salary
# A method calculate_salary() that returns base_salary. A method display_info() that prints the employee's name, ID, and calculated salary
#
# Create a class Manager that inherits from Employee:
#
# Adds an attribute bonus
# Overrides calculate_salary() to return base_salary + bonus
#
# Create a class Developer that inherits from Employee:
# Adds an attribute programming_language
# Overrides display_info() to also print the programming language (in addition to the base info — use super())
#
# Create a class TeamLead that inherits from both Manager and Developer (multiple inheritance):
# Should be able to use calculate_salary() (bonus logic) and display_info() (language info)
# Test it by creating one object of each class and calling display_info() on them. Also print TeamLead.__mro__.



class Employee:

    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.calculate_salary()}")


class Manager(Employee):

    def __init__(self, name, emp_id, base_salary, bonus):
        self.bonus = bonus

        super().__init__(
            name,
            emp_id,
            base_salary
        )

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):

    def __init__(
        self,
        name,
        emp_id,
        base_salary,
        programming_language,
        **kwargs
    ):
        self.programming_language = programming_language

        super().__init__(
            name,
            emp_id,
            base_salary
        )

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# class TeamLead(Manager, Developer):
#
#     def __init__(
#         self,
#         name,
#         emp_id,
#         base_salary,
#         bonus,
#         programming_language
#     ):
#
#         # Initialize Manager
#         Manager.__init__(
#             self,
#             name,
#             emp_id,
#             base_salary,
#             bonus
#         )
#
#         # Initialize Developer
#         Developer.__init__(
#             self,
#             name,
#             emp_id,
#             base_salary,
#             programming_language
#         )

class TeamLead(Manager, Developer):

    def __init__( self,  name, emp_id, base_salary, bonus, programming_language):
        super().__init__(self,
            name,
            emp_id,
            base_salary,
            bonus,
            programming_language
        )
# Testing

employee = Employee("Aashish", 101, 50000)

manager = Manager("Rahul", 102, 70000, 10000)

developer = Developer("Amit", 103, 60000, "Python")

teamlead = TeamLead(
    "Raj",
    104,
    80000,
    20000,
    "Java"
)


print("Employee:")
employee.display_info()

print("\nManager:")
manager.display_info()

print("\nDeveloper:")
developer.display_info()

print("\nTeamLead:")
teamlead.display_info()

print("\nTeamLead MRO:")
print(TeamLead.__mro__)