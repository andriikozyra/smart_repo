def firstlast(value):
    return value[slice(0, len(value), len(value)-1)]

print(firstlast('AgtdkpdcbB'))
print(firstlast([5, 6, 7]))
print(firstlast((12, 15.5, 'dinosaur')))