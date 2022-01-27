import os
import sys

def  gematria_for(word):
    result = sum([ord(i) - 96 for i in word])
    return result

def  gematria_equal_words(word):
    _path = os.path.join(sys.path[0], "files\\7.7.txt")
    if os.path.exists(_path):
        f = open(_path, 'r')
        _dict = {word.lower():gematria_for(word.lower()) for word in f.read().split()}
        _list = [key for key, value in _dict.items() if value == gematria_for(word)]
    return _list

print(gematria_for('cat'))
print(gematria_equal_words('cat'))
