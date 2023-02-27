class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def afficherX(self):
        return self.x
    def afficherY(self):
        return self.y

    def changerx(self, newx):
        self.x = newx
    def changery(self, newy):
        self.y = newy

Point1 = Point(10,20)
print(Point1.afficherLesPoints())
Point1.changerx(20)
print(Point1.afficherLesPoints())