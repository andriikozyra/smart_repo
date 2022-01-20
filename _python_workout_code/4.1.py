MENU = {'sandwitch': 10, 'tea': 7, 'coffee': 8}

def  restaurant():
    cost = 0
    while True:
        x = raw_input('Order: ')
        if len(x) == 0:
            print('Your total is ' + str(cost))
            break
        elif x in MENU:
            cost += MENU[x]
            print(x + ' costs ' + str(MENU[x]) + ', total is ' + str(cost))
        else:
            print('Sorry, we are fresh out of ' + x + ' today.')

restaurant()