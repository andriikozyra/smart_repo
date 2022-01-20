def  how_many_different_numbers(list):
    dict = {}
    for i in list:
        num = str(i)
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    return dict

numbers = [1, 2, 3, 1, 2, 3, 4, 1]
print(how_many_different_numbers(numbers))