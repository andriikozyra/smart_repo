from re import S
from menu import menu

def func_a():
    return "A"
def func_b():
    return "B"

return_value = menu(a=func_a, b=func_b)

print('Result is ' + str(return_value))
