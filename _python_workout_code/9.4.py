from scoop import Scoop
from bowlBig import BowlBig

def create_bowl():
    ice_1 = Scoop('chocolate')
    ice_2 = Scoop('vanilla')
    ice_3 = Scoop('persimmon')
    ice_4 = Scoop('shit')
    ice_5 = Scoop('piss')
    ice_6 = Scoop('squirt')

    bowl = BowlBig()
    bowl.add_scoops(ice_1, ice_2, 'fucking fuck mazafucka', ice_3, ice_4, ice_5, 45, ice_6)
    return bowl

print(create_bowl())