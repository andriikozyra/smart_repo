def  gematria():
    dict = {chr(i + 96): i for i in range(1, 27)}
    return dict

print(gematria())