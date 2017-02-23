class Building:
    def __init__(self, building, address):
        self.building = building
        self.address = address


class House(Building):
    def __init__(self, building, address, appartements):
        self.appartements = appartements
        super().__init__(building, address)


class AcademicBuilding(Building):
    def __init__(self, address, classrooms):
        self.classrooms = classrooms
        super().__init__('Academic Building', address)

    def total_equipment(self):
        eq = []
        for i in self.classrooms:
            eq += i.equipment
        return list(set([(i, eq.count(i)) for i in eq]))

    def __str__(self):
        return "{} \n".format(self.address) + '\n'.join([i.__str__() for i in self.classrooms])

