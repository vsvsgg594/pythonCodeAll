from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def frombirthyear(cls,name,year):
        return cls(name, date.today().year - year)
    
    @staticmethod

    def isAudlt(age):
        return age>18
    

p1=Person("viaksh",24)
p2=Person.frombirthyear("vikash",1999)
print(p1.age)
print(p2.age)
print(p1.isAudlt(24))
