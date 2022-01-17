def pig_latin(string):
    result = ''
    if string[0]=='A' or string[0]=='a' or string[0]=='E' or string[0]=='e' or string[0]=='I' or string[0]=='i' or string[0]=='O' or string[0]=='o' or string[0]=='U' or string[0]=='u':
        result = string + 'way'
    else:
        firstLetterOld = string[0]
        firstLetterNew = string[1]
        if firstLetterOld.isupper() == True:
            firstLetterNew = firstLetterNew.upper()
        result = firstLetterNew + string[2:] + firstLetterOld.lower() + 'ay'
    return (result)

print(pig_latin('Asshole'))
print(pig_latin('Motherfucker'))