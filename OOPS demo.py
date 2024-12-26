# class contains variable, method, object
import self


class Calculator:
    num = 100  # -------------------------variable

    def getdata(self):  # -------------------------method
        print("i am now executing method")


obj = Calculator()  # -------------------------object
obj.getdata()
print(obj.num)


# using constructor
class Calculator1:
    num = 100  # ------------------------class variable

    def __init__(self):  # ----constructor
        print("I am called automatically when object is created")

    def getdata(self):  # -------------------------method
        print("i am now executing method")


obj1 = Calculator1()  # -------------------------object
man = 22  # -----------------------instance variable (inside object)
obj1.getdata()
print(obj1.num)
print("*****************")


# calling parameters using instance variables in class
class Calculator2:
    num = 100  # ------------------------class variable

    def __init__(self, a, b):  # self is nothing but object
        self.firstnumber = a
        self.secondnumber = b

    # if we want to call any variable in any method

    def Summation(self):
        return self.firstnumber + self.secondnumber



obj2 = Calculator2(4, 7)  #-------------------------object
print(obj2.Summation())

obj3 = Calculator2(3, 2)  # -------------------------object
print(obj3.Summation())
# instance variable values changes always when  every object is called
# self keyword is important when calling variables into method
# constructor name should be init
