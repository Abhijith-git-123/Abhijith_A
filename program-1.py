class Calculator():
    def __init__(self, a, b, operations):
        self.a = float(a)
        self.b = float(b)
        self.operations = operations

    def calculate(self):
        if self.operations == "add":
            return self.a + self.b
        elif self.operations == "sub":
            return self.a - self.b
        elif self.operations == "mul":
            return self.a * self.b
        elif self.operations == "div":
            return self.a/self.b
        else:
            return "Error:Invalid operation"
        

c1 = Calculator(10,5,"add")
print(c1.calculate())

c2 = Calculator(5,5,"mul")
print(c2.calculate())
            

        
