from animal import Animal

class Cage():
    ID = 0
    def __init__(self, id):
        self.ID = id
        self.animals = []

    def add_animals(self, *args):
        for i in args:
            if isinstance(i, Animal):
                self.animals.append(i)

    def __repr__(self):
        return str(self.ID) + '\n' + '\n'.join(i.__repr__() for i in self.animals)
