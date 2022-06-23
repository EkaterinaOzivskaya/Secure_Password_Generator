import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
totpw = input('Укажите количество паролей для генерации:')
lenpw = input('Укажите длину одного пароля:')
dig_on = input('Включать ли цифры 0123456789? (y/n)')
if dig_on.lower() == 'yes' or dig_on.lower() == 'да'or dig_on.lower() == 'y':
    chars += digits
upperlet_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
if upperlet_on.lower() == 'yes' or upperlet_on.lower() == 'да' or upperlet_on.lower() == 'y':
    chars += uppercase_letters
lowerlet_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
if lowerlet_on.lower() == 'yes' or lowerlet_on.lower() == 'да' or lowerlet_on.lower() == 'y':
    chars += lowercase_letters
char_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
if char_on.lower() == 'yes' or char_on.lower() == 'да' or char_on.lower() == 'y':
    chars += punctuation
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
if exc_on.lower() == 'yes' or exc_on.lower() == 'да' or exc_on.lower() == 'y':
    for i in  'il1Lo0O':
        if i in chars:
            chars = chars.replace(i, '')

def generate_password(length, chars):    
    return random.sample(chars, int(length))

for _ in range(int(totpw)):
    print(*generate_password(lenpw, chars), sep='')
