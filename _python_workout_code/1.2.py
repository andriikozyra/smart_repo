def mysum(*args):
    sum = 0
    if args is not None:
        for i in args:
            if type(i) is list:
                sum += mysumList(i)
            elif type(i) is int or type(i) is float:
                sum += i
    return sum

def mysumList(list):
    sum = 0
    for i in list:
        if type(i) is int or type(i) is float:
            sum += i
    return sum

print (sum([1, 2, 3]), mysum([1, 2, 3]), mysum(1, 2, 3), mysum(1, 'apple', 3.5))