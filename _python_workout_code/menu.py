def  menu(**kwargs):
    x = raw_input('Enter a letter: ')
    while True:
        if x in kwargs:
            return x
        else:
            x = raw_input('Error. Try again. Enter a letter: ')
