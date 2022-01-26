import os
import sys
import csv

def  passwd_to_csv(pathIn, pathOut):
    _pathIn = os.path.join(sys.path[0], pathIn)
    _pathOut = os.path.join(sys.path[0], pathOut)
    if os.path.exists(_pathIn):
        f = open(_pathIn, 'r')
        c = open(_pathOut, 'a')
        lines = f.readlines()
        for line in lines:
            if line.startswith('#') == False:
                list = line.split(':')
                spamwriter = csv.writer(c)
                spamwriter.writerow([list[0], list[2]])
        c = open(_pathOut, 'r')
        return c.read()

print(passwd_to_csv("files\\5.2.txt", "files\\5.5.csv"))
