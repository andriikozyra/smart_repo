import os
import sys

def  wordcount(path):
    _path = os.path.join(sys.path[0], path)
    dict = {}
    if os.path.exists(_path):
        f = open(_path, 'r')
        content = f.read()        
        characters = len(content)
        words = len(content.split())
        lines = int(content.count('\n')) + 1
        uniqueWords = len(set(content.split()))
        return 'Number of characters - ' + str(characters) + '\nNumber of words - ' + str(words) + '\nNumber of lines - ' + str(lines) + '\nNumber of unique words - ' + str(uniqueWords)

print(wordcount("files\\5.3.txt"))
