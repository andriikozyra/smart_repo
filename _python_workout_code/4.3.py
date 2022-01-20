def  dictdiff(dict1, dict2):
    diff = {}
    for d in dict1:
        if d in dict2:
            if dict1[d] != dict2[d]:
                diff[d] = [dict1[d], dict2[d]]
        else:
            diff[d] = [dict1[d], None]
    for d in dict2:
        if d not in dict1:
            diff[d] = [None, dict2[d]]
    return diff

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}

print(dictdiff(d1, d1))
print(dictdiff(d1, d2))
print(dictdiff(d3, d4))
print(dictdiff(d1, d5))