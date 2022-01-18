def mysum(*args):
    if args is not None:
        result = args[0]
        for i in args:
            if args.index(i) > 0:
                result += i
    return result

print(mysum('abc', 'def'))
print(mysum([1, 2, 3], [4, 5, 6]))
print(mysum(1, 2, 3))