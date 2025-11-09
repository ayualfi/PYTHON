class summation:
    def sum(self, a, b):
        c = a + b
        print("Sum= ", c)
class multiplication:
    def multi(self, a, b):
        c = a * b
        print("Multi= ", c)
class calculator(summation, multiplication):
    def devide(self, a, b):
        c = a / b
        print("Devide= ", c)

hitung=calculator()
hitung.sum(10, 15)
hitung.multi(10, 15)
hitung.devide(10, 15)
