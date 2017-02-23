class Classroom:
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, classroom):
        return self.capacity > classroom.capacity

    def equipment_differences(self, classroom):
        return [i for i in self.equipment if i not in classroom.equipment]

    def __str__(self):
        return "Classroom {} has a capacity of {} persons and " \
               "has the following equipment: {}.".format(self.number, str(self.capacity), ", ".join(self.equipment))

    def __repr__(self):
        return 'Classroom({}, {}, {})'.format(self.number, self.capacity, self.equipment)
