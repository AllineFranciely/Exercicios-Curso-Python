# from math import factorial
# number = int(input('Digite um número: '))
# fatorial = factorial(number)
# print('O fatorial de {} é {}'.format(number, fatorial))

n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

