class FlexibleDict():
    def __init__(self):
        self.dict = {}

    def __setitem__(self, key, value):
        self.dict[str(key)] = value

    def __getitem__(self, key):
        try:
            return self.dict[str(key)]
        except:
            return None
