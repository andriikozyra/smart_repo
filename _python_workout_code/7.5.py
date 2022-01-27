def  flip_dict(dict):
    _dict = {dict[key]:key for key in dict}
    return _dict

dict = {'a':1, 'b':2, 'c':3}
print(flip_dict(dict))
