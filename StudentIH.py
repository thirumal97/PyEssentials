class Student:
    def __init__(self, name = None, rollNumber = None):
        self.__name = name
        self.__rollNumber = rollNumber

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    def getRollNumber(self):
        return self.__rollNumber
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

demo1 = Student()
print("initially, ", demo1.getName(), demo1.getRollNumber())
demo1.setName("Alex")
print(demo1)
demo1.setRollNumber(2415)
print(demo1.getRollNumber())