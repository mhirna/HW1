from classroom import Classroom

class AcademicBuilding:
    def __init__(self, address, classrooms):
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        eq = []
        for i in self.classrooms:
            eq += i.equipment
        return list(set([(i, eq.count(i)) for i in eq]))

    def __str__(self):
        return "{} \n".format(self.address) + '\n'.join([i.__str__() for i in self.classrooms])
