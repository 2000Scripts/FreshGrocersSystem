class Employee:
    #Object
    def __init__(self, employee_id, name, branch):
        self.employee_id = employee_id
        self.name = name
        self.branch = branch

    def calculate_pay(self): #Polymorphism 
        raise NotImplementedError("Subclasses must implement calculate_pay")

    def display_info(self): #Polymorphism
        return f"Employee {self.employee_id}: {self.name}, Branch: {self.branch}"