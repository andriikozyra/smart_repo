import os
import sys
import re
import codecs

def  find_longest_word(path):
    _path = os.path.join(sys.path[0], path)
    if os.path.exists(_path):
        f = codecs.open(_path, encoding='utf-8')
        content = f.read()
        words = re.findall(r"[\w']+", content)
        maxWord = ''
        for word in words:
            if len(word) > len(maxWord):
                maxWord = word
        return maxWord

def find_all_longest_words(dir):
    _path = os.path.join(sys.path[0], dir)
    dict = {}
    if os.path.exists(_path):
        for file in os.listdir(_path):
            dict[file] = find_longest_word(dir + "\\" + file)
    return dict

print(find_longest_word("files\\5.4\\43-0.txt"))
print(find_all_longest_words("files\\5.4"))
