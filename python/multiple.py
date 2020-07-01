class Human:
    def __init__(self, age, name):
        self.name = name
        self.age = age

class Dancer:
    def __init__(self,style):
        self.style = style

class Student(Human,Dancer):
    def __init__(self, age, name, style):
        Human.__init__(self,age,name)
        Dancer.__init__(self,style)
    

John = Student(20,'John','HipHop')
print(John.style)
