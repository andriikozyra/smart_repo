def  sum_numbers(str):
    list = [int(i) for i in str.split() if i.isdigit()]
    return sum(list)

print(sum_numbers('10 abc 20 de44 30 55fg 40'))
