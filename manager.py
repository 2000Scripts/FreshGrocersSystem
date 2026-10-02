from employee import Employee

class Manager(Employee):#Inheritance
    def __init__(self, employee_id, name, branch, monthly_salary, bonus):
        super().__init__(employee_id, name, branch)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_pay(self):
        return self.monthly_salary + self.bonus