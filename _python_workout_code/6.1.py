def  myxml(*args, **kwargs):
    result = ''
    tag = getString(args, 0)
    text = getString(args, 1)
    attributes = ''
    for i in kwargs:
        attributes += ' ' + i + '="' + str(kwargs[i]) + '"'
    result = '<' + tag + attributes + '>' + text + '</' + tag + '>'
    return result

def getString(args, index):
    try:
        string = args[index]
    except:
        string = ''
    return string

print(myxml('foo'))
print(myxml('foo', 'bar'))
print(myxml('foo', 'bar', a=1, b=2, c=3))
print(myxml())
