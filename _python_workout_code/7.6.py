def  transform_values(func, dict):
    _dict = {key:func(value) for key, value in dict.items()}
    return _dict

dict = {'a':1, 'b':2, 'c':3}
print(transform_values(lambda x: x*x, dict))