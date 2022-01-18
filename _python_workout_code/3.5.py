def  format_sort_records(people):
    result = ''
    for p in people:
        lastName = "{:<10}".format(p[1])
        firstName = "{:<10}".format(p[0])
        time = "{:>5}".format("{:.2f}".format(round(p[2], 2)))
        result += lastName + firstName + time + '\n'
    return result

PEOPLE = [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

print(format_sort_records(PEOPLE))