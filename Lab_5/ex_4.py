# 4. Build an employee hierarchy with a base class Employee.
# Create subclasses for different types of employees like
# Manager, Engineer, and Salesperson. Each subclass should have
# attributes like salary and methods related to their roles.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + ' with salary ' + str(self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def calculate_bonus(self):
        return 0.15 * self.salary

    def get_salary(self):
        return self.salary + self.calculate_bonus()

    def __str__(self):
        return 'Manager ' + super().__str__() + ' in departament ' + str(self.department)


class Engineer(Employee):
    def __init__(self, name, salary, programming_language, project):
        super().__init__(name, salary)
        self.programming_language = programming_language
        self.project = project

    def get_engineer_task(self):
        return f"{self.name} is coding in {self.programming_language} at the project {self.project}"

    def get_salary(self):
        return self.salary

    def __str__(self):
        return 'Engineer ' + super().__str__() + ' codes in ' + self.programming_language + ' for the project ' + self.project


class Salesperson(Employee):
    def __init__(self, name, salary, sales_target):
        super().__init__(name, salary)
        self.sales_target = sales_target

    def calculate_commission(self, sales_amount):
        if sales_amount >= self.sales_target:
            return 0.1 * sales_amount
        else:
            return 0

    def get_salary(self):
        return self.salary + self.calculate_commission(sales_amount=100000)

    def __str__(self):
        return 'Sales person ' + super().__str__() + ' ' + ' should sale over ' \
            + str(self.sales_target) + ' to get commission'


manager = Manager('Alex', 1000, 'IT')
print(manager)

engineer = Engineer('Alexandra', 500, 'Python', 'Project_1')
print(engineer.get_engineer_task())
print(engineer)

salesperson = Salesperson('Mada', 300, 100000)
print(salesperson)