import os
import sys

def  get_final_line(path):
    _path = os.path.join(sys.path[0], path)
    if os.path.exists(_path):
        f = open(_path, 'r')
        lines = f.readlines()
        return lines[-1]

print(get_final_line("files\\5.1.txt"))
