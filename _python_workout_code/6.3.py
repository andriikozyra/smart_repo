import random

def  create_password_generator(str):
    def create_password(length):
        result = ''
        for i in range(length):
            result += random.choice(str)
        return result
    return create_password

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))
print(alpha_password(10))
print(symbol_password(5))
print(symbol_password(10))
