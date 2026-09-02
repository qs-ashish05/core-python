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

    def __str__(self):
        return f"Emp_id = {self.emp_id}, Emp_name = {self.name} base_salary = {self.base_salary}"


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super.__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus + self.bonus

