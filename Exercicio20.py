import random
n1 = str(input('Primeiro grupo:'))
n2 = str(input('Segundo grupo:'))
n3 = str(input('Terceiro grupo:'))
n4 = str(input('Quarto grupo:'))
grupos = [n1, n2, n3, n4]
random.shuffle(grupos)
print('A ordem de apresentação será')
print(grupos)
