# Class Rectangle
# two private properties: length and width 
# area() l * b 
# perimeter() 2* (l*b)


class Rectangle:
    def __init__(self, length = None, width = None):
        self.__length = length
        self.__width = width
        pass

    def area(self):
        return self.__length*self.__width
        pass

    def perimeter(self):
        return 2*(self.__length+self.__width)
        pass

cal_rect = Rectangle(4, 5)
print(cal_rect.area())
print(cal_rect.perimeter())