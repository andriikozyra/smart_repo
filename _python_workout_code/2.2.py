def pig_latin(string):
    listWords = string.split()
    result = ''
    for word in listWords:
        index = listWords.index(word)
        if word[0] in 'AEIOU' or word[0] in 'aeiou':
            listWords[index] = word + 'way'
        else:
            firstLetterOld = word[0]
            firstLetterNew = word[1]
            if firstLetterOld.isupper() == True:
                firstLetterNew = firstLetterNew.upper()
            listWords[index] = firstLetterNew + word[2:] + firstLetterOld.lower() + 'ay'
        result = result + listWords[index]
        if index < len(listWords) - 1:
            result = result + ' '
    return (result)

SENTANCE = 'Pig Latin is a common children`s secret language in Englishspeaking countries'
print(pig_latin(SENTANCE))