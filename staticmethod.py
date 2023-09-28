class A:
    def printName(self,age):
        self.age=age

        print("vikash", age)

    @staticmethod
    def printOccupation():
        print("i am software engineerer")  
a=A()
a.printName(12)

a.printName(34)
a.printOccupation()          