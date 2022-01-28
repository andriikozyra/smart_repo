class Animal():
    def __init__(self):
        self.species = ''
        self.color = ''
        self.legs = 0

    def __repr__(self):
        return self.color.capitalize() + ' ' + self.species + ', ' + str(self.legs) + ' legs'

class Sheep(Animal):
    def __init__(self, color):
        self.species = 'sheep'
        self.legs = 4
        self.color = color

class Wolf(Animal):
    def __init__(self, color):
        self.species = 'wolf'
        self.legs = 4
        self.color = color

class Snake(Animal):
    def __init__(self, color):
        self.species = 'snake'
        self.legs = 0
        self.color = color

class Parrot(Animal):
    def __init__(self, color):
        self.species = 'parrot'
        self.legs = 2
        self.color = color
