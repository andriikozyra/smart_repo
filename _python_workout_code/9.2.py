from scoop import Scoop
from bowl import Bowl

def create_bowl():
    ice_1 = Scoop('chocolate')
    ice_2 = Scoop('vanilla')
    ice_3 = Scoop('persimmon')

    bowl = Bowl()
    bowl.add_scoops(ice_1, ice_2)
    bowl.add_scoops(ice_3)
    bowl.add_scoops(45, 'fucking fuck mazafucka')
    return bowl

print(create_bowl())