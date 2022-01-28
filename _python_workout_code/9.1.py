from scoop import Scoop

def create_scoops():
    ice_1 = Scoop('chocolate')
    ice_2 = Scoop('vanilla')
    ice_3 = Scoop('persimmon')
    return [ice_1.flavor, ice_2.flavor, ice_3.flavor]

print(create_scoops())