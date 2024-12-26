from Inertenceparentclasss import Calculator


class ChildClass(Calculator):
    num2 = 200

    def getCompleteData(self):
        return self.num2 + self.num

    def getCompleteData1(self):
        return self.data2()


objChild = ChildClass()
print(objChild.getCompleteData())
print(objChild.getCompleteData1())
