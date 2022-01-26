import operator

def  calc(str):
    list = str.split()
    try:
        return calculate(list[1:], list[0])
    except:
        return 'Error: function "' + list[0] + '" doesnt exist'

def  calculate(list, oper):
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '%' : operator.mod,
        '**' : operator.pow,
    }
    return ops[oper](int(list[0]), int(list[1]))

print(calc('+ 2 3'))
print(calc('- 2 3'))
print(calc('* 2 3'))
print(calc('/ 2 3'))
print(calc('% 2 3'))
print(calc('** 2 3'))
print(calc('. 2 3'))
