import os
import sys

def  get_sv(path):
    _path = os.path.join(sys.path[0], path)
    if os.path.exists(_path):
        f = open(_path, 'r')
        vowels = {'a', 'e', 'i', 'o', 'u'}
        _set = set(word for word in f.read().split() if set(word.lower()) > vowels)
        return _set

print(get_sv("files\\7.7.txt"))