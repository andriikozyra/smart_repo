import os
import sys

def  passwd_to_csv(pathIn, pathOut):
    _pathIn = os.path.join(sys.path[0], pathIn)
    _pathOut = os.path.join(sys.path[0], pathOut)
    if os.path.exists(_pathIn):
        f = open(_pathIn, 'r')
        c = open(_pathOut, 'w')
        lines = f.readlines()
        for line in lines:
            c.write(line[::-1].replace('\n', '')+'\n')
        c = open(_pathOut, 'r')
        return c.read()

print(passwd_to_csv("files\\5.7\\input.txt", "files\\5.7\\output.txt"))
