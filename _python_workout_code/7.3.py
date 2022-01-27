def  flatten(list):
    _list = [j for i in list for j in i]
    return _list

print(flatten([[1,2], [3,4]]))
