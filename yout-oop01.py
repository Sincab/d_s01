class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def printout_emp(self):
        return f'{self.first}, {self.last.upper()}'

emp1 = Employee('Sinan', 'Selcuk', 5000)

print(Employee.printout_emp(emp1))

# # claas to create instance
# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)
#
# emp_1.first = 'Sinan'
# emp_1.last = 'Sel'
