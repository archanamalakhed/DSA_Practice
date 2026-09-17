'''Problem 2: Employee Payroll Hierarchy (Inheritance & Method Overriding)
Model an organization's payroll system where different types of employees calculate compensation differently while reusing base information.
Requirements:
Create a base class Employee that initializes emp_id, name, and base department, with a generic calculate_pay() method.
Create a child class SalariedEmployee that takes a fixed monthly salary and overrides calculate_pay().
Create a child class HourlyEmployee that takes hourly_rate and hours_worked and overrides calculate_pay().
Ensure both child classes use super().__init__() to initialize common attributes.
Write a script that iterates over a list of mixed employees and prints their monthly pay in a single polymorphic loop.'''

class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def get_details(self):
        return f"Employee ID: {self.emp_id} | Name: {self.name} | Dept: {self.department}"

    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement calculate_pay()")


class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, department, monthly_salary):
        super().__init__(emp_id, name, department)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, department, hourly_rate, hours_worked):
        super().__init__(emp_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        else:
            regular_pay = 40 * self.hourly_rate
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            return regular_pay + overtime_pay


# List of diverse employee objects
employees = [
    SalariedEmployee("SE101", "Alice Smith", "Engineering", 6500.0),
    SalariedEmployee("SE102", "Bob Jones", "Marketing", 4800.0),
    HourlyEmployee("HE201", "Charlie Brown", "Operations", hourly_rate=25.0, hours_worked=38),  # Normal hours
    HourlyEmployee("HE202", "Diana Prince", "Logistics", hourly_rate=30.0, hours_worked=46),   # 6 hrs overtime
]

for emp in employees:
    details = emp.get_details()
    payout = emp.calculate_pay()
    print(f"{details} -> Monthly Payout: ${payout:.2f}")