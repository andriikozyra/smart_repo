def  join_numbers(count):
    list = [i for i in range(count)]
    return ','.join(map(str, list))

print(join_numbers(15))
