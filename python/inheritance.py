class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first +'.' + last + '@email.com'
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
       #print raise_amt
        self.pay = int(self.pay + self.raise_amt)

class Developer(Employee):
    raise_amt = 1.0
    #print raise_amt 
    def __init__(self,first,last,pay,prog_lang):
        Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang
	print self.first
    #pass

class Manager(Employee):
   
    def __init__(self,first,last,pay,employees = None):
        Super().__init__(self,first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employess.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

#dev_1 = Employee('Corey','Schafer',50000)
#dev_1 = Employee('Corey','Schafer',50000)
dev_1 = Developer('Test','Employee',6000,'Python')
dev_2 = Developer('Test','Employee',6000,'Java')

#print(help(Developer))

#mgr_1 = Manager('Sue','Smith',9000,[dev_1])

#print(mgr_1.email)

#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_1)

#print(issubclass(mgr_1, Developer))
#print(issubclass(Manager, Developer))


#mgr_1.print_emps()

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_2.pay)

#print(dev_1.email)
#print(dev_2.email)
#print dev_1.fullname()
