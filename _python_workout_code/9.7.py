from animal import Sheep, Wolf, Snake, Parrot
from cage import Cage

sheep = Sheep('white')
wolf = Wolf('grey')
snake = Snake('green')
parrot = Parrot('red')

c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)

print(c1)
print(c2)
