# Implement a class -Student
# has four properties and two methods

# Task 1
# Implement a constructor to initialize the values of four properties: name, phy, chem, and bio.

# Task 2
# Implement a method – totalObtained – in the Student class that calculates total marks of a student.

# Task 3
# Using the totalObtained method, implement another method, percentage, in the Student class that calculates the percentage of students marks

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem 
        self.bio = bio
        pass

    def totalObtained(self):
        total_score = self.phy + self.chem + self.bio
        return total_score
        pass

    def percentage(self):
        perc = (self.totalObtained()/300) * 100
        return perc
        pass

student_1 = Student("Mark", 80, 90, 40)
print(student_1.totalObtained())
print(student_1.percentage())
