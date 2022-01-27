import imp
open_file, file_name, description = imp.find_module('2.2')
plModule = imp.load_module('2.2', open_file, file_name, description)
pigLatin = plModule.pig_latin
# !!!!!!!!!!! NEVER AGAIN !!!!!!!!!!! I WILL HAVE NUMBERS or DOTS IN MY .PY FILE NAME
# from pigLatin import pig_latin

import os
import sys

def  plword(path):
    _path = os.path.join(sys.path[0], path)
    if os.path.exists(_path):
        f = open(_path, 'r')
        return pigLatin(f.read())

print(plword("files\\7.4.txt"))
