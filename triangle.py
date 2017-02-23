from math import *
from point import Point

class Triangle:
    def __init__(self, point1, point2, point3):
        self.points = [point1, point2, point3]

    def line_len(self, point1, point2):
        return sqrt((point1.get_xposition() - point2.get_xposition()) ** 2 +
                    (point1.get_yposition() - point2.get_yposition()) ** 2)

    def get_sides(self):
        s1 = self.line_len(self.points[0], self.points[1])
        s2 = self.line_len(self.points[1], self.points[2])
        s3 = self.line_len(self.points[2], self.points[0])
        return s1, s2, s3

    def is_triangle(self):
        s1, s2, s3 = self.get_sides()
        if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
            return True
        return False

    def perimeter(self):
        return sum(self.get_sides())

    def area(self):
        s1, s2, s3 = self.get_sides()
        half = (s1 + s2 + s3) / 2
        return sqrt(half * (half - s1) * (half - s2) * (half - s3))
