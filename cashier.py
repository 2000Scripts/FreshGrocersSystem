from employee import Employee

class Cashier(Employee): #Inheritance
    def __init__(self, employee_id, name, branch, hourly_rate, hours_worked):
        super().__init__(employee_id, name, branch)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked