class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_employees(self, sort_parameter):
        if sort_parameter == 1:  # Sort by Age
            self.employees.sort(key=lambda emp: emp.age)
        elif sort_parameter == 2:  # Sort by Name
            self.employees.sort(key=lambda emp: emp.name)
        elif sort_parameter == 3:  # Sort by Salary
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter!")

    def display_employees(self):
        for employee in self.employees:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

def main():
    employee_table = EmployeeTable()

    employee_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    employee_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Sorting Options:")
    print("1. Age\n2. Name\n3. Salary")
    sort_option = int(input("Enter the sorting parameter: "))
    
    employee_table.sort_employees(sort_option)
    print("\nSorted Employee Data:")
    employee_table.display_employees()

if __name__ == "__main__":
    main()
