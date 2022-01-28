from cage import Cage

class Zoo():
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        for i in args:
            if isinstance(i, Cage):
                self.cages.append(i)

    def animals_by_color(self, color):
        return color.capitalize() + ' animals are: \n' + '\n'.join(a.__repr__() + ' in cage #' + str(c.ID) for c in self.cages for a in c.animals if a.color == color)

    def animals_by_legs(self, legs):
        return str(legs) + '-legs animals are: \n' + '\n'.join(a.__repr__() + ' in cage #' + str(c.ID) for c in self.cages for a in c.animals if a.legs == legs)

    def number_of_legs(self):
        listLegs = [a.legs for c in self.cages for a in c.animals]
        return 'The zoo has in total ' + str(sum(listLegs)) + ' legs'

    def __repr__(self):
        return '\n'.join(c.__repr__() for c in self.cages)
