class Employee(object):
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.1)

emp_1 = Employee('Jun', 'Yoon', 50000)
emp_1.apply_raise()
print(emp_1.pay)
