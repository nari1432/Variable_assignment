#create an employee class and add details of employee  
#using three deferent variables and access that variables

class Employee:
    total_employees = 0

    def __init__(self, name, salary):  # Instance variable
        self.name = name
        self.salary = salary
        Employee.total_employees += 1  # Static variable

    def display_employee_details(self):  # Local variable
        department = "python"
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {department}")  # Local variable

    def display_total_employees(self):
        print(f"Total Employees: {Employee.total_employees}")  # Static variable

employee1 = Employee("venu", 220000)
employee2 = Employee("Arya", 800000)
employee3 = Employee("Sujatha", 750000)

# Instance variable

print("Employee 1 Name:", employee1.name)
print("Employee 1 salary:", employee1.salary)
print("Employee 2 Name:", employee2.name)
print("Employee 2 salary:", employee2.salary)
print("Employee 3 Name:", employee3.name)
print("Employee 3 salary:", employee3.salary)

print("Total Employees:", Employee.total_employees)  # Static variable

employee1.display_employee_details()  # Local variable
