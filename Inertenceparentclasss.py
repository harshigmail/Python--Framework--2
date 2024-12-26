class Calculator:
    num = 100  # -------------------------variable

    def getdata(self):  # -------------------------method
        print("i am now executing method")

    def data2(self):
        print("good data")


obj = Calculator()  # -------------------------object
obj.getdata()
obj.data2()
print(obj.num)
