import os
import sys
import json

def  print_scores(dir):
    _dir = os.path.join(sys.path[0], dir)
    if os.path.exists(_dir):
        for file in os.listdir(_dir):
            _path = os.path.join(_dir, file)
            json_data = open(_path).read()
            print(json_data)

print_scores("files\\5.6")
