class Bowl():
    MAX =  3
    def __init__(self):
        self.bowl = []
    
    def add_scoops(self, *args):
        for i in args:
            if len(self.bowl) < self.MAX:
                try:
                    self.bowl.append(i.flavor)
                except:
                    pass

    def __repr__(self):
        return '\n'.join(self.bowl)
