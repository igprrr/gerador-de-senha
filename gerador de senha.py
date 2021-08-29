import random
chars = 'abcdefghijklmnopqrstuvwxyz'
chars += chars.upper()
num = str(1234567890)
simb = '!@#$%^&*()_'
chars += num + simb
#tamanho
tam = 8
senha = ''.join(random.sample(chars, tam))
print(senha)
