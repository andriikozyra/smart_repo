from flexibleDict import FlexibleDict

fd = FlexibleDict()
fd['a'] = 100
print(fd['a'])
fd[5] = 500
print(fd[5])
fd[1] = 100
print(fd['1'])
fd['1'] = 100
print(fd[1])
