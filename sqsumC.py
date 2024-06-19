class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x*self.x) + (self.y*self.y) + (self.z*self.z)

ob = Point(1, 3, 5)
print(ob.sqSum())
