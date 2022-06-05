# Python OOP

class Employee:
  # instead of manually making variables, we can use a class.
  def __init__(self, first, last, pay):
    # this is a special method which basically initiziales the function and it defaultly takes the instance as the first argument. eg: emp_1, emp_2, name of our instance.
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + "@company.com"

  def full_name(self):
     return f"{self.first} {self.last}"

'''emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

# instance variables are variables that hold data unique to the instance.
emp_1.first = 'Corey'
emp_1.last = 'Williamson'
emp_1.pay = 50000
emp_1.email = 'something@company.com'

emp_2.first = 'Todd'
emp_2.last = 'Chavez'
emp_2.pay = 70000
emp_2.email = 'something_1@company.com'
print(emp_1.email)
print(emp_2.email)
'''

# code using class instances and methods.

emp_1 = Employee('Todd', 'Chavez', 50000)
emp_2 = Employee('Bojack', 'Horseman', 60000)

# here, we make an instance of the class Employee and print out one of the attributes of said class.
print(emp_1.email)
print(emp_2.email)
# print(f"{emp_1.first} {emp_1.last}")
# print(f"{emp_2.first} {emp_2.last}")
print(emp_1.full_name())
print(emp_2.full_name())

# here, instead of printing the attributes of the instance, we print the attributes directly from the class which does the same thing but we have to pass in the instance name as an argument (parameter). put side by side
print(Employee.full_name(emp_1))
print(emp_1.email)
