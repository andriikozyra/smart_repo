def strsort(string):
    result = ''
    for i in sorted(string):
        result = result + i
    return (result)

print(strsort('lgtdkpdcba'))