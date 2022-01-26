import os
import sys

def  get_final_line(path):
    _path = os.path.join(sys.path[0], path)
    dict = {}
    if os.path.exists(_path):
        f = open(_path, 'r')
        lines = f.readlines()
        for line in lines:
            if line.startswith('#') == False:
                list = line.split(':')
                dict[list[0]] = list[2]
    return dict

print(get_final_line("files\\5.2.txt"))
