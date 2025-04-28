import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, point1, point2, point3):
        self.__points = [point1, point2, point3]  # Lista privada de 3 puntos

    def perimeter(self):
        p1, p2, p3 = self.__points
        side1 = p1.distance_from_point(p2)
        side2 = p2.distance_from_point(p3)
        side3 = p3.distance_from_point(p1)
        return side1 + side2 + side3

# Ejemplo de uso:
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())  # 12.0
