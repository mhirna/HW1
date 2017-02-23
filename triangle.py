class Triangle:
    def __init__(self, point1, point2, point3):
        all_points = [point1, point2, point3]

    def line_len(self, point1, point2):
        return sqrt((point1.get_xposition() - point2.get_xposition()) ** 2 +
                    (point1.get_yposition() - point2.get_yposition()))

    def is_triangle(self):
        sides = [self.line_len()]
