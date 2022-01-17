def ubbi_dubbi(string):
    listWords = string.split()
    result = ''
    for word in listWords:
        index = listWords.index(word)
        newWord = ''
        for letter in word:
            if letter in 'AEIOU' or letter in 'aeiou':
                if letter.isupper():
                    prefix = 'Ub'
                else:
                    prefix = 'ub'
                newWord = newWord + prefix + letter.lower()
            else:
                newWord = newWord + letter
        listWords[index] = newWord
        result = result + listWords[index]
        if index < len(listWords) - 1:
            result = result + ' '
    return (result)

SENTANCE = 'Ubbi Dubbi is a common children`s secret language in Englishspeaking countries'
print(ubbi_dubbi(SENTANCE))