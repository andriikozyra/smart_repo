from animal import Sheep, Wolf, Snake, Parrot
from cage import Cage
from zoo import Zoo

sheep = Sheep('white')
wolf = Wolf('grey')
snake = Snake('green')
parrot = Parrot('red')
wolf2 = Parrot('blue')
parrot2 = Parrot('grey')

c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)
c3 = Cage(3)
c3.add_animals(parrot2, wolf2)

z = Zoo()
z.add_cages(c1, c2, c3)
print(z)
print('-------------')
print(z.animals_by_color('grey'))
print('-------------')
print(z.animals_by_legs(2))
print('-------------')
print(z.number_of_legs())
