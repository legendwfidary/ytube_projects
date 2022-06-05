# Python OOP

class Employee:
  # instead of manually making variables, we can use a class.
  def __init__(self, first, last, pay, email):
    # this is a special method which basically initiziales the function and it defaultly takes the instance as the first argument.
    self.first = first
    self.last = last
    self.pay = pay
    self.email = email

emp_1 = Employee()
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
