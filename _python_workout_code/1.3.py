def run_timing():
    totalTime = 0
    runs = 0
    while True:
        x = raw_input('Enter 10 km run time: ')
        if is_float(x):
            runs += 1
            totalTime += float(x)
        if len(x) == 0:
            print ('Average of ' + str(totalTime/runs) + ', over ' + str(runs) + ' runs')
            break

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

run_timing()