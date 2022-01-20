def  get_rainfall():
    dict = {}
    while True:
        city = raw_input('Enter city: ')
        if not city:
            break
        rain = raw_input('Enter rainfall: ')
        if rain.isdigit():
            if city in dict:
                dict[city] += int(rain)
            else:
                dict[city] = int(rain)
    result = ''
    for d in dict:
        result += d + ': ' + str(dict[d]) + '\n'
    print(result)

get_rainfall()