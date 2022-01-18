def  most_repeating_word(words):
    repeatedLetter = []
    for word in words:
        repeatedLetter.append(repeatedLettersCount(sorted(word)))
    
    isMax = False
    for i, num in enumerate(repeatedLetter):
        if num is not repeatedLetter[i - 1]:
            isMax = True
            break
    
    if isMax == True:
        maxIndex = repeatedLetter.index(max(repeatedLetter))
        return 'The maximum word is: ' + words[maxIndex]
    else:
        return 'There is no maximum'

def  repeatedLettersCount(string):
    result = 0
    for i, l in enumerate(string):
        if l == string[i - 1]:
            result += 1
    return result

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']
WORDS1 = ['this', 'is', 'an']

print(most_repeating_word(WORDS))
print(most_repeating_word(WORDS1))